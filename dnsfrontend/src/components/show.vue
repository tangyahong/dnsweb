<template>
  <div class="bg">
      <el-row class="panel-group">
        <el-col :xs="24" :sm="24" :lg="24" class="panel-group-col">
          <el-row>
            <el-col :xs="24" :sm="24" :lg="24" class="panel-group-col">
              <div class="test">
                <span style="text-align:center; font-size:30px; color:#43CAF2">DNS大数据</span>
              </div>
            </el-col>
          </el-row>
        </el-col>
        <el-col :xs="24" :sm="24" :lg="8" class="panel-group-col">
          <el-row>
            <el-col :xs="24" :sm="24" :lg="24" class="panel-group-col">
              <div class="div-css" :style="{height:heightData + 'px'}" id="chart_4">
                <div>
                  <div class="border-top-left"></div>
                  <div class="border-top-right"></div>
                </div>
                <span class="item-font">客户基本信息</span>
                <div id="chart4" style="display:inline-block"></div>
                <div>
                  <div class="border-bottom-left"></div>
                  <div class="border-bottom-right"></div>
                </div>
              </div>
            </el-col>
          </el-row>
        </el-col>
        <el-col :xs="8" :sm="8" :lg="8" class="panel-group-col" id="chart">
          <el-row>
            <el-col :xs="24" :sm="24" :lg="24" class="panel-group-col">
              <div class="div-css" :style="{height:heightData + 'px'}" id="chart_1">
                <div>
                  <div class="border-top-left"></div>
                  <div class="border-top-right"></div>
                </div>
                <span class="item-font">访问云业务类型占比</span>
                <div id="chart2" style="display:inline-block"></div>
                <div>
                  <div class="border-bottom-left"></div>
                  <div class="border-bottom-right"></div>
                </div>
              </div>
            </el-col>
          </el-row>
        </el-col>
        <el-col :xs="8" :sm="8" :lg="8" class="panel-group-col">
          <el-row>
            <el-col :xs="24" :sm="24" :lg="24" class="panel-group-col">
              <div class="div-css" :style="{height:heightData + 'px'}">
                <div>
                  <div class="border-top-left"></div>
                  <div class="border-top-right"></div>
                </div>
                <span class="item-font">TOP5云域名</span>
                <div>
                  <div class="border-bottom-left"></div>
                  <div class="border-bottom-right"></div>
                </div>
              </div>
            </el-col>
          </el-row>
        </el-col>
        <el-col :xs="24" :sm="24" :lg="8" class="panel-group-col">
          <el-row>
            <el-col :xs="24" :sm="24" :lg="24" class="panel-group-col">
              <div class="div-css" :style="{height:heightData + 'px'}" id="chart_1">
                <div>
                  <div class="border-top-left"></div>
                  <div class="border-top-right"></div>
                </div>
                <span class="item-font">TOP5非云域名</span>
                <div>
                  <div class="border-bottom-left"></div>
                  <div class="border-bottom-right"></div>
                </div>
              </div>
            </el-col>
          </el-row>
        </el-col>
        <el-col :xs="24" :sm="24" :lg="8" class="panel-group-col">
          <el-row>
            <el-col :xs="24" :sm="24" :lg="24" class="panel-group-col">
              <div class="div-css" :style="{height:heightData /2 -10 + 'px'}" id="chart_1">
                <div>
                  <div class="border-top-left"></div>
                  <div class="border-top-right"></div>
                </div>
                <span class="item-font">非工作时间访问公有云占比1</span>
                <div id="chart1" style="display:inline-block"></div>
                <div>
                  <div class="border-bottom-left"></div>
                  <div class="border-bottom-right"></div>
                </div>
              </div>
            </el-col>
          </el-row>

          <el-row>
            <el-col :xs="24" :sm="24" :lg="12" class="panel-group-col">
              <el-row>
                <el-col :xs="24" :sm="24" :lg="24" class="panel-group-col">
                  <div class="div-css" :style="{height:heightData /2 + 'px'}" id="chart_3">
                    <div>
                      <div class="border-top-left"></div>
                      <div class="border-top-right"></div>
                    </div>
                    <span class="item-font">非工作时间访问公有云占比1</span>
                    <div id="chart7" style="display:inline-block"></div>
                    <div>
                      <div class="border-bottom-left"></div>
                      <div class="border-bottom-right"></div>
                    </div>
                  </div>
                </el-col>
              </el-row>
            </el-col>

            <el-col :xs="24" :sm="24" :lg="12" class="panel-group-col">
              <el-row>
                <el-col :xs="24" :sm="24" :lg="24" class="panel-group-col">
                  <div class="div-css" :style="{height:heightData /2 + 'px'}">
                    <div>
                      <div class="border-top-left"></div>
                      <div class="border-top-right"></div>
                    </div>
                    <span class="item-font">非工作时间访问公有云占比1</span>
                    <div id="chart3" style="display:inline-block"></div>
                    <div>
                      <div class="border-bottom-left"></div>
                      <div class="border-bottom-right"></div>
                    </div>
                  </div>
                </el-col>
              </el-row>
            </el-col>

          </el-row>
        </el-col>

        <el-col :xs="24" :sm="24" :lg="8" class="panel-group-col">
          <el-row>
            <el-col :xs="24" :sm="24" :lg="24" class="panel-group-col">
              <div class="div-css" :style="{height:heightData + 'px'}">
                <div>
                  <div class="border-top-left"></div>
                  <div class="border-top-right"></div>
                </div>
                <span class="item-font">非工作时间访问公有云占比</span>
                <div>
                  <div class="border-bottom-left"></div>
                  <div class="border-bottom-right"></div>
                </div>
              </div>
            </el-col>
          </el-row>
        </el-col>
      </el-row>
  </div>
