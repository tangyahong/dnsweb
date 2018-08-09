<template>
  <div class="bg">
      <el-row class="panel-group">
        <el-col :xs="24" :sm="24" :lg="24" class="panel-group-col">
          <el-row>
            <el-col :xs="24" :sm="24" :lg="24" class="panel-group-col">
              <div class="test">
                <span style="text-align:center; font-size:30px; color:#43CAF2; line-height:60px;">DNS展板</span>
              </div>
              <div>
                <el-button-group style="float:right; margin-top: -50px; margin-right:10px">
                  <span style="text-align:center; font-size:25px; color:#43CAF2; float:left; padding-right:20px; line-height:35px;">2018年5月19日</span>
                  <el-button >日</el-button>
                  <el-button >周</el-button>
                  <el-button >月</el-button>
                </el-button-group>
              </div>
            </el-col>
          </el-row>
        </el-col>
        <el-col :xs="24" :sm="24" :lg="5" class="panel-group-col">
          <el-row>
            <div class="div-css" :style="{height:heightData + 'px'}">
<!--               <div>
                <div class="border-top-left"></div>
                <div class="border-top-right"></div>
              </div> -->
              <span class="item-font">访问量TOP10域名</span>
              <div id="chart3" style="display:inline-block;"></div>
<!--               <div>
                <div class="border-bottom-left"></div>
                <div class="border-bottom-right"></div>
              </div> -->
            </div>
              <div class="div-css" :style="{height:heightData + 'px'}">
<!--                 <div>
                  <div class="border-top-left"></div>
                  <div class="border-top-right"></div>
                </div> -->
                <span class="item-font">访问量TOP10网站</span>
                <div id="chart3" style="display:inline-block"></div>
                <div>
<!--                   <div class="border-bottom-left"></div>
                  <div class="border-bottom-right"></div> -->
                </div>
              </div>
              <div class="div-css" :style="{height:heightData + 'px'}">
<!--                 <div>
                  <div class="border-top-left"></div>
                  <div class="border-top-right"></div>
                </div> -->
                <span class="item-font">访问量TOP10类别</span>
                <div id="chart2" style="display:inline-block"></div>
                <div>
<!--                   <div class="border-bottom-left"></div>
                  <div class="border-bottom-right"></div> -->
                </div>
              </div>
          </el-row>
        </el-col>

        <el-col :xs="8" :sm="8" :lg="14" class="panel-group-col" id="chart">
          <el-row>
            <el-col :xs="24" :sm="24" :lg="24" class="panel-group-col">
              <div class="div-css" :style="{height:heightData - 170 + 'px'}" id="chart_1">
<!--                 <div>
                  <div class="border-top-left"></div>
                  <div class="border-top-right"></div>
                </div> -->
                <div style="text-align:center"><span class="item-font" style="font-size:20px">访问总量</span></div>
                <div style="text-align:center"><span class="item-font" style="font-size:60px; color:#FFF" :style="{lineHeight:heightData - 200 + 'px'}">113,302,330,000</span></div>
<!--                 <div>
                  <div class="border-bottom-left"></div>
                  <div class="border-bottom-right"></div>
                </div> -->
              </div>
            </el-col>
            <el-col :xs="24" :sm="24" :lg="24" class="panel-group-col">
              <div class="div-css" :style="{height:heightData + 220 + 'px'}" id="chart_map">
                <div class="chart-css">
                  <div id="dt1" style="display:inline-block; float:left"></div>
                  <div>
                    <!-- <span class="item-font">各地市访问量</span> -->
                    <div id="zzt1" style="display:inline-block; margin-top:50px"></div>
                  </div>
                </div>
              </div>
            </el-col>
            <el-col :xs="24" :sm="24" :lg="24" class="panel-group-col">
              <el-row>
                <el-col :xs="24" :sm="24" :lg="12" class="panel-group-col">
                  <el-row>
                    <el-col :xs="24" :sm="24" :lg="24" class="panel-group-col" id="chart_qst">
                      <div class="div-css" :style="{height:heightData - 50 + 'px'}">
<!--                         <div>
                          <div class="border-top-left"></div>
                          <div class="border-top-right"></div>
                        </div> -->
                        <span class="item-font">总体趋势</span>
                        <div id="chart7" style="display:inline-block"></div>
<!--                         <div>
                          <div class="border-bottom-left"></div>
                          <div class="border-bottom-right"></div>
                        </div> -->
                      </div>
                    </el-col>
                  </el-row>
                </el-col>

                <el-col :xs="24" :sm="24" :lg="12" class="panel-group-col">
                  <el-row>
                    <el-col :xs="24" :sm="24" :lg="24" class="panel-group-col">
                      <div class="div-css" :style="{height:heightData - 50 + 'px'}">
