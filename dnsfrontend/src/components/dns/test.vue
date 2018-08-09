<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right" style="font-size: 14px">
      <el-breadcrumb-item :to="{ path: '/dns-dashboard' }"><i class="el-icon-menu"></i> 首页</el-breadcrumb-item>
      <el-breadcrumb-item>专线用户分析</el-breadcrumb-item>
    </el-breadcrumb>

    <div class="handle-box">
      <el-form :model="formFilter" ref="formFilter" style="display:inline-block">
        <el-row :gutter="10">
          <el-col class="handle-select-input">
            <el-form-item prop="select_customer">
              <el-select placeholder="客户"  size="small" v-model="formFilter.select_customer" clearable >
                <el-option v-for="item in items" :label="item" :value="item" :key="item"></el-option>
              </el-select>
            </el-form-item>
          </el-col>
          <el-col :span="4.5">
            <el-form-item>
              <el-date-picker
                v-model="valueDate"
                type="date"
                size="small"
                @change="handleDatePick"
                value-format="yyyyMMdd"
                placeholder="选择日期">
              </el-date-picker>
            </el-form-item>
          </el-col>
          <el-col :span="2">
            <el-form-item>
              <el-button type="primary" icon="el-icon-search" size="small" @click="DataFilter()">分析</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </div>
    <div style="margin:0 -20px;">
      <el-row class="panel-group">
        <el-col :xs="24" :sm="24" :lg="12" class="panel-group-col" id="chart">
          <div class="div-css">
            <icon name="item" scale="2" style="padding-right: 5px; margin-left: -10px; float:left; margin-top:10px"></icon><span class="item-font">访问云业务类型占比</span>
            <div id="chart2" style="display:inline-block"></div>
          </div>
        </el-col>
        <el-col :xs="24" :sm="24" :lg="12" class="panel-group-col">
          <div class="div-css">
            <icon name="item" scale="2" style="padding-right: 5px; margin-left: -10px; float:left; margin-top:10px"></icon><span class="item-font">工作时间访问公有云占比</span>
            <div id="chart3" style="display:inline-block"></div>
          </div>
        </el-col>
        <el-col :xs="24" :sm="24" :lg="12" class="panel-group-col">
          <div class="div-css">
            <icon name="item" scale="2" style="padding-right: 5px; margin-left: -10px; float:left; margin-top:10px"></icon><span class="item-font">非工作时间访问公有云占比</span>
            <div id="chart4" style="display:inline-block"></div>
          </div>
        </el-col>

        <el-col :xs="24" :sm="24" :lg="12" class="panel-group-col">
          <div class="div-css">
            <icon name="item" scale="2" style="padding-right: 5px; margin-left: -10px; float:left; margin-top:10px"></icon><span class="item-font">公有云访问量</span>
            <div id="chart1" style="display:inline-block"></div>
          </div>
        </el-col>
      </el-row>
    </div>

  </div>
</template>

