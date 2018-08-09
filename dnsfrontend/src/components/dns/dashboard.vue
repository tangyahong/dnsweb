<template>
  <div class="dashboard">
    <div>
      <el-row class="panel-group">
        <el-col :xs="12" :sm="12" :lg="6" class="panel-group-col">
          <div class="div-css">
            <!-- <div><img src="../../assets/1.png" height="90px" class="pic" /></div> -->
            <div style="margin-top:15px;">
              <!-- <i class="el-icon-location-outline" style="color: #000; font-size:80px; float:left"></i> -->
              <icon name="device_1" scale="8" style="float:left"></icon>
              <span class="span-style"><strong>昨日-总解析量</strong></span>
              <!-- <hr class="hr-style"/> -->
              <span style="width:100%; text-align:center; line-height:25px; display:block;">
                <strong style="font-size:30px; color:#1C86EE">123456</strong>
                <strong style="font-size:20px; color:#32CD32">+1234</strong>
              </span>
            </div>
          </div>
        </el-col>
        <el-col :xs="12" :sm="12" :lg="6" class="panel-group-col">
          <div class="div-css">
            <!-- <div><img src="../../assets/1.png" height="90px" class="pic" /></div> -->
            <div style="margin-top:15px;">
              <!-- <i class="el-icon-location-outline" style="color: #000; font-size:80px; float:left"></i> -->
              <icon name="device" scale="8" style="float:left" ></icon>
              <span class="span-style"><strong>昨日-解析成功率</strong></span>
              <!-- <hr class="hr-style"/> -->
              <span style="width:100%; text-align:center; line-height:25px; display:block;">
                <strong style="font-size:25px; color:#1C86EE; margin-top：10px">{{deviceCollectCount}}</strong>
              </span>
            </div>
          </div>
        </el-col>
        <el-col :xs="12" :sm="12" :lg="6" class="panel-group-col">
          <div class="div-css">
            <!-- <div><img src="../../assets/1.png" height="90px" class="pic" /></div> -->
            <div style="margin-top:15px;">
              <!-- <i class="el-icon-location-outline" style="color: #000; font-size:80px; float:left"></i> -->
              <icon name="device_2" scale="8" style="float:left"></icon>
              <span class="span-style"><strong>本周解析量</strong></span>
              <!-- <hr class="hr-style"/> -->
              <span style="width:100%; text-align:center; line-height:25px; display:block;">
                <strong style="font-size:25px; color:#1C86EE; margin-top：10px">0</strong>
              </span>
            </div>
          </div>
        </el-col>
        <el-col :xs="12" :sm="12" :lg="6" class="panel-group-col">
          <div class="div-css">
            <!-- <div><img src="../../assets/1.png" height="90px" class="pic" /></div> -->
            <div style="margin-top:15px;">
              <!-- <i class="el-icon-location-outline" style="color: #000; font-size:80px; float:left"></i> -->
              <icon name="device_3" scale="8" style="float:left"></icon>
              <span class="span-style"><strong>IPV6解析量</strong></span>
              <!-- <hr class="hr-style"/> -->
              <span style="width:100%; text-align:center; line-height:25px; display:block;">
                <strong style="font-size:25px; color:#1C86EE; margin-top：10px">0</strong>
              </span>
            </div>
          </div>
        </el-col>
      </el-row>
<!--        <el-row class="panel-group">
        <el-col :xs="24" :sm="24" :lg="12" id="chart" class="panel-group-col">
          <div class="chart-css">
            <icon name="item" scale="2" style="padding-right: 5px; margin-left: -10px; float:left; margin-top:10px"></icon><span class="item-font">本周每日解析量</span>
            <div id="chart1" style="display:inline-block"></div>
          </div>
        </el-col>
        <el-col :xs="24" :sm="24" :lg="12" id="chart_2" class="panel-group-col" >
          <div class="chart-css-2">
            <icon name="item" scale="2" style="padding-right: 5px; margin-left: -10px; float:left; margin-top:10px"></icon><span class="item-font">本周每日解析成功率</span>
            <div id="chart2" style="display:inline-block"></div>
          </div>
        </el-col>
      </el-row> -->
    </div>
  </div>
</template>