<!--                         <div>
                          <div class="border-top-left"></div>
                          <div class="border-top-right"></div>
                        </div> -->
                        <span class="item-font">移动用户趋势</span>
                        <div class="chart-css">
                          <div id="qst1" style="display:inline-block;"></div>
                        </div>
<!--                         <div>
                          <div class="border-bottom-left"></div>
                          <div class="border-bottom-right"></div>
                        </div> -->
                      </div>
                    </el-col>
                  </el-row>
                </el-col>
              </el-row>
            </el-col>
          </el-row>
        </el-col>
        <el-col :xs="8" :sm="8" :lg="5" class="panel-group-col">
          <el-row>
            <el-col :xs="24" :sm="24" :lg="24" class="panel-group-col" id="chart_bzt">
              <div class="div-css" :style="{height:heightData + 'px'}">
<!--                 <div>
                  <div class="border-top-left"></div>
                  <div class="border-top-right"></div>
                </div> -->
                <span class="item-font">公有云访问占比</span>
                <div class="chart-css">
                  <div id="bzt1" style="display:inline-block;"></div>
                </div>
<!--                 <div>
                  <div class="border-bottom-left"></div>
                  <div class="border-bottom-right"></div>
                </div> -->
              </div>
            </el-col>
            <el-col :xs="24" :sm="24" :lg="24" class="panel-group-col">
              <div class="div-css" :style="{height:heightData + 'px'}">
<!--                 <div>
                  <div class="border-top-left"></div>
                  <div class="border-top-right"></div>
                </div> -->
                <span class="item-font">用户类型访问量占比</span>
<!--                 <div>
                  <div class="border-bottom-left"></div>
                  <div class="border-bottom-right"></div>
                </div> -->
              </div>
            </el-col>
            <el-col :xs="24" :sm="24" :lg="24" class="panel-group-col">
              <div class="div-css" :style="{height:heightData + 'px'}">
<!--                 <div>
                  <div class="border-top-left"></div>
                  <div class="border-top-right"></div>
                </div> -->
                <span class="item-font">重点关注域名</span>
