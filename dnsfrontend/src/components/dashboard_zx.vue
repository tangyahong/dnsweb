<template>
  <div class="detail">
    <div class="dashboard">
      <el-row class="panel-group">
        <el-col :xs="24" :sm="24" :lg="24">
          <div class="title-css">
            <span style="line-height: 15vh; font-size: 25px; color: #FFF"><strong>智联广东指数-工业互联网大数据看板</strong></span>
          </div>
        </el-col>
      </el-row>
      <el-row class="panel-group">
        <el-col :xs="12" :sm="12" :lg="4" id="chart">
          <div class="div-css" @click="showDetailQYZS()" style="cursor:pointer">
            <div style="margin-top:5px;">
              <div style="float: left">
                <span class="span-style-left">企业指数</span>
              </div>
              <div>
                <span class="span-style-right"><strong>{{ enterpriseIndex }}</strong></span>
              </div>
            </div>
            <div class="chart-css">
              <div id="chart_qyzs" style="display:inline-block;"></div>
            </div>
          </div>
        </el-col>
        <el-col :xs="12" :sm="12" :lg="4">
          <div class="div-css" @click="showDetailPTZS()" style="cursor:pointer">
            <div style="margin-top:5px;">
              <div style="float: left">
                <span class="span-style-left">平台指数</span>
              </div>
              <div>
                <span class="span-style-right"><strong>{{ platformIndex }}</strong></span>
              </div>
            </div>
            <div class="chart-css">
              <div id="chart_ptzs" style="display:inline-block;"></div>
            </div>
          </div>
        </el-col>
        <el-col :xs="12" :sm="12" :lg="4">
          <div class="div-css" @click="showDetailSFJDZS()" style="cursor:pointer">
            <div style="margin-top:5px;">
              <div style="float: left">
                <span class="span-style-left">示范基地指数</span>
              </div>
              <div>
                <span class="span-style-right"><strong>{{ demonstrationBasesIndex }}</strong></span>
              </div>
            </div>
            <div class="chart-css">
              <div id="chart_sfjdzs" style="display:inline-block;"></div>
            </div>
          </div>
        </el-col>
        <el-col :xs="12" :sm="12" :lg="4">
          <div class="div-css"  @click="showDetailYYFWZS()" style="cursor:pointer">
            <div style="margin-top:5px;">
              <div style="float: left">
                <span class="span-style-left">应用服务指数</span>
              </div>
              <div>
                <span class="span-style-right"><strong>{{ applicationServiceIndex }}</strong></span>
              </div>
            </div>
            <div class="chart-css">
              <div id="chart_yyfwzs" style="display:inline-block;"></div>
            </div>
          </div>
        </el-col>
        <el-col :xs="12" :sm="12" :lg="4">
          <div class="div-css" @click="showDetailJRFWZS()" style="cursor:pointer">
            <div style="margin-top:5px;">
              <div style="float: left">
                <span class="span-style-left">金融服务指数</span>
              </div>
              <div>
                <span class="span-style-right"><strong>{{ financialServiceIndex }}</strong></span>
              </div>
            </div>
            <div class="chart-css">
              <div id="chart_jrfwzs" style="display:inline-block;"></div>
            </div>
          </div>
        </el-col>
      </el-row>
      <el-row class="panel-group">
        <el-col :xs="24" :sm="24" :lg="24">
          <div class="div-css" style="height: calc(60vh - 50px)">
            <div style="margin-top:5px;">
              <div>
                <span class="span-style-left">全省发展指数</span>
                <el-row>
                  <el-col :xs="12" :sm="12" :lg="9" id="chart_qsfzzs">
                    <div class="div-css-2" style="height: calc(50vh - 70px);" >
                      <div style="height: calc(50vh - 70px); margin-top:20px" >
                        <div id="chart2" style="display:inline-block;"></div>
                      </div>
                    </div>
                  </el-col>
                  <el-col :lg="6">
                    <div style="text-align: center; margin-top:15vh">
                      <span style="font-size:7vh; color: #6AE9FF;"><strong>{{ developmentIndex }}</strong></span>
                    </div>
                    <div style="text-align: center; margin-top: 2vh">
                      <span style="font-size:20px; color: #FFF;">连接数</span>
                    </div>
                  </el-col>
                  <el-col :xs="12" :sm="12" :lg="9" id="chart_map">
                    <div style="height: calc(69vh - 40px); margin-top:-30px">
                      <div id="chart7" style="display:inline-block;"></div>
                    </div>
                  </el-col>
                </el-row>
              </div>
            </div>
          </div>
        </el-col>
      </el-row>
    </div>

    <!-- 点击“企业指数”展开 -->
    <!-- 左边是用户每周公有云访问量排名， 右边是选择一天查看具体排名 -->
    <el-dialog title="企业指数详情" :visible.sync="detailQYZSChartsVisible" style="text-align:center; width:180%; margin-left:-40%; margin-top:-5vh">
      <div>
        <div id="chartDetail" style="height:62vh;">
          <div style="display:inline-block; float:right; margin-right:20px; z-index: 1; position: relative">
            <el-date-picker
              v-model="datePick_qyzs"
              type="date"
              size="mini"
              value-format="yyyyMMdd"
              placeholder="选择日期">
            </el-date-picker>
            <el-button size="mini" class="button-css" style="margin-left: 5px; " @click="detailQYZSquery()">确定</el-button>
          </div>
          <div id="chart_qyzs_left"  style="top:5px; float:left"></div>
          <div id="chart_qyzs_right"  style="top:-25px; float:left"></div>
        </div>
      </div>
    </el-dialog>

    <!-- 点击“平台指数”展开 -->
    <!-- 左边是每周公有云访问量排名， 右边是选择一天查看具体排名 -->
    <el-dialog title="平台指数详情" :visible.sync="detailPTZSChartsVisible" style="text-align:center; width:180%; margin-left:-40%; margin-top:-5vh">
      <div>
        <div id="chartDetail2" style="height:62vh;">
          <div style="display:inline-block; float:right; margin-right:20px; z-index: 1; position: relative">
            <el-date-picker
              v-model="datePick_ptzs"
              type="date"
              size="mini"
              value-format="yyyyMMdd"
              placeholder="选择日期">
            </el-date-picker>
            <el-button size="mini" class="button-css" style="margin-left: 5px;" @click="detailPTZSquery()">确定</el-button>
          </div>
          <div id="chart_ptzs_left"  style="top:5px; float:left"></div>
          <div id="chart_ptzs_right"  style="top:-25px; float:left"></div>
        </div>
      </div>
    </el-dialog>

    <!-- 点击“平台指数”展开 -->
    <!-- 左边是每周公有云访问量排名， 右边是选择一天查看具体排名 -->
    <el-dialog title="示范基地指数详情" :visible.sync="detailSFJDZSChartsVisible" style="text-align:center; width:180%; margin-left:-40%; margin-top:-5vh">
      <div>
        <div id="chartDetail3" style="height:62vh;">
          <div style="display:inline-block; float:right; margin-right:20px; z-index: 1; position: relative">
            <el-date-picker
              v-model="datePick_sfjdzs"
              type="date"
              size="mini"
              value-format="yyyyMMdd"
              placeholder="选择日期">
            </el-date-picker>
            <el-button size="mini"  class="button-css" style="margin-left:5px;" @click="detailSFJDZSquery()">确定</el-button>
          </div>
          <div id="chart_sfjdzs_left"  style="top:5px; float:left"></div>
          <div id="chart_sfjdzs_right"  style="top:-25px; float:left"></div>
        </div>
      </div>
    </el-dialog>

    <el-dialog title="应用服务指数详情" :visible.sync="detailYYFWZSChartsVisible" style="text-align:center; width:180%; margin-left:-40%; margin-top:-5vh">
      <div>
        <div id="chartDetail4" style="height:62vh;">
          <div style="display:inline-block; float:right; margin-right:20px; z-index: 1; position: relative">
            <el-date-picker
              v-model="datePick_yyfwzs"
              type="date"
              size="mini"
              value-format="yyyyMMdd"
              placeholder="选择日期">
            </el-date-picker>
            <el-button size="mini"  class="button-css" style="margin-left:5px;" @click="detailYYFWZSquery()">确定</el-button>
          </div>
          <div id="chart_yyfwzs_left"  style="top:5px; float:left"></div>
          <div id="chart_yyfwzs_right"  style="top:-25px; float:left"></div>
        </div>
      </div>
    </el-dialog>

    <el-dialog title="金融服务指数详情" :visible.sync="detailJRFWZSChartsVisible" style="text-align:center; width:180%; margin-left:-40%; margin-top:-5vh">
      <div>
        <div id="chartDetail5" style="height:62vh;">
          <div style="display:inline-block; float:right; margin-right:20px; z-index: 1; position: relative">
            <el-date-picker
              v-model="datePick_jrfwzs"
              type="date"
              size="mini"
              value-format="yyyyMMdd"
              placeholder="选择日期">
            </el-date-picker>
            <el-button  class="button-css" size="mini" style="margin-left: 5px;" @click="detailJRFWZSquery()">确定</el-button>
          </div>
          <div id="chart_jrfwzs_left"  style="top:5px; float:left"></div>
          <div id="chart_jrfwzs_right"  style="top:-25px; float:left"></div>
        </div>
      </div>
    </el-dialog>

  </div>
