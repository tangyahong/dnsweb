<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right" style="font-size: 14px">
      <el-breadcrumb-item :to="{ path: '/index' }"><i class="el-icon-menu"></i> 首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/dns-dashboard' }">DNS日志分析</el-breadcrumb-item>
      <el-breadcrumb-item>重点行业分析</el-breadcrumb-item>
    </el-breadcrumb>

    <div class="handle-box">
      <el-form :model="formFilter" ref="formFilter" style="display:inline-block">
        <el-row :gutter="10">
          <el-col class="handle-select-category">
            <el-form-item prop="select_industry">
              <el-select placeholder="请选择行业" size="small" v-model="formFilter.select_industry" >
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
          <el-col :span="4.5">
            <el-form-item>
              <el-date-picker
                v-model="valueWeek"
                type="week"
                size="small"
                @change="handleWeekPick"
                :picker-options="{
                  firstDayOfWeek: 1
                }"
                format="yyyy 第 WW 周"
                placeholder="选择周">
              </el-date-picker>
            </el-form-item>
          </el-col>

          <el-col :span="2">
            <el-form-item>
              <el-button type="primary" size="small" @click="DataFilter()">确定</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </div>
    <div>
      <el-row >
        <el-col :span="12" style="text-align:center" v-show="showCharts">
          <div id="chart1" style="display:inline-block"></div>
        </el-col>
          <el-col :span="12" style="text-align:center" v-show="showCharts">
          <div id="chart2" style="display:inline-block"></div>
        </el-col>
      </el-row>
    </div>
    <div>
      <el-table
        :data="data"
        border
        style="width: 100%; height:100%"
        ref="multipleTable"
        size="mini">
        <el-table-column prop="id" label="id" align="center" v-if="false">
        </el-table-column>
        <el-table-column prop="category_rank" label="排名" width="50" align="center">
        </el-table-column>
        <el-table-column prop="domain" label="域名" width="140" align="center" >
        </el-table-column>
        <el-table-column prop="tld" label="二级域名" width="140" align="center" >
        </el-table-column>
<!--         <el-table-column prop="stld" label="三级域名" width="140" align="center" >
        </el-table-column> -->
        <el-table-column prop="service_name" label="首页名称" width="100" align="center" >
        </el-table-column>
        <el-table-column prop="category_name" label="域名分类" width="100" align="center" >
        </el-table-column>
        <el-table-column prop="resolved_ip" label="IP解析" align="center" >
        </el-table-column>
        <el-table-column prop="count" label="解析量" width="80" align="center" >
        </el-table-column>
        <el-table-column prop="success_rate" label="解析成功率" width="100" align="center" >
        </el-table-column>
      </el-table>
    </div>
  </div>
  
</template>
<script>
  import { restful_path } from '../util.js'
  export default {
    data() {
      return {
        formFilter: {
          select_industry: '',
        },
        items: [],
        data:[],
        valueDate: '20171201',
        valueWeek: '',
        showCharts: false
      }
    },
    methods: {
      getDropDownList () {
        this.$http({
          method: 'get',
          url: restful_path + '/api/dns/get-category-name'
        }).then(response => {
          this.items = response.data.data;
        }).catch(error => {
          console.log(error);
        });
      },
      handleWeekPick() {
        this.valueDate = '';
        let d = new Date(this.valueWeek);
        let weekFormat = d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate();
        //this.valueWeek = weekFormat;
        //console.log(this.valueWeek)
      },
      handleDatePick() {
        this.valueWeek = '';
      },
      DataFilter() {
        var data;
        if (this.valueDate) {
          data = {
            //'count': 20,
            'category_name': this.formFilter.select_industry,
            'date': this.valueDate,
            'week': ''
          }
        } else {
          let d = new Date(this.valueWeek);
          let weekFormat = d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate();
          data = {
            //'count': 20,
            'category_name': this.formFilter.select_industry,
            'week': weekFormat,
            'date': ''
          }
        }
        //console.log(data);
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/get-category-topn/20',
          data: data
        }).then(response => {
          if(response.data.msg) {
            this.data = response.data.data;
          }
        }).catch(error => {
          console.log(error);
        });
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/get-category-group-new/10',
          data: data
        }).then(response => {
          console.log(response.data.data)
          if(response.data.msg && response.data.data.all.length > 0) {
            this.drawLine(response.data.data.name, response.data.data.value, response.data.data.all);
            this.showCharts = true;
            //console.log(this.showCharts)
          } else {
            this.showCharts = false;
          }
        }).catch(error => {
          console.log(error);
        });
      },
      drawLine(list1, list2, list3){
				var chart1 = document.getElementById('chart1');
				var chart2 = document.getElementById('chart2');
				var chart1Container = function () {
				    chart1.style.width = ((window.innerWidth - 300)/2) +'px';
				    chart1.style.height = '300px';
				};
				var chart2Container = function () {
				    chart2.style.width = ((window.innerWidth - 300)/2) + 'px';
				    chart2.style.height = '300px';
				};
				chart1Container();
				chart2Container();

        // 基于准备好的dom，初始化echarts实例
        chart1 = this.$echarts.init(chart1);
        chart2 = this.$echarts.init(chart2);
        // 绘制图表
        chart1.setOption({
					title : {
            text: this.formFilter.select_industry + '行业解析量',
          },
          tooltip : {
            trigger: 'axis'
          },
          legend: {
            data:['解析量']
          },
/*           toolbox: {
            show : true,
            feature : {
              dataView : {show: true, readOnly: false},
              magicType : {show: true, type: ['line', 'bar']},
              restore : {show: true},
              saveAsImage : {show: true}
            }
          }, */
          calculable : true,
          xAxis : [
            {
              type : 'category',
              data : list1,
              axisLabel:{  
                interval:0,
                rotate:-30
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
              name:'解析量',
              type:'bar',
              data:list2
            }
          ]
        });
        chart2.setOption({
					title : {
		        text: '解析率占比',
		        x:'center'
			    },
			    grid:{
			    	bottom:5,
			    	top: 20,
			    	left: 0,
			    	right: 0
			    },
			    tooltip : {
		        trigger: 'item',
		        formatter: "{a} <br/>{b} : {c} ({d}%)"
			    },
			    legend: {
		        orient: 'vertical',
		        left: 'right',
		        data: list1
          },
			    series : [
		        {
	        		name: '解析量',
	            type: 'pie',
	            radius : '50%',
	            center: ['50%', '52%'],
	            data: list3,
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
      }
    },
    created(){
      this.getDropDownList();
    }
  }
</script>
<style lang="scss" scoped>
  /* @import '../../assets/normalize.css'; */
  .handle-box {
    margin-top: 20px;
    text-align: center
  }
  .el-select-dropdown__item {
    text-align: center;
  }

  .handle-select-category{
    width: 150px;
  }

  .el-input--small {
    .el-input__icon {
      margin-top: 0px !important;
    }
  }
</style>