<script>
  import { restful_path } from '../util.js'
  import _ from 'lodash'
  require('echarts/theme/shine')
	export default {
    data(){
      return {
        deviceTotal: '-',
        deviceCollectCount: '-',
        chart1: null,
        chart2: null
        //chart: document.getElementById('chart1'),
      }
    },
    methods: {
      getDeviceTotal() {
        this.$http({
          method: 'get',
          url: restful_path + '/api/audit/get-statistics/device-num',
        }).then(response => {
          if (response.data.status){
            this.deviceTotal = response.data.data;
          }
        }).catch(error => {
          //console.log(error);
        });
      },
      getDeviceCollectCount() {
        this.$http({
          method: 'post',
          url: restful_path + '/api/audit/get-statistics/collect-num',
          data: {
            'date':'20171205'
          }
        }).then(response => {
          if (response.data.status){
            this.deviceCollectCount = response.data.data;
          }
        }).catch(error => {
          //console.log(error);
        });
      },

      drawChart_pie() {
        //this.$store.commit('change');
        //console.log(this.$store.state.isCollapse)
        var chart1 = document.getElementById('chart1');
        var chart = document.getElementById('chart');
        var chart1Container = function () {
            chart1.style.width = (chart.clientWidth) +'px';
            chart1.style.height = (chart.clientHeight - 20) +'px';
        };
        chart1Container();
        this.chart1 = chart1;
        this.chart1 = this.$echarts.init(chart1, 'shine');
        this.chart1.setOption({
          tooltip : {
            trigger: 'item',
            formatter: "{a} <br/>{b} : {c} ({d}%)"
          },
          legend: {
            orient: 'vertical',
            left: 'left',
            data: ['华为','中兴','阿尔卡特','Redback','思科', 'Juniper']
          },
          toolbox: {
            show : true,
          },
          calculable : true,
          series : [
            {
              name:'设备量',
              type:'pie',
              radius : '70%',
              center: ['50%', '40%'],
              data:[
                {value:50, name:'华为'},
                {value:20, name:'中兴'},
                {value:15, name:'阿尔卡特'},
                {value:25, name:'Redback'},
                {value:20, name:'思科'},
                {value:20, name:'Juniper'}
              ]
            }
          ]
        });
      },

      drawChart_bar() {
        var chart2 = document.getElementById('chart2');
        var chart_2 = document.getElementById('chart_2');
        var chart2Container = function () {
            chart2.style.width = (chart_2.clientWidth) +'px';
            chart2.style.height = (chart_2.clientHeight - 20) +'px';
        };
        chart2Container();
        this.chart2 = chart2;
        this.chart2 = this.$echarts.init(chart2, 'shine');
        this.chart2.setOption({
          tooltip : {
            trigger: 'axis',
            axisPointer : {
              type : 'shadow'
            }
          },
          grid: {
            top:'20',
            left: '0',
            right: '50',
            bottom: '20%',
            containLabel: true
          },
          xAxis: {
            type: 'category',
            data: ['广州','深圳','佛山','东莞','惠州','江门','揭阳','梅州','汕头','潮州',
              '湛江','肇庆','中山','珠海','汕尾','阳江','肇庆','河源','韶关','茂名','清远'],
            axisLabel:{
              interval:0,
              rotate:-60
            }
          },
          yAxis: {
            type: 'value'
          },
          series: [{
            data: [120, 200, 150, 80, 70, 110, 130,120, 200, 150,
              80, 70, 110, 130,120, 200, 150, 80, 70, 110, 130],
            type: 'bar'
          }]
        });
      }
    },
    created() {
      //this.showInfo()
      this.getDeviceTotal()
      this.getDeviceCollectCount()
    },
    mounted() {
      this.drawChart_pie();
      this.drawChart_bar();
      window.addEventListener('resize', _.throttle(() => {
        this.drawChart_bar();
        this.drawChart_pie();
        this.chart1.resize();
        this.chart2.resize();
      }, 500))
    },
    computed: {
      getIsCollapse() {
        return this.$store.state.isCollapse;
      }
    },
    watch: {
      getIsCollapse() {
        setTimeout(() => {
          this.drawChart_pie();
          this.drawChart_bar();
          this.chart1.resize();
          this.chart2.resize();
        }, 300);
        console.log(this.chart1)
        //this.drawChart_bar();
        //this.drawChart_pie();
        //this.chart1.resize()
        //this.chart2.resize()
      }
    }
  }
</script>

<style lang="scss" scoped>
  ::-webkit-scrollbar-track {
    background: #F0F2F5
  }
  .dashboard {
    background-color: #F0F2F5;
    height: calc(100% + 40px);
    margin: -20px;
    overflow: auto;
  }
  .panel-group {
    margin-left: 10px;
    margin-right: 0px;
  }
  .div-css {
    //border:1px solid #F7F7F7;
    height: 100px;
    margin: 10px 10px 0px 0px;
    padding: 0 20px;
    //box-shadow: 4px 4px 40px rgba(0, 0, 0, 0.05);
    overflow:hidden;
    background-color: #FFF;
    /* cursor: pointer; */
  }
  .chart-css {
    //border:1px solid #F7F7F7;
    height: 300px;
    margin: 10px 10px 0px 0px;
    padding: 0 20px;
    //box-shadow: 4px 4px 40px rgba(0, 0, 0, 0.05);
    overflow:hidden;
    background-color: #FFF;
    /* cursor: pointer; */
  }
  .chart-css-2 {
    //border:1px solid #F7F7F7;
    height: 300px;
    margin: 10px 10px 10px 0px;
    padding: 0 20px;
    //box-shadow: 4px 4px 40px rgba(0, 0, 0, 0.05);
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
</style>