<script>
  import { restful_path } from '../util.js'
  import _ from 'lodash'
  require('echarts/theme/infographic')
  require('echarts/theme/shine')
  require('echarts/theme/macarons')
  export default {
    data() {
      return {
        data: [],
        userData:[
        ],
        cloudData:[],
        top5CloudDomain:[],
        top5NotCloudDomain:[],
        items: [],
        formFilter: {
          select_customer: ''
        },
        valueDate:'20180103',
        pageSize:10,
        currentPage:1,
        maxCount:0,
        chart1: null,
        chart2: null,
        chart3: null,
        chart4: null
      }
    },
    mounted () {
      this.init();
      const that = this;
      window.addEventListener('resize', _.throttle(() => {
        console.log(that.chart2);
        that.chart2.resize();
       }, 500))
    },
    methods: {
      handleDatePick () {
      },
      getDropDownList () {
        this.$http({
          method: 'get',
          url: restful_path + '/api/dns/get-customer-info'
        }).then(response => {
          if(response.data.status){
            this.items = response.data.data;
          }
        }).catch(error => {});
      },

      init() {
        var chart2 = document.getElementById('chart2');
        var chart = document.getElementById('chart');
        var chart2Container = function () {
            chart2.style.width = (chart.clientWidth - 50) +'px';
            chart2.style.height = '300px';
        };
        chart2Container();
        this.chart2 = chart2;
        this.chart2 = this.$echarts.init(chart2, 'macarons');
      },

      //用户共有公有云访问量
      userCloudChartFilter(){
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/get-customer-cloud-count-chart',
          data: {
            'customer_name': this.formFilter.select_customer,
            'date': this.valueDate
          }
        }).then(response => {
          if(response.data.status){
            let i = 0;
            let a = new Array(23);
            for(i=0; i<24; i ++) {
              a[i] = i;
            }
            this.drawChart1(response.data.data['腾讯云'], response.data.data['阿里云'], a);
            let max = 0;
            for(let i =0; i<24; i++) {
              if(response.data.data['腾讯云'][i] + response.data.data['阿里云'][i] > max){ max = response.data.data['腾讯云'][i] + response.data.data['阿里云'][i];}
            }
            this.drawChart3(response.data.data['腾讯云'].slice(8,19), response.data.data['阿里云'].slice(8,19), a.slice(8,19), max);
            this.drawChart4(response.data.data['腾讯云'].slice(19).concat(response.data.data['腾讯云'].slice(0,8)), 
              response.data.data['阿里云'].slice(19).concat(response.data.data['阿里云'].slice(0,8)), 
              a.slice(19).concat(a.slice(0,8)), max);
          }
        }).catch(error => {
          console.log(error);
        });
      },

      userCloudServiceNameChartFilter(){
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/get-customer-top-cloud-service-name',
          data: {
            'customer_name': this.formFilter.select_customer,
            'date': this.valueDate,
            'n':5
          }
        }).then(response => {
          if(response.data.status){
            let service_name = [];
            let tmp = [];
            let d = {};
            for(let i=0; i<response.data.data.length; i++){
              service_name.push(response.data.data[i].service_name);
              d = {};
              d.name = response.data.data[i].service_name;
              d.value = response.data.data[i].count;
              tmp.push(d);
            }
            var chart2 = document.getElementById('chart2');
            var chart = document.getElementById('chart');
            var chart2Container = function () {
                chart2.style.width = (chart.clientWidth - 50) +'px';
                chart2.style.height = '300px';
            };
            chart2Container();
            this.chart2 = chart2;
            this.chart2 = this.$echarts.init(chart2, 'macarons');
            this.chart2.setOption({
              tooltip : {
                trigger: 'item',
                formatter: "{a} <br/>{b} : {c} ({d}%)"
              },
              legend: {
                orient: 'horizontal',
                //left: 'top',
                data: service_name
              },
              series : [
                {
                  name: '访问量',
                  type: 'pie',
                  radius : '60%',
                  center: ['50%', '50%'],
                  data: tmp,
                  itemStyle: {
                    emphasis: {
                      shadowBlur: 10,
                      shadowOffsetX: 0,
                      shadowColor: 'rgba(0, 0, 0, 0.5)'
                    }
                  }
                }
              ]
            });
            //this.drawChart2(service_name, tmp);
          }
        }).catch(error => {
          console.log(error);
        });
      },

      DataFilter() {
        this.userCloudChartFilter();
        this.userCloudServiceNameChartFilter();
      },

      drawChart1(list1, list2, list3) {
        var chart1 = document.getElementById('chart1');
        var chart = document.getElementById('chart');
        var chart1Container = function () {
            chart1.style.width = (chart.clientWidth) +'px';
            chart1.style.height = '300px';
        };
        chart1Container();
        this.chart1 = chart1;
        console.log(this.chart1.style.width)
        //console.log(chart.clientWidth)
        this.chart1 = this.$echarts.init(chart1, 'macarons');
        this.chart1.setOption({
          tooltip : {
            trigger: 'axis',
            axisPointer : {
              type : 'shadow'
            }
          },
          legend: {
            data:['腾讯云','阿里云']
          },
          grid: {
            left: '3%',
            right: '10%',
            bottom: '15%',
            top:'10%',
            containLabel: true
          },
          xAxis : [
            {
              type : 'category',
              boundaryGap: false,
              data : list3,
              axisTick: {
                alignWithLabel: true
              }
            }
          ],
          yAxis : [
            {
              type : 'value'
            }
          ],
          series : [
            {
              name:'阿里云',
              type:'line',
              //stack: '公有云',
              data: list2
            },
            {
              name:'腾讯云',
              type:'line',
              //stack: '公有云',
              data: list1
            }
          ]
        });
      },
      drawChart2(list1, list2) {
        var chart2 = document.getElementById('chart2');
        var chart = document.getElementById('chart');
        var chart2Container = function () {
            chart2.style.width = (chart.clientWidth - 50) +'px';
            chart2.style.height = '300px';
        };
        chart2Container();
        //this.chart2 = chart2;
        chart2 = this.$echarts.init(chart2, 'macarons');
        chart2.setOption({
          tooltip : {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
          },
          legend: {
            orient: 'horizontal',
            //left: 'top',
            data: list1
          },
          series : [
            {
              name: '访问量',
              type: 'pie',
              radius : '60%',
              center: ['50%', '50%'],
              data: list2,
              itemStyle: {
                emphasis: {
                  shadowBlur: 10,
                  shadowOffsetX: 0,
                  shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
              }
            }
          ]
        });
      },
      drawChart3(list1, list2, list3, max) {
        var chart3 = document.getElementById('chart3');
        var chart = document.getElementById('chart');
        var chart3Container = function () {
            chart3.style.width = (chart.clientWidth - 50) +'px';
            chart3.style.height = '300px';
        };
        chart3Container();
        chart3 = this.$echarts.init(chart3, 'macarons');
        chart3.setOption({
          tooltip : {
            trigger: 'axis',
            axisPointer : {
              type : 'shadow'
            }
          },
          legend: {
            data:['腾讯云','阿里云']
          },
          grid: {
            left: '3%',
            right: '4%',
            bottom: '15%',
            top:'10%',
            containLabel: true
          },
          xAxis : [
            {
              type : 'category',
              data : list3,
              axisTick: {
                alignWithLabel: true
              }
            }
          ],
          yAxis : [
            {
              type : 'value',
              max: max
            }
          ],
          series : [
            {
              name:'阿里云',
              type:'bar',
              stack: '公有云',
              data: list2
            },
            {
              name:'腾讯云',
              type:'bar',
              stack: '公有云',
              data: list1
            }
          ]
        });
      },
      drawChart4(list1, list2, list3, max) {
        var chart4 = document.getElementById('chart4');
        var chart = document.getElementById('chart');
        var chart4Container = function () {
            chart4.style.width = (chart.clientWidth - 50) +'px';
            chart4.style.height = '300px';
        };
        chart4Container();
        chart4 = this.$echarts.init(chart4, 'macarons');
        chart4.setOption({
          tooltip : {
            trigger: 'axis',
            axisPointer : {
              type : 'shadow'
            }
          },
          legend: {
            data:['腾讯云','阿里云']
          },
          grid: {
            left: '3%',
            right: '4%',
            bottom: '15%',
            top:'10%',
            containLabel: true
          },
          xAxis : [
            {
              type : 'category',
              data : list3,
              axisTick: {
                alignWithLabel: true
              }
            }
          ],
          yAxis : [
            {
              type : 'value',
              max: max
            }
          ],
          series : [
            {
              name:'阿里云',
              type:'bar',
              symbolSize:10,
              stack: '公有云',
              data: list2
            },
            {
              name:'腾讯云',
              type:'bar',
              stack: '公有云',
              data: list1
            }
          ]
        });
      },
    },
    created(){
      this.getDropDownList();
    },
    computed: {
      getIsCollapse() {
        return this.$store.state.isCollapse;
      }
    },
    watch: {
      getIsCollapse() {
        setTimeout(() => {
          this.DataFilter();
          //this.chart1.resize();
          //this.chart2.resize();
        }, 300);
      }
    }
  }