<!--                 <div>
                  <div class="border-bottom-left"></div>
                  <div class="border-bottom-right"></div>
                </div> -->
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
        bzt1: null,
        qst1: null,
        dt1: null,
        zzt1: null,
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
        heightData: window.screen.availHeight / 3 - 80
      }
    },
    filters: {
    },
    mounted () {
    },
    methods: {
      draw_bzt1() {
        this.$http({
          method: 'get',
          url: restful_path + '/api/dns/get-platform-index-detail-weekly',
        }).then(response => {
          if (response.data.status){
            setTimeout(() => {
              var chart = document.getElementById('bzt1');
              var chart1 = document.getElementById('chart_bzt');
              var chartContainer = function () {
                chart.style.width = (chart1.clientWidth -10) +'px';
                chart.style.height = (chart1.clientHeight - 50) +'px';
              };
              chartContainer();
              this.bzt1 = chart;
              this.bzt1 = this.$echarts.init(bzt1);
              this.bzt1.setOption({
                color:['#468EE5', '#6AE7FF','#FFD300','#BCBDBC', '#FF6A6A'],
                tooltip : {
                  trigger: 'item',
                  formatter: "{a} <br/>{b} : {c} ({d}%)"
                },
                series : [
                  {
                    name: '访问量',
                    type: 'pie',
                    radius : '80%',
                    center: ['50%', '50%'],
                    data: response.data.data['value'],
                    itemStyle: {
                      emphasis: {
                          shadowBlur: 10,
                          shadowOffsetX: 0,
                          shadowColor: 'rgba(0, 0, 0, 0.5)'
                      }
                    }
                  }
                ]
              })
            },100)
          }
        }).catch(error => {});
      },
      draw_qst1() {
        this.$http({
          method: 'get',
          url: restful_path + '/api/dns/get-enterprise-index',
        }).then(response => {
          if (response.data.status){
            this.enterpriseIndex = response.data.data['resolved_number'][response.data.data['date'].length -1]
            setTimeout(() => {
              var qst1 = document.getElementById('qst1');
              var chart_qst = document.getElementById('chart_qst');
              var chartContainer = function () {
                  qst1.style.width = (chart_qst.clientWidth - 10) +'px';
                  qst1.style.height = (chart_qst.clientHeight - 40) +'px';
              };
              chartContainer();
              this.qst1 = qst1;
              this.qst1 = this.$echarts.init(qst1);
              this.qst1.setOption({
                //color: ['#3398DB'],
                color: ['#1790CF'],
                tooltip : {
                  trigger: 'axis',
                  axisPointer : {
                    type : 'line',
                    lineStyle: {color: '#1790CF'}
                  }
                },
                grid: {
                  top:'10',
                  left: '10',
                  right: '20',
                  bottom: '0',
                  containLabel: true
                },
                 xAxis: {
                  //show: false,
                  type: 'category',
                  boundaryGap: false,
                  axisLine:{
                    lineStyle:{
                      color: '#1790CF',
                      //width:0
                    }
                  },
                  axisTick: {
                    show: false
                  },
                  axisLabel : {//坐标轴刻度标签的相关设置。
                    formatter : function(params){
                      var newParamsName = "";// 最终拼接成的字符串
                      var paramsNameNumber = params.length;// 实际标签的个数

                      if (paramsNameNumber == 8) {
                        newParamsName = params.substr(4);
                      } else {
                        newParamsName = params;
                      }
                      return newParamsName
                    }
                  },
/*                   axisLabel : {
                    formatter: function(){
                       return "";
                    }
                  }, */
                  splitLine:{
                  　show:false
                  },
                  data: response.data.data['date']
                },
                yAxis: {
                  //show: false,
                  type: 'value',
                  splitLine:{
                  　show:false
                  },
/*                   axisLine:{
                    lineStyle:{
                      color: '#FFF',
                      width:2
                    }
                  }, */
                  axisTick: {
                    show: false
                  },
                  axisLine : {
                    type : 'line',
                    lineStyle: {color: '#1790CF'}
                  }
/*                   axisLabel : {
                    formatter: function(){
                       return "";
                    }
                  } */
                },
                series: [{
                  data: response.data.data['resolved_number'],
                  type: 'line',
                  smooth: true,
                  itemStyle : { 
                    normal: {
                      areaStyle: {
                      //areaStyle: { color: '#1790CF'}
                      color: new this.$echarts.graphic.LinearGradient(
                        0, 0, 0, 1,
                        [
                          {offset: 0, color: '#1790CF'},
                          {offset: 1, color: '#000'}
                        ]
                      )}
                    }
                  },
                  symbol: 'none',
                }]
              })
            },100)
          }
        })
      },
      draw_dt1() {
        this.$http({
          method: 'get',
          url: restful_path + '/api/dns/get-development-index-weekly',
        }).then(response => {
          var value_list = []
          if (response.data.status){
            var data = response.data.data;
            var l = response.data.data['subscriber_city'].length;
            for (var i = 0; i <l; i ++){
              value_list.push({name : data['subscriber_city'][i] + '市', value: data['resolved_number'][i]})
            }
            var max = Math.max.apply(null, data['resolved_number'])
          }
          setTimeout(() => {
            var dt1 = document.getElementById('dt1');
            var chart2 = document.getElementById('chart_map');
            var chartContainer = function () {
                dt1.style.width = (chart2.clientWidth /3 *2) +'px';
                dt1.style.height = (chart2.clientHeight) +'px';
            };
            chartContainer();
            this.dt1 = dt1;
            this.dt1 = this.$echarts.init(dt1, 'shine');
            this.dt1.setOption({
              tooltip: {
                trigger: 'item'
              },
              visualMap: {
                show: false,
                min: 0,
                max: max,
                left: 'right',
                top: 'bottom',
                calculable: true,
                itemWidth:15,
                itemHeight:120,
              },
              grid: {
                top:'0',
                left: '50',
                right: '0',
                bottom: '0',
                //containLabel: true
              },
              series: [
                {
                  name: '访问量',
                  type: 'map',
                  mapType: '广东',
                  roam: false,
                  zoom: 1.2,
                  smooth: true,
                  itemStyle: {
                    normal: {
                      borderColor: '#FFF'
                    },
                    emphasis: {
                      areaColor: '#F8F197'
                    }
                  },
                  label: {
                    normal: {
                        show: true,
                        fontSize: 11
                    },
                    emphasis: {
                        show: true
                    }
                  },
                  data: value_list
                }
              ]
            })
          },100)
        })
      },
      draw_zzt1() {
        this.$http({
          method: 'get',
          url: restful_path + '/api/dns/get-development-index-weekly',
        }).then(response => {
          var value_list = []
          if (response.data.status){
            var data = response.data.data;
            var l = response.data.data['subscriber_city'].length;
            for (var i = 0; i <l; i ++){
              value_list.push({name : data['subscriber_city'][i] + '市', value: data['resolved_number'][i]})
            }
            var max = Math.max.apply(null, data['resolved_number'])
          }
          setTimeout(() => {
            var zzt1 = document.getElementById('zzt1');
            var chart2 = document.getElementById('chart_map');
            var chartContainer = function () {
                zzt1.style.width = (chart2.clientWidth /3) +'px';
                zzt1.style.height = (chart2.clientHeight - 80) +'px';
            };
            chartContainer();
            this.zzt1 = zzt1;
            this.zzt1 = this.$echarts.init(zzt1, 'shine');
            this.zzt1.setOption({
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
                bottom: '0%',
                containLabel: true
              },
              xAxis: {
                type: 'value',
                show: false,
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
                axisTick: {
                  show: false
                },
                axisLine:{
                  lineStyle:{
                    color:'#fff',
                    width:0,   //这里是坐标轴的宽度,可以去掉
                  }
                },
                type: 'category',
                data: ['深圳','广州','江门','中山','潮州','珠海','东莞','肇庆','惠州','梅州','佛山','揭阳','河源','汕头','韶关','汕尾','清远','湛江','茂名','云浮','阳江'],
                splitLine: {
                  show:false
                },
                splitArea : {show : false}
              },
              series: [
                {
                  name: '20180318',
                  type: 'bar',
                  label: {
                    normal: {
                      position: 'right',
                      show: false
                    }
                  },
                  itemStyle: {
                    //柱形图圆角，鼠标移上去效果，如果只是一个数字则说明四个参数全部设置为那么多
                    emphasis: {
                      barBorderRadius: 30
                    },
                    normal: {
                      //柱形图圆角，初始化效果
                      barBorderRadius: 30,
                      color: '#1790CF',
                    }
                  },
                  data: [54752013,64721824,109551264,129689625,143216610,151172777,156990245,235846618,265062255,523848693,743683726,809756549,1014558193,1324145341,1480068913,1508062992,1639509586,1973073966,2322635761,5393260599,12238123455]
                }
              ]
            })
          },100)
        })
      }
    },
    created(){
      this.draw_bzt1();
      this.draw_qst1();
      this.draw_dt1();
      this.draw_zzt1();
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
    background-color:#050B21;
    height:100%;
    //width: 1536px;
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
    background-color: rgba(0,0,0,0.5);
    //background: url('../assets/border-small.png') no-repeat 0 0;
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
    position:absolute;
    width:10px;
    height:10px;
    bottom:0;
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
    height: 60px;
    text-align:center;
    background: url('../assets/bgtitle.png') no-repeat center;
    //background-size: 50%;
  }

  .chart-css {
    //border:1px solid #F7F7F7;
    //height: 300px;
    //margin: 10px 10px 0px 0px;
    //padding: 0 20px;
    //box-shadow: 4px 4px 40px rgba(0, 0, 0, 0.05);
    //overflow:hidden;
    margin-left: 0px;
    //background-color: #FFF;
    /* cursor: pointer; */
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
    font-size:15px;
    line-height:30px;
    color:#51B6D8;
    font-weight: bold;
  }