</template>

<script>
  import { restful_path } from './util.js'
  import { CITY_GEO_COORDS } from './geo.js'
  import 'echarts/map/js/province/guangdong';
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
        heightData: window.screen.availHeight / 2 - 80
      }
    },
    filters: {
    },
    mounted () {
      this.drawChart1();
      this.drawChart2();
      this.drawChart3();
      this.drawChart4();
    },
    methods: {
/*      getDivStyle() {
        let a = document.getElementById('div1');
        let b = document.body.clientWidth;
        a.style.height = b/2 + 'px';
        console.log(window.screen.height);
      },*/

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

      userinfoFilter(){
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/get-customer-info',
          data: {
            'customer_name': this.formFilter.select_customer
          }
        }).then(response => {
          if(response.data.status){
            //console.log(response.data.data)
            this.userData = response.data.data;
          }
        }).catch(error => {
          console.log(error);
        });
      },

      userCloudCountFilter(){
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/get-customer-cloud-count-total',
          data: {
            'customer_name': this.formFilter.select_customer,
            'date': this.valueDate
          }
        }).then(response => {
          if(response.data.status){
            this.cloudData = response.data.data;
            let csp_name = [];
            let tmp = [];
            let d = {};
            for(let i=0; i<response.data.data.length; i++) {
              csp_name.push(response.data.data[i].csp_name);
              //count.push(response.data.data[i].count);
              //service_name.push(response.data.data[i].service_name);
              d = {};
              d.name = response.data.data[i].csp_name;
              d.value = response.data.data[i].count;
              tmp.push(d);
            }
            //console.log(csp_name)
            this.drawChart5(csp_name, tmp)
            //this.drawChart1(hourList, aliyunList, tentcentCloudList);
          }
        }).catch(error => {
          //console.log(error);
        });
      },

      userTop5CloudTldFilter(){
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/get-customer-top-cloud-tld',
          data: {
            'customer_name': this.formFilter.select_customer,
            'date': this.valueDate,
            'n':5
          }
        }).then(response => {
          if(response.data.status){
            this.top5CloudDomain = response.data.data;
            //this.drawChart1(hourList, aliyunList, tentcentCloudList);
          }
        }).catch(error => {
          //console.log(error);
        });
      },

      userTop5NotCloudTldFilter(){
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/get-customer-top-not-cloud-tld',
          data: {
            'customer_name': this.formFilter.select_customer,
            'date': this.valueDate,
            'n':5
          }
        }).then(response => {
          if(response.data.status){
            this.top5NotCloudDomain = response.data.data;
            //this.drawChart1(hourList, aliyunList, tentcentCloudList);
          }
        }).catch(error => {
          //console.log(error);
        });
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
            //console.log(response.data.data['腾讯云'].slice(0,8).concat(response.data.data['腾讯云'].slice(18)));
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
            //this.cloudData = response.data.data;
            //console.log(response.data.data)
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
            this.drawChart2(service_name, tmp);
          }
        }).catch(error => {
          //console.log(error);
        });
      },

      DataFilter() {
        this.userinfoFilter();
        this.userCloudCountFilter();
        this.userCloudChartFilter();
        this.userTop5CloudTldFilter();
        this.userTop5NotCloudTldFilter();
        this.userCloudServiceNameChartFilter();
      },

      drawChart1() {
        var chart1 = document.getElementById('chart1');
        var chart = document.getElementById('chart_1');
        console.log(chart.clientHeight)
        var chart1Container = function () {
            chart1.style.width = (chart.clientWidth) +'px';
            chart1.style.height = (chart.clientHeight / 2- 20) +'px' ;
        };
        chart1Container();
        chart1 = this.$echarts.init(chart1, 'macarons');
        chart1.setOption({
          tooltip : {
            trigger: 'axis',
            axisPointer : {
              type : 'shadow'
            }
          },
          grid: {
            left: '3%',
            right: '3%',
            bottom: '15%',
            top:'3%',
            containLabel: true
          },
          xAxis: {
            type: 'category',
            data: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
            splitLine: {
              show: false
            }
          },
          yAxis: {
            type: 'value',
            splitLine: {
              show: false
            }
          },
          series: [{
            data: [820, 932, 901, 934, 1290, 1330, 1320],
            type: 'line',
            smooth: true
          }]
        });
      },

      drawChart2() {
        var convertData = function (data) {
          var res = [];
          for (var i = 0; i < data.length; i++) {
            var geoCoord = CITY_GEO_COORDS[data[i].name];
            if (geoCoord) {
              res.push({
                  name: data[i].name,
                  value: geoCoord.concat(data[i].value)
              });
            }
          }
          return res;
        };
        var dataGD =
          [{name: '潮州', value: 178},
          {name: '东莞', value: 10780},
          {name: '佛山', value: 5388},
          {name: '广州', value: 9636},
          {name: '惠州', value: 1771},
          {name: '江门', value: 1997},
          {name: '揭阳', value: 1241},
          {name: '梅州', value: 1091},
          {name: '汕头', value: 2292},
          {name: '深圳', value: 8951},
          {name: '云浮', value: 4374},
          {name: '湛江', value: 716},
          {name: '肇庆', value: 902},
          {name: '中山', value: 1375},
          {name: '珠海', value: 7225}];
        var chart2 = document.getElementById('chart2');
        var chart = document.getElementById('chart');
        var chart2Container = function () {
            chart2.style.width = (chart.clientWidth - 30) +'px';
            chart2.style.height = (chart.clientHeight - 80) +'px';
        };
        chart2Container();
        chart2 = this.$echarts.init(chart2, 'macarons');
        chart2.setOption({
          //backgroundColor: '#FFF',
            tooltip : {
              trigger: 'item'
            },
            geo: {
              map: '广东',
              zoom: 1.2,
              roam: true,
              label: {
                emphasis: {
                  show: false,
                  textStyle:{
                    color:'#FFF'
                  }
                }
              },
              center: [113.23, 22.8],
              itemStyle: {
                normal: {
                  areaColor: '#48B0D5',
                  borderColor: '#FFF'
                },
                emphasis: {
                  areaColor: '#48B0D5'
                }
              }
            },
            series : [
              {
                name: '数量',
                type: 'scatter',
                coordinateSystem: 'geo',
                data: convertData(dataGD),
                symbolSize: function (val) {
                    return val[2] / 700;
                },
                label: {
                    normal: {
                        formatter: '{b}',
                        position: 'right',
                        show: true
                    },
                    emphasis: {
                        formatter: '{b}',
                        position: 'left',
                        show: true
                    }
                },
                itemStyle: {
                  normal: {
                      color: '#E9CA10'
                  }
                }
              }
            ]
          });
      },
      drawChart3() {
        var chart3 = document.getElementById('chart3');
        var chart = document.getElementById('chart_3');
        var chart3Container = function () {
            chart3.style.width = (chart.clientWidth) +'px';
            chart3.style.height = (chart.clientHeight - 20) +'px';
        };
        chart3Container();
        chart3 = this.$echarts.init(chart3, 'macarons');
        chart3.setOption({
          tooltip : {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
          },
          toolbox: {
            show : true,
          },
          calculable : true,
          series : [
            {
              name:'面积模式',
              type:'pie',
              radius : [30, 40],
              center : ['50%', '45%'],
              roseType : 'area',
              data:[
                {value:10, name:'rose1'},
                {value:5, name:'rose2'},
                {value:15, name:'rose3'},
                {value:25, name:'rose4'},
                {value:20, name:'rose5'}
              ]
            }
          ]
        });
      },
      drawChart4() {
        var chart4 = document.getElementById('chart4');
        var chart = document.getElementById('chart_4');
        var chart4Container = function () {
            chart4.style.width = (chart.clientWidth) +'px';
            chart4.style.height = (chart.clientHeight - 20) +'px';
        };
        chart4Container();
        chart4 = this.$echarts.init(chart4, 'macarons');
        chart4.setOption({
          tooltip: {
            trigger: 'axis',
            axisPointer: {
              type: 'shadow'
            }
          },
          grid: {
            top:'1%',
            left: '3%',
            right: '7%',
            bottom: '6%',
            containLabel: true
          },
          xAxis: {
            type: 'value',
            boundaryGap: [0, 0.01],
            axisLabel: {
              show:false
            },
            splitLine: {
              show:false
            },
            splitArea : {show : false}
          },
          yAxis: {
            type: 'category',
            data: ['巴西','印尼','美国','印度','中国','巴西','印尼','美国','印度','中国'],
            splitLine: {
              show:false
            },
            splitArea : {show : false}
          },
          series: [
            {
              name: '2011年',
              type: 'bar',
              label: {
                normal: {
                  position: 'right',
                  show: true
                }
              },
              data: [18203, 23489, 29034, 104970, 131744,18203, 23489, 29034, 104970, 131744]
            }
          ]
        });
      },
      drawChart5(list1, list2) {
        //console.log(list2)
        var chart5 = document.getElementById('chart5');
        var chart = document.getElementById('chart');
        var chart5Container = function () {
            chart5.style.width = (chart.clientWidth - 50) +'px';
            chart5.style.height = '300px';
        };
        chart5Container();
        chart5 = this.$echarts.init(chart5, 'macarons');
        chart5.setOption({
          tooltip : {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
          },
          legend: {
            orient: 'horizontal',
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
    },
    created(){
      ////this.getDropDownList();
      //this.getDivStyle();
    },
    computed: {
    }
  }
</script>

<style lang="scss" scoped>
  ::-webkit-scrollbar
  {
    width: 0;
  }
  .bg {
    position: absolute;
    //background-image: url('../assets/background2.jpg');
    //background-repeat: no-repeat;
    //background-size: 100% 100%;
    background-color:#083A6B;
    height:100%;
    width:100%;
  }
/*   .handle-box{
    margin-top: 20px;
    text-align: center;
    margin-bottom: -20px;
  }
  .handle-select-input{
    width: 210px;
  }
  .handle-select-2{
    width: 100px;
  } */

/*   .handle-input{
    width: 300px;
  }

  .el-select-dropdown__item {
    text-align: center;
  }

  .el-input__inner {
    margin-right: 10px;
  } */
  .panel-group {
    margin-left: 10px;
    margin-right: 0px;
  }
  .panel-group-col {
    //border: 0.5px solid #3B98C2;
    //border:1em solid transparent;
    //-webkit-border-image:url('../assets/border.png') 10 round stretch;
  }
  .div-css {
    //border-image-source: url('../assets/border.png');
    //border-image-width: 4px;
    //background: url('../assets/border.png') no-repeat 0 0;
    //border: 0.5px solid #3B98C2;
    //height: 50%;
    margin: 10px 10px 0px 0px;
    //padding: 15px 15px;
    /* box-shadow: 4px 4px 40px rgba(0, 0, 0, 0.05); */
    overflow:hidden;
    //background-color: #0B4576;
    background-color: rgba(0,0,0,0.1);
    /* cursor: pointer; */
  }

  .border-top-left {
    position: absolute;
    width:10px;
    height:10px;
    border-width: 2px 0 0 2px;
    border-style: solid;
    border-color: #227BA6;
  }

  .border-top-right {
    position: absolute;
    width:10px;
    height:10px;
    right:10px;
    border-width: 2px 2px 0 0;
    border-style: solid;
    border-color: #227BA6;
  }

  .border-bottom-left {
    width:10px;
    height:10px;
    bottom:0;
    position:absolute;
    border-width: 0 0 2px 2px;
    border-style: solid;
    border-color: #227BA6;
  }

  .border-bottom-right {
    width:10px;
    height:10px;
    position: absolute;
    right:10px;
    bottom:0px;
    border-width: 0 2px 2px 0;
    border-style: solid;
    border-color: #227BA6;
  }
  .test{
    margin: 20px 10px 10px 0px;
    height:30px;
    text-align:center;
    background: url('../assets/behavior2.png') no-repeat 100% 100%;
    background-size: cover;
  }

/*   .div-css div:nth-child(1){
    background-color:#333;
    width:20px;
    height:20px;
    //position:absolute;
    left: 8.5px;
    top: 18.5px;
    //padding-top: -5px;
    //padding: 5px;
    border-style: solid;
    border-color: #227BA6;
    border-width: 3px 0 0 3px;
  }

  .div-css div:nth-child(2){
    background-color:#666;
    width:20px;
    height:20px;
    float:right;
    //position:absolute;
    margin-right: 8px;
    bottom: 0px;
    //padding-top: -5px;
    //padding: 5px;
    border-style: solid;
    border-color: #227BA6;
    border-width: 0 3px 3px 0;
  } */

/*   .div-css div:nth-child(3){
    width:20px;
    height:20px;
    position:absolute;
    margin-left: -1.5px;
    margin-top: -1.5px;
    //padding-top: -5px;
    //padding: 5px;
    border-style: solid;
    border-color: #227BA6;
    border-width: 3px 0 0 3px;
  }

  .div-css div:nth-child(4){
    width:20px;
    height:20px;
    position:absolute;
    margin-left: -1.5px;
    margin-top: -1.5px;
    //padding-top: -5px;
    //padding: 5px;
    border-style: solid;
    border-color: #227BA6;
    border-width: 3px 0 0 3px;
  } */

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
    padding-top:-20px;
    margin-left:10px;
    font-size:14px;
    line-height:30px;
    color:#51B6D8;
    font-weight: bold;
  }
</style>