</script>

<style lang="scss" scoped>
  ::-webkit-scrollbar
  {
    width: 0;
  }
  .handle-box{
    margin-top: 20px;
    text-align: center;
    margin-bottom: -20px;
  }
  .handle-select-input{
    width: 210px;
  }
  .handle-select-2{
    width: 100px;
  }

  .handle-input{
    width: 300px;
  }

  .el-select-dropdown__item {
    text-align: center;
  }

  .el-input__inner {
    margin-right: 10px;
  }
/*   .panel-group {
    //margin-left: 10px;
    margin-right: 10px;
  }
  .div-css {
    border:1px solid #F7F7F7;
    height: 300px;
    margin: 10px 0px 0 10px;
    padding: 15px 15px;
    box-shadow: 4px 4px 20px rgba(0, 0, 0, 0.05);
    overflow:hidden;
    background-color: #FFF;
    //cursor: pointer;
  } */

  .panel-group {
    margin-left: 10px;
    margin-right: 0px;
  }
  .div-css {
    border:1px solid rgba(0, 0, 0, 0.06);
    height: 300px;
    margin: 10px 10px 0px 0px;
    padding: 0 20px;
    box-shadow: 4px 4px 30px rgba(0, 0, 0, 0.05);
    overflow:hidden;
    background-color: #FFF;
    /* cursor: pointer; */
  }

  .span-style {
    width:100%;
    text-align:center;
    line-height:40px;
    display:block;
    color:#8C8C8C;
  }
  .pic {
    float: left;
    margin: 15px 15px 15px 15px;
  }
  .item-font {
    font-size:14px; 
    line-height:37px; 
    color:#2F3848;
    font-weight: bold;
  }
</style>