</style>
<style lang="scss">
  .bg {
    .el-dialog__body {
      background-color: #1F2F3B;
      border-radius: 9px;
    }
    .el-dialog__header {
      background-color: #1F2F3B;
      border-radius: 9px;
    }
    .el-dialog__title {
      color: #FFF;
    }
    .el-input__inner {
      background-color: #1F2F3B;
      color: #6AE9FF;
      border: 1px solid #6AE9FF;
    }
    .el-dialog {
      border: 1.5px solid #3C566A;
      border-radius: 10px;
      background-color: #1F2F3B;
    }
    .el-button-group{ 
      .el-button:not(:last-child) {
        color: #227BA6;
        font-size: 16px;
        font-weight: bold;
        border: 1.5px solid #227BA6;
        background-color: #050B21;
      }
      .el-button:last-child {
        color: #227BA6;
        font-size: 16px;
        font-weight: bold;
        border: 1.5px solid #227BA6;
        background-color: #050B21;
      }
    }
    .el-table {
      border: 0px;
    }
    .el-table__empty-block {
      background-color: #050B21;
    }
    .el-table td, .el-table th.is-leaf {
      border: 0px;
      background-color: #050B21;
    }
    .el-table td, .el-table th {
      padding: 6px 0;
    }
    .el-button {
      padding: 9px 15px;
    }
  }
</style>