</template>

<script>
  import { restful_path } from './util.js'
  import _ from 'lodash'
  import 'echarts/map/js/province/guangdong';
  import 'echarts/map/js/china';
  import { CITY_GEO_COORDS } from './geo.js'
  require('echarts/theme/shine')
  export default {
    data(){
      return {
        detailQYZSChartsVisible: false,
        detailPTZSChartsVisible: false,
        detailSFJDZSChartsVisible: false,
        detailYYFWZSChartsVisible: false,
        detailJRFWZSChartsVisible: false,
        chart1: null,
        chart2: null,
        chart3: null,
        chart4: null,
        chart5: null,
        chart6: null,
        chart7: null,
        chart_qyzs: null,
        chart_qyzs_left: null,
        chart_qyzs_right: null,
        chart_ptzs: null,
        chart_ptzs_left: null,
        chart_ptzs_right: null,
        chart_sfjdzs: null,
        chart_sfjdzs_left: null,
        chart_sfjdzs_right: null,
        chart_yyfwzs: null,
        chart_yyfwzs_left: null,
        chart_yyfwzs_right: null,
        chart_jrfwzs: null,
        chart_jrfwzs_left: null,
        chart_jrfwzs_right: null,
        datePick_qyzs: '20180318',
        datePick_ptzs: '20180318',
        datePick_sfjdzs: '20180318',
        datePick_yyfwzs: '20180318',
        datePick_jrfwzs: '20180318',
        date_qyzs: '',
        date_ptzs: '',
        date_sfjdzs: '',
        date_yyfwzs: '',
        date_jrwfzs: '',
        enterpriseIndex: '',
        platformIndex: '',
        demonstrationBasesIndex: '',
        applicationServiceIndex: '',
        financialServiceIndex: '',
        developmentIndex: ''
        //chart: document.getElementById('chart1'),
      }
    },
    methods: {
      showDetailQYZS() {
        this.detailQYZSChartsVisible = true;
        this.drawChartDetail_qyzs_left();
        this.drawChartDetail_qyzs_right();
      },
      showDetailPTZS() {
        this.detailPTZSChartsVisible = true;
        this.drawChartDetail_ptzs_left();
        this.drawChartDetail_ptzs_right();
      },
      showDetailSFJDZS() {
        this.detailSFJDZSChartsVisible = true;
        this.drawChartDetail_sfjdzs_left();
        this.drawChartDetail_sfjdzs_right();
      },
      showDetailYYFWZS() {
        this.detailYYFWZSChartsVisible = true;
        this.drawChartDetail_yyfwzs_left();
        this.drawChartDetail_yyfwzs_right();
      },
      showDetailJRFWZS() {
        this.detailJRFWZSChartsVisible = true;
        this.drawChartDetail_jrfwzs_left();
        this.drawChartDetail_jrfwzs_right();
      },
      detailQYZSquery() {
        this.drawChartDetail_qyzs_right();
      },
      detailPTZSquery() {
        this.drawChartDetail_ptzs_right();
      },
      detailSFJDZSquery() {
        this.drawChartDetail_sfjdzs_right();
      },
      detailYYFWZSquery() {
        this.drawChartDetail_yyfwzs_right();
      },
      detailJRFWZSquery() {
        this.drawChartDetail_jrfwzs_right();
      },
      drawChartDetail_qyzs_left() {
        this.date_qyzs = this.datePick_qyzs;
        this.$http({
          method: 'get',
          url: restful_path + '/api/dns/get-enterprise-index-detail-weekly',
        }).then(response => {
          if (response.data.status){
            setTimeout(() => {
              var chart_qyzs_left = document.getElementById('chart_qyzs_left');
              var chartDetail = document.getElementById('chartDetail');
              var chartContainer = function () {
                chart_qyzs_left.style.width = (chartDetail.clientWidth) /2 +'px';
                chart_qyzs_left.style.height = (chartDetail.clientHeight) +'px';
              };
              chartContainer();
              this.chart_qyzs_left = chart_qyzs_left;
              this.chart_qyzs_left = this.$echarts.init(chart_qyzs_left, 'shine');
              this.chart_qyzs_left.setOption({
                color: ['#68E7FE'],
                title : {
                  //text: '过去一周公有云访问排名-' + this.date_qyzs,
                  text: '一周公有云访问排名-' + response.data.data['year'] + '年第' + response.data.data['week'] + '周',
                  textStyle: {
                    fontSize: 14,
                    fontWeight: 'bold',
                    color: '#FFF'
                  }
                },
                tooltip : {
                  trigger: 'axis',
                  axisPointer : {            // 坐标轴指示器，坐标轴触发有效
                    type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                  }
                },
                grid: {
                  top:'40',
                  left: '6',
                  right: '20',
                  bottom: '15',
                  containLabel: true
                },
                xAxis : [
                  {
                    type : 'category',
                    axisLine: {
                      lineStyle: {
                        color: '#FFF'
                      }
                    },
                    data : response.data.data['subscriber_name'],
                    axisTick: {
                      alignWithLabel: true
                    },
                    splitLine:{
                　　  show:false
                　　},
                    axisLabel : {//坐标轴刻度标签的相关设置。
                      formatter : function(params){
                        var newParamsName = "";// 最终拼接成的字符串
                          var paramsNameNumber = params.length;// 实际标签的个数
                          var provideNumber = 3;// 每行能显示的字的个数
                          var rowNumber = Math.ceil(paramsNameNumber / provideNumber);// 换行的话，需要显示几行，向上取整
                          if (paramsNameNumber > provideNumber) {
                            /** 循环每一行,p表示行 */
                            for (var p = 0; p < rowNumber; p++) {
                              var tempStr = "";// 表示每一次截取的字符串
                              var start = p * provideNumber;// 开始截取的位置
                              var end = start + provideNumber;// 结束截取的位置
                              if (p == rowNumber - 1) {
                                tempStr = params.substring(start, paramsNameNumber);
                              } else {
                                tempStr = params.substring(start, end) + "\n";
                              }
                              newParamsName += tempStr;// 最终拼成的字符串
                            }
                          } else {
                            newParamsName = params;
                          }
                          return newParamsName
                      }
                    }
                  }
                ],
                yAxis : [
                  {
                    type : 'value',
                    splitLine:{
                　　  show:false
                　　},
                    axisLine: {
                      lineStyle: {
                        color: '#FFF'
                      }
                    },
                  }
                ],
                series : [
                  {
                    name:'访问量',
                    type:'bar',
                    barWidth: '60%',
                    data: response.data.data['resolved_number'],
                    itemStyle : { normal: {label : {show: true, position: 'top'}}},
                  }
                ]
              })
            },100)
          }
        }).catch(error => {});
      },
      drawChartDetail_qyzs_right() {
        //this.date_qyzs = '20180228'
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/get-enterprise-index-detail-daily',
          data: {
           'date': this.datePick_qyzs
          }
        }).then(response => {
          if (response.data.status){
            setTimeout(() => {
              var chart_qyzs_right = document.getElementById('chart_qyzs_right');
              var chartDetail = document.getElementById('chartDetail');
              var chartContainer = function () {
                chart_qyzs_right.style.width = (chartDetail.clientWidth) /2 +'px';
                chart_qyzs_right.style.height = (chartDetail.clientHeight) +'px';
              };
              chartContainer();
              this.chart_qyzs_right = chart_qyzs_right;
              this.chart_qyzs_right = this.$echarts.init(chart_qyzs_right, 'shine');
              this.chart_qyzs_right.setOption({
                color: ['#68E7FE'],
                title : {
                  text:  '公有云访问排名-' + this.datePick_qyzs,
                  textStyle: {
                    fontSize: 14,
                    fontWeight: 'bold',
                    color: '#FFF'
                  }
                },
                tooltip : {
                  trigger: 'axis',
                  axisPointer : {            // 坐标轴指示器，坐标轴触发有效
                    type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                  }
                },
                grid: {
                  top:'38',
                  left: '6',
                  right: '20',
                  bottom: '15',
                  containLabel: true
                },
                xAxis : [
                  {
                    type : 'category',
                    data : response.data.data['subscriber_name'],
                    axisTick: {
                      alignWithLabel: true
                    },
                    splitLine:{
                　　  show:false
                　　},
                    axisLine: {
                      lineStyle: {
                        color: '#FFF'
                      }
                    },
                    axisLabel : {//坐标轴刻度标签的相关设置。
                      formatter : function(params){
                        var newParamsName = "";// 最终拼接成的字符串
                          var paramsNameNumber = params.length;// 实际标签的个数
                          var provideNumber = 3;// 每行能显示的字的个数
                          var rowNumber = Math.ceil(paramsNameNumber / provideNumber);// 换行的话，需要显示几行，向上取整
                          if (paramsNameNumber > provideNumber) {
                            /** 循环每一行,p表示行 */
                            for (var p = 0; p < rowNumber; p++) {
                              var tempStr = "";// 表示每一次截取的字符串
                              var start = p * provideNumber;// 开始截取的位置
                              var end = start + provideNumber;// 结束截取的位置
                              if (p == rowNumber - 1) {
                                tempStr = params.substring(start, paramsNameNumber);
                              } else {
                                tempStr = params.substring(start, end) + "\n";
                              }
                              newParamsName += tempStr;// 最终拼成的字符串
                            }
                          } else {
                            newParamsName = params;
                          }
                          return newParamsName
                      }
                    }
                  }
                ],
                yAxis : [
                  {
                    type : 'value',
                    axisLine: {
                      lineStyle: {
                        color: '#FFF'
                      }
                    },
                    splitLine:{
                　　  show:false
                　　}
                  }
                ],
                series : [
                  {
                    name:'访问量',
                    type:'bar',
                    barWidth: '60%',
                    data: response.data.data['resolved_number'],
                    itemStyle : { normal: {label : {show: true, position: 'top'}}},
                  }
                ]
              })
            },100)
          }
        }).catch(error => {});
      },
      drawChartDetail_ptzs_left() {
        //this.date_ptzs = this.datePick_ptzs;
        this.$http({
          method: 'get',
          url: restful_path + '/api/dns/get-platform-index-detail-weekly',
        }).then(response => {
          if (response.data.status){
            setTimeout(() => {
              var chart_ptzs_left = document.getElementById('chart_ptzs_left');
              var chartDetail = document.getElementById('chartDetail2');
              var chartContainer = function () {
                chart_ptzs_left.style.width = (chartDetail.clientWidth / 2) +'px';
                chart_ptzs_left.style.height = (chartDetail.clientHeight) +'px';
              };
              chartContainer();
              this.chart_ptzs_left = chart_ptzs_left;
              this.chart_ptzs_left = this.$echarts.init(chart_ptzs_left);
              this.chart_ptzs_left.setOption({
                //color:['#468EE5','#6AE7FF', '#FFFFFF'],
                color:['#468EE5', '#6AE7FF','#FFD300','#BCBDBC', '#FF6A6A'],
                title : {
                  text: '过去一周公有云访问量-' + response.data.data['year'] + '年第' + response.data.data['week'] + '周',
                  textStyle: {
                    fontSize: 14,
                    fontWeight: 'bold',
                    color: '#FFF'
                  }
                },
                tooltip : {
                  trigger: 'item',
                  formatter: "{a} <br/>{b} : {c} ({d}%)"
                },
                legend: {
                  orient: 'vertical',
                  left: 'right',
                  data: response.data.data['name'],
                  padding: 40,
                  textStyle:{    //图例文字的样式
                    color:'#FFF'
                  }
                },
                series : [
                  {
                    name: '访问量',
                    type: 'pie',
                    radius : '80%',
                    center: ['45%', '55%'],
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
      drawChartDetail_ptzs_right() {
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/get-platform-index-detail-daily',
          data: {
           'date': this.datePick_ptzs
          }
        }).then(response => {
          if (response.data.status){
            setTimeout(() => {
              var chart_ptzs_right = document.getElementById('chart_ptzs_right');
              var chartDetail = document.getElementById('chartDetail2');
              var chartContainer = function () {
                chart_ptzs_right.style.width = (chartDetail.clientWidth / 2) +'px';
                chart_ptzs_right.style.height = (chartDetail.clientHeight) +'px';
              };
              chartContainer();
              this.chart_ptzs_right = chart_ptzs_right;
              this.chart_ptzs_right = this.$echarts.init(chart_ptzs_right, 'shine');
              this.chart_ptzs_right.setOption({
                color:['#468EE5', '#6AE7FF','#FFD300','#BCBDBC', '#FF6A6A'],
                title : {
                  text: '当日公有云访问量-' + this.datePick_ptzs,
                  textStyle: {
                    fontSize: 14,
                    fontWeight: 'bold',
                    color: '#FFF'
                  }
                },
                tooltip : {
                  trigger: 'item',
                  formatter: "{a} <br/>{b} : {c} ({d}%)"
                },
                legend: {
                  orient: 'vertical',
                  left: 'right',
                  data: response.data.data['name'],
                  padding: [40, 20],
                  textStyle:{    //图例文字的样式
                    color:'#FFF'
                  }
                },
                series : [
                  {
                    name: '访问量',
                    type: 'pie',
                    radius : '80%',
                    center: ['45%', '55%'],
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
      drawChartDetail_sfjdzs_left() {
        //this.date_sfjdzs = this.datePick_sfjdzs;
        this.$http({
          method: 'get',
          url: restful_path + '/api/dns/get-demonstration-bases-index-detail-weekly',
        }).then(response => {
          if (response.data.status){
            setTimeout(() => {
              var chart_sfjdzs_left = document.getElementById('chart_sfjdzs_left');
              var chartDetail = document.getElementById('chartDetail3');
              var chartContainer = function () {
                chart_sfjdzs_left.style.width = (chartDetail.clientWidth / 2) +'px';
                chart_sfjdzs_left.style.height = (chartDetail.clientHeight) +'px';
              };
              chartContainer();
              this.chart_sfjdzs_left = chart_sfjdzs_left;
              this.chart_sfjdzs_left = this.$echarts.init(chart_sfjdzs_left, 'shine');
              this.chart_sfjdzs_left.setOption({
                color:['#468EE5', '#6AE7FF','#FFD300','#BCBDBC', '#FF6A6A'],
                //color:['#1B61B7', '#F5C827','#F5C827','#13B2B6', '#8372CE'],
                title : {
                  text: '过去一周示范基地公有云访问量-' + response.data.data['year'] + '年第' + response.data.data['week'] + '周',
                  textStyle: {
                    fontSize: 14,
                    fontWeight: 'bold',
                    color: '#FFF'
                  }
                },
                tooltip : {
                  trigger: 'item',
                  formatter: "{a} <br/>{b} : {c} ({d}%)"
                },
                legend: {
                  orient: 'vertical',
                  left: 'right',
                  data: response.data.data['name'],
                  padding: 40,
                  textStyle:{    //图例文字的样式
                    color:'#FFF'
                  },
                  show: false
                },
                series : [
                  {
                    name: '访问量',
                    type: 'pie',
                    radius : '70%',
                    center: ['45%', '55%'],
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
      drawChartDetail_sfjdzs_right() {
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/get-demonstration-bases-index-detail-daily',
          data: {
           'date': this.datePick_sfjdzs
          }
        }).then(response => {
          if (response.data.status){
            setTimeout(() => {
              var chart_sfjdzs_right = document.getElementById('chart_sfjdzs_right');
              var chartDetail = document.getElementById('chartDetail3');
              var chartContainer = function () {
                chart_sfjdzs_right.style.width = (chartDetail.clientWidth / 2) +'px';
                chart_sfjdzs_right.style.height = (chartDetail.clientHeight) +'px';
              };
              chartContainer();
              this.chart_sfjdzs_right = chart_sfjdzs_right;
              this.chart_sfjdzs_right = this.$echarts.init(chart_sfjdzs_right, 'shine');
              this.chart_sfjdzs_right.setOption({
                color:['#468EE5', '#6AE7FF','#FFD300','#BCBDBC', '#FF6A6A'],
                //color:['#1B61B7', '#F5C827','#F5C827','#13B2B6', '#8372CE'],
                title : {
                  text: '当日示范基地公有云访问量-' + this.datePick_sfjdzs,
                  textStyle: {
                    fontSize: 14,
                    fontWeight: 'bold',
                    color: '#FFF'
                  }
                },
                tooltip : {
                  trigger: 'item',
                  formatter: "{a} <br/>{b} : {c} ({d}%)"
                },
                legend: {
                  orient: 'vertical',
                  left: 'right',
                  data: response.data.data['name'],
                  itemGap: 10,
                  padding: [40, 20],
                  textStyle:{    //图例文字的样式
                    color:'#FFF'
                  },
                  show: false
                },
                series : [
                  {
                    name: '访问量',
                    type: 'pie',
                    radius : '70%',
                    center: ['45%', '55%'],
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
      drawChartDetail_yyfwzs_left() {
        this.date_yywfzs = this.datePick_yyfwzs;
        this.$http({
          method: 'get',
          url: restful_path + '/api/dns/get-application-service-index-detail-weekly',
        }).then(response => {
          if (response.data.status){
            setTimeout(() => {
              var name_list = response.data.data['name']
              var value_list = response.data.data['value']
              var chart_yyfwzs_left = document.getElementById('chart_yyfwzs_left');
              var chartDetail = document.getElementById('chartDetail4');
              var chartContainer = function () {
                chart_yyfwzs_left.style.width = (chartDetail.clientWidth / 2) +'px';
                chart_yyfwzs_left.style.height = (chartDetail.clientHeight) +'px';
              };
              chartContainer();
              this.chart_yyfwzs_left = chart_yyfwzs_left;
              this.chart_yyfwzs_left = this.$echarts.init(chart_yyfwzs_left, 'shine');
              this.chart_yyfwzs_left.setOption({
                color:['#468EE5', '#6AE7FF','#FFD300','#BCBDBC', '#FF6A6A'],
                //color:['#1B61B7', '#F5C827','#F5C827','#13B2B6', '#8372CE'],
                title : {
                  text: '过去一周应用服务访问量-' + response.data.data['year'] + '年第' + response.data.data['week'] + '周',
                  textStyle: {
                    fontSize: 14,
                    fontWeight: 'bold',
                    color: '#FFF'
                  }
                },
                tooltip : {
                  trigger: 'item',
                  formatter: "{a} <br/>{b} : {c} ({d}%)"
                },
                legend: {
                  orient: 'vertical',
                  left: 'right',
                  data: name_list,
                  padding: 40,
                  textStyle:{    //图例文字的样式
                    color:'#FFF'
                  }
                },
                series : [
                  {
                    name: '访问量',
                    type: 'pie',
                    radius : '70%',
                    center: ['45%', '55%'],
                    data: value_list,
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
      drawChartDetail_yyfwzs_right() {
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/get-application-service-index-detail-daily',
          data: {
           'date': this.datePick_yyfwzs
          }
        }).then(response => {
          if (response.data.status){
            setTimeout(() => {
              var name_list = response.data.data['name']
              var value_list = response.data.data['value']
              var chart_yyfwzs_right = document.getElementById('chart_yyfwzs_right');
              var chartDetail = document.getElementById('chartDetail4');
              var chartContainer = function () {
                chart_yyfwzs_right.style.width = (chartDetail.clientWidth / 2) +'px';
                chart_yyfwzs_right.style.height = (chartDetail.clientHeight) +'px';
              };
              chartContainer();
              this.chart_yyfwzs_right = chart_yyfwzs_right;
              this.chart_yyfwzs_right = this.$echarts.init(chart_yyfwzs_right, 'shine');
              this.chart_yyfwzs_right.setOption({
                color:['#468EE5', '#6AE7FF','#FFD300','#BCBDBC', '#FF6A6A'],
                //color:['#1B61B7', '#F5C827','#F5C827','#13B2B6', '#8372CE'],
                title : {
                  text: '当日应用服务访问量-' + this.datePick_yyfwzs,
                  textStyle: {
                    fontSize: 14,
                    fontWeight: 'bold',
                    color: '#FFF'
                  }
                },
                tooltip : {
                  trigger: 'item',
                  formatter: "{a} <br/>{b} : {c} ({d}%)"
                },
                legend: {
                  orient: 'vertical',
                  left: 'right',
                  data: name_list,
                  padding: [40, 20],
                  textStyle:{    //图例文字的样式
                    color:'#FFF'
                  },
                },
                series : [
                  {
                    name: '访问量',
                    type: 'pie',
                    radius : '70%',
                    center: ['45%', '55%'],
                    data: value_list,
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
      drawChartDetail_jrfwzs_left() {
        this.date_jrwfzs = this.datePick_jrfwzs;
        this.$http({
          method: 'get',
          url: restful_path + '/api/dns/get-financial-service-index-detail-weekly',
        }).then(response => {
          if (response.data.status){
            var name_list = response.data.data['name']
            var value_list = response.data.data['value']
            setTimeout(() => {
              var chart_jrfwzs_left = document.getElementById('chart_jrfwzs_left');
              var chartDetail = document.getElementById('chartDetail5');
              var chartContainer = function () {
                chart_jrfwzs_left.style.width = (chartDetail.clientWidth / 2) +'px';
                chart_jrfwzs_left.style.height = (chartDetail.clientHeight) +'px';
              };
              chartContainer();
              this.chart_jrfwzs_left = chart_jrfwzs_left;
              this.chart_jrfwzs_left = this.$echarts.init(chart_jrfwzs_left, 'shine');
              this.chart_jrfwzs_left.setOption({
                color:['#468EE5', '#6AE7FF','#FFD300','#BCBDBC', '#FF6A6A'],
                //color:['#1B61B7', '#F5C827','#F5C827','#13B2B6', '#8372CE'],
                title : {
                  text: '过去一周金融服务访问量-' + response.data.data['year'] + '年第' + response.data.data['week'] + '周',
                  textStyle: {
                    fontSize: 14,
                    fontWeight: 'bold',
                    color: '#FFF'
                  }
                },
                tooltip : {
                  trigger: 'item',
                  formatter: "{a} <br/>{b} : {c} ({d}%)"
                },
                legend: {
                  orient: 'vertical',
                  left: 'right',
                  data: name_list,
                  padding: 40,
                  textStyle:{    //图例文字的样式
                    color:'#FFF'
                  }
                },
                series : [
                  {
                    name: '访问量',
                    type: 'pie',
                    radius : '80%',
                    center: ['45%', '55%'],
                    data: value_list,
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
      drawChartDetail_jrfwzs_right() {
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/get-financial-service-index-detail-daily',
          data: {
           'date': this.datePick_jrfwzs
          }
        }).then(response => {
          if (response.data.status){
            var name_list = response.data.data['name']
            var value_list = response.data.data['value']
            setTimeout(() => {
              var chart_jrfwzs_right = document.getElementById('chart_jrfwzs_right');
              var chartDetail = document.getElementById('chartDetail5');
              var chartContainer = function () {
                chart_jrfwzs_right.style.width = (chartDetail.clientWidth / 2) +'px';
                chart_jrfwzs_right.style.height = (chartDetail.clientHeight) +'px';
              };
              chartContainer();
              this.chart_jrfwzs_right = chart_jrfwzs_right;
              this.chart_jrfwzs_right = this.$echarts.init(chart_jrfwzs_right, 'shine');
              this.chart_jrfwzs_right.setOption({
                color:['#468EE5', '#6AE7FF','#FFD300','#BCBDBC', '#FF6A6A'],
                //color:['#1B61B7', '#F5C827','#F5C827','#13B2B6', '#8372CE'],
                title : {
                  text: '当日金融服务访问量-' + this.datePick_jrfwzs,
                  textStyle: {
                    fontSize: 14,
                    fontWeight: 'bold',
                    color: '#FFF'
                  }
                },
                tooltip : {
                  trigger: 'item',
                  formatter: "{a} <br/>{b} : {c} ({d}%)"
                },
                legend: {
                  orient: 'vertical',
                  left: 'right',
                  data: name_list,
                  padding: [40, 20],
                  textStyle:{    //图例文字的样式
                    color:'#FFF'
                  }
                },
                series : [
                  {
                    name: '访问量',
                    type: 'pie',
                    radius : '80%',
                    center: ['45%', '55%'],
                    data: value_list,
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
      drawChart_qyzs() {
        this.$http({
          method: 'get',
          url: restful_path + '/api/dns/get-enterprise-index',
        }).then(response => {
          if (response.data.status){
            this.enterpriseIndex = response.data.data['resolved_number'][response.data.data['date'].length -1]
            setTimeout(() => {
              var chart_qyzs = document.getElementById('chart_qyzs');
              var chart = document.getElementById('chart');
              var chartContainer = function () {
                  chart_qyzs.style.width = (chart.clientWidth - 50) +'px';
                  chart_qyzs.style.height = (chart.clientHeight - 60) +'px';
              };
              chartContainer();
              this.chart_qyzs = chart_qyzs;
              this.chart_qyzs = this.$echarts.init(chart_qyzs, 'shine');
              this.chart_qyzs.setOption({
                //color: ['#3398DB'],
                color: ['#FFF'],
                tooltip : {
                  trigger: 'axis',
                  axisPointer : {
                    type : 'shadow'
                  }
                },
                grid: {
                  top:'10',
                  left: '-7',
                  right: '0',
                  bottom: '0',
                  containLabel: true
                },
                 xAxis: {
                  //show: false,
                  type: 'category',
                  boundaryGap: false,
                  axisLine:{
                    lineStyle:{
                      color: '#FFF',
                      width:2
                    }
                  },
                  axisTick: {
                    show: false
                  },
                  axisLabel : {
                    formatter: function(){
                       return "";
                    }
                  },
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
                  axisLine:{
                    lineStyle:{
                      color: '#FFF',
                      width:2
                    }
                  },
                  axisTick: {
                    show: false
                  },
                  axisLabel : {
                    formatter: function(){
                       return "";
                    }
                  }
                },
                series: [{
                  data: response.data.data['resolved_number'],
                  type: 'line',
                  //symbol: 'none',
                  itemStyle: {
                    normal: {
                      color: "#FFF",
                      lineStyle: {
                          color: "#FFF"
                      }
                    }
                  },
                  //areaStyle: {},
                }]
              })
            },100)
          }
        })
      },
      drawChart_ptzs() {
        this.$http({
          method: 'get',
          url: restful_path + '/api/dns/get-platform-index',
        }).then(response => {
          if (response.data.status){
            this.platformIndex = response.data.data['resolved_number'][response.data.data['date'].length -1]
            setTimeout(() => {
              var chart_ptzs = document.getElementById('chart_ptzs');
              var chart = document.getElementById('chart');
              var chartContainer = function () {
                  chart_ptzs.style.width = (chart.clientWidth - 50) +'px';
                  chart_ptzs.style.height = (chart.clientHeight - 60) +'px';
              };
              chartContainer();
              this.chart_ptzs = chart_ptzs;
              this.chart_ptzs = this.$echarts.init(chart_ptzs, 'shine');
              this.chart_ptzs.setOption({
                color: ['#FFF'],
                tooltip : {
                  trigger: 'axis',
                  axisPointer : {
                    type : 'shadow'
                  }
                },
                grid: {
                  top:'10',
                  left: '-7',
                  right: '0',
                  bottom: '0',
                  containLabel: true
                },
                 xAxis: {
                  //show: false,
                  type: 'category',
                  boundaryGap: false,
                  axisLine:{
                    lineStyle:{
                      color: '#FFF',
                      width:2
                    }
                  },
                  axisTick: {
                    show: false
                  },
                  axisLabel : {
                    formatter: function(){
                       return "";
                    }
                  },
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
                  axisLine:{
                    lineStyle:{
                      color: '#FFF',
                      width:2
                    }
                  },
                  axisTick: {
                    show: false
                  },
                  axisLabel : {
                    formatter: function(){
                       return "";
                    }
                  }
                },
                series: [{
                  data: response.data.data['resolved_number'],
                  type: 'line',
                  //symbol: 'none',
                  itemStyle: {
                    normal: {
                      color: "#FFF",
                      lineStyle: {
                          color: "#FFF"
                      }
                    }
                  },
                  //areaStyle: {},
                }]
              })
            },100)
          }
        })
      },
      drawChart_sfjdzs() {
        this.$http({
          method: 'get',
          url: restful_path + '/api/dns/get-demonstration-bases-index',
        }).then(response => {
          if (response.data.status){
            this.demonstrationBasesIndex = response.data.data['resolved_number'][response.data.data['date'].length -1]
            setTimeout(() => {
              var chart_sfjdzs = document.getElementById('chart_sfjdzs');
              var chart = document.getElementById('chart');
              var chartContainer = function () {
                  chart_sfjdzs.style.width = (chart.clientWidth - 50) +'px';
                  chart_sfjdzs.style.height = (chart.clientHeight - 60) +'px';
              };
              chartContainer();
              this.chart_sfjdzs = chart_sfjdzs;
              this.chart_sfjdzs = this.$echarts.init(chart_sfjdzs, 'shine');
              this.chart_sfjdzs.setOption({
                color: ['#FFF'],
                tooltip : {
                  trigger: 'axis',
                  axisPointer : {
                    type : 'shadow'
                  }
                },
                grid: {
                  top:'10',
                  left: '-7',
                  right: '0',
                  bottom: '0',
                  containLabel: true
                },
                 xAxis: {
                  //show: false,
                  type: 'category',
                  boundaryGap: false,
                  axisLine:{
                    lineStyle:{
                      color: '#FFF',
                      width:2
                    }
                  },
                  axisTick: {
                    show: false
                  },
                  axisLabel : {
                    formatter: function(){
                       return "";
                    }
                  },
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
                  axisLine:{
                    lineStyle:{
                      color: '#FFF',
                      width:2
                    }
                  },
                  axisTick: {
                    show: false
                  },
                  axisLabel : {
                    formatter: function(){
                       return "";
                    }
                  }
                },
                series: [{
                  data: response.data.data['resolved_number'],
                  type: 'line',
                  //symbol: 'none',
                  itemStyle: {
                    normal: {
                      color: "#FFF",
                      lineStyle: {
                          color: "#FFF"
                      }
                    }
                  },
                  //areaStyle: {},
                }]
              })
            },100)
          }
        })
      },
      drawChart_yyfwzs() {
        this.$http({
          method: 'get',
          url: restful_path + '/api/dns/get-application-service-index',
        }).then(response => {
          if (response.data.status){
            this.applicationServiceIndex = response.data.data['resolved_number'][response.data.data['date'].length -1]
            setTimeout(() => {
              var chart_yyfwzs = document.getElementById('chart_yyfwzs');
              var chart = document.getElementById('chart');
              var chartContainer = function () {
                  chart_yyfwzs.style.width = (chart.clientWidth - 50) +'px';
                  chart_yyfwzs.style.height = (chart.clientHeight - 60) +'px';
              };
              chartContainer();
              this.chart_yyfwzs = chart_yyfwzs;
              this.chart_yyfwzs = this.$echarts.init(chart_yyfwzs, 'shine');
              this.chart_yyfwzs.setOption({
                color: ['#FFF'],
                tooltip : {
                  trigger: 'axis',
                  axisPointer : {
                    type : 'shadow'
                  }
                },
                grid: {
                  top:'10',
                  left: '-7',
                  right: '0',
                  bottom: '0',
                  containLabel: true
                },
                 xAxis: {
                  //show: false,
                  type: 'category',
                  boundaryGap: false,
                  axisLine:{
                    lineStyle:{
                      color: '#FFF',
                      width:2
                    }
                  },
                  axisTick: {
                    show: false
                  },
                  axisLabel : {
                    formatter: function(){
                       return "";
                    }
                  },
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
                  axisLine:{
                    lineStyle:{
                      color: '#FFF',
                      width:2
                    }
                  },
                  axisTick: {
                    show: false
                  },
                  axisLabel : {
                    formatter: function(){
                       return "";
                    }
                  }
                },
                series: [{
                  data: response.data.data['resolved_number'],
                  type: 'line',
                  //symbol: 'none',
                  itemStyle: {
                    normal: {
                      color: "#FFF",
                      lineStyle: {
                          color: "#FFF"
                      }
                    }
                  },
                  //areaStyle: {},
                }]
              })
            },100)
          }
        })
      },
      drawChart_jrfwzs() {
        this.$http({
          method: 'get',
          url: restful_path + '/api/dns/get-financial-service-index',
        }).then(response => {
          if (response.data.status){
            this.financialServiceIndex = response.data.data['resolved_number'][response.data.data['date'].length -1]
            setTimeout(() => {
              var chart_jrfwzs = document.getElementById('chart_jrfwzs');
              var chart = document.getElementById('chart');
              var chartContainer = function () {
                  chart_jrfwzs.style.width = (chart.clientWidth - 50) +'px';
                  chart_jrfwzs.style.height = (chart.clientHeight - 60) +'px';
              };
              chartContainer();
              this.chart_jrfwzs = chart_jrfwzs;
              this.chart_jrfwzs = this.$echarts.init(chart_jrfwzs, 'shine');
              this.chart_jrfwzs.setOption({
                color: ['#FFF'],
                tooltip : {
                  trigger: 'axis',
                  axisPointer : {
                    type : 'shadow'
                  }
                },
                grid: {
                  top:'10',
                  left: '-7',
                  right: '0',
                  bottom: '0',
                  containLabel: true
                },
                 xAxis: {
                  //show: false,
                  type: 'category',
                  boundaryGap: false,
                  axisLine:{
                    lineStyle:{
                      color: '#FFF',
                      width:2
                    }
                  },
                  axisTick: {
                    show: false
                  },
                  axisLabel : {
                    formatter: function(){
                       return "";
                    }
                  },
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
                  axisLine:{
                    lineStyle:{
                      color: '#FFF',
                      width:2
                    }
                  },
                  axisTick: {
                    show: false
                  },
                  axisLabel : {
                    formatter: function(){
                       return "";
                    }
                  }
                },
                series: [{
                  data: response.data.data['resolved_number'],
                  type: 'line',
                  //symbol: 'none',
                  itemStyle: {
                    normal: {
                      color: "#FFF",
                      lineStyle: {
                          color: "#FFF"
                      }
                    }
                  },
                  //areaStyle: {},
                }]
              })
            },100)
          }
        })
      },
      drawChart_qsfzzs() {
        this.$http({
          method: 'get',
          url: restful_path + '/api/dns/get-development-index',
        }).then(response => {
          if (response.data.status){
            this.developmentIndex = response.data.data['resolved_number'][response.data.data['date'].length -1]
            setTimeout(() => {
              var chart2 = document.getElementById('chart2');
              var chart_2 = document.getElementById('chart_qsfzzs');
              var chart2Container = function () {
                  chart2.style.width = (chart_2.clientWidth - 80) +'px';
                  chart2.style.height = (chart_2.clientHeight - 80) +'px';
              };
              chart2Container();
              this.chart2 = chart2;
              this.chart2 = this.$echarts.init(chart2, 'shine');
              this.chart2.setOption({
                color: ['#FFF'],
                tooltip : {
                  trigger: 'axis',
                  axisPointer : {
                    type : 'shadow'
                  }
                },
                grid: {
                  top:'10',
                  left: '-7',
                  right: '0',
                  bottom: '0',
                  containLabel: true
                },
                 xAxis: {
                  //show: false,
                  type: 'category',
                  boundaryGap: false,
                  axisLine:{
                    lineStyle:{
                      color: '#FFF',
                      width:2
                    }
                  },
                  axisTick: {
                    show: false
                  },
                  axisLabel : {
                    formatter: function(){
                       return "";
                    }
                  },
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
                  axisLine:{
                    lineStyle:{
                      color: '#FFF',
                      width:2
                    }
                  },
                  axisTick: {
                    show: false
                  },
                  axisLabel : {
                    formatter: function(){
                       return "";
                    }
                  }
                },
                series: [{
                  data: response.data.data['resolved_number'],
                  type: 'line',
                  //symbol: 'none',
                  itemStyle: {
                    normal: {
                      color: "#FFF",
                      lineStyle: {
                          color: "#FFF"
                      }
                    }
                  },
                  //areaStyle: {},
                }]
              })
            },100)
          }
        })
      },
      drawChart_map() {
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
            var chart7 = document.getElementById('chart7');
            var chart2 = document.getElementById('chart_map');
            var chartContainer = function () {
                chart7.style.width = (chart2.clientWidth) +'px';
                chart7.style.height = (chart2.clientHeight - 70) +'px';
            };
            chartContainer();
            this.chart7 = chart7;
            this.chart7 = this.$echarts.init(chart7, 'shine');
            this.chart7.setOption({
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
    },
    mounted() {
      this.drawChart_qyzs();
      this.drawChart_ptzs();
      this.drawChart_sfjdzs();
      this.drawChart_yyfwzs();
      this.drawChart_jrfwzs();
      this.drawChart_qsfzzs();
      this.drawChart_map();
      //this.drawChart_ptzs()
    }
  }
</script>

<style scoped>
  @media (min-width: 1200px){
    .el-col-lg-4 {
        width: 20%;
    }
  }
  ::-webkit-scrollbar-track {
    background: #1F2F3C
  }
  .dashboard {
    background-color: #1F2F3C;
    width: 100%;
    height: 100vh;
  }
  .panel-group {
    margin-left: 10px;
    margin-right: 0px;
  }
  .title-css {
    height: 15vh;
    text-align:center;
    background-color: #1F2F3C;
    background: url('../assets/bgtitle.png') no-repeat center
  }
  .div-css {
    border:1px solid #3F5C71;
    border-radius: 8px;
    height: 25vh;
    margin: 10px 10px 0px 0px;
    padding: 0 20px;
    //box-shadow: 4px 4px 40px rgba(0, 0, 0, 0.05);
    overflow:hidden;
    background-color: #1F2F3C ;
    /* cursor: pointer; */
  }
  .div-css-2 {
    border:1px solid #3F5C71;
    border-radius: 8px;
    height: 25vh;
    /* //margin: 10px 10px 0px 0px; */
    margin: 20px 20px;
    padding: 0 20px;
    overflow:hidden;
    background-color: #1F2F3C ;
    /* cursor: pointer; */
  }
  .chart-css {
/*     //border:1px solid #F7F7F7;
    //height: 300px;
    //margin: 10px 10px 0px 0px;
    //padding: 0 20px;
    //box-shadow: 4px 4px 40px rgba(0, 0, 0, 0.05);
    //overflow:hidden; */
    margin-left: 0px;
    /* //background-color: #FFF; */
    /* cursor: pointer; */
  }
  .chart-css-2 {
    /* //border:1px solid #F7F7F7; */
    height: 60vh;
/*     //margin: 10px 10px 10px 0px;
    //padding: 0 20px;
    //box-shadow: 4px 4px 40px rgba(0, 0, 0, 0.05);
    //overflow:hidden; */
    margin-left: 0px;
    background-color: #FFF;
    /* cursor: pointer; */
  }
  .span-style-left {
    width:100%;
    text-align:left;
    line-height:40px;
    display:block;
    color:#FFF;
  }
  .span-style-right {
    width:100%;
    text-align:right;
    line-height:40px;
    font-size: 20px;
    display:block;
    color:#6AE9FF;
  }
  .pic {
    float: left;
    margin: 15px 15px 15px 15px;
  }
  .hr-style {
    border: 0;
    height: 1px;
    background-image: linear-gradient(to right, rgba(0, 0, 0, 0), rgba(0, 0, 0, 0.75), rgba(0, 0, 0, 0));
    //margin-right: 15px;
  }
  .item-font {
    //font-family: SimHei;
    font-size:15px; 
    line-height:37px; 
    color:#2F3848;
    font-weight: bold;
  }
  .el-dialog__body {
    padding: 20px 20px;
    background-color: #1F2F3B;
  }
  .el-dialog__header {
    background-color: #1F2F3B;
  }
  .el-input__inner {
    background-color: #1F2F3B
  }
  .button-css {
    background-color:#47667E;
    border:1px solid #47667E;
    color:#FFF;
  }
</style>
<style lang="scss">
  .detail{
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
  }
</style>