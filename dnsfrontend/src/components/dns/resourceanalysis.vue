<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right" style="font-size: 14px">
      <el-breadcrumb-item :to="{ path: '/index' }"><i class="el-icon-menu"></i> 首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/dns-dashboard' }">DNS日志分析</el-breadcrumb-item>
      <el-breadcrumb-item>资源分布分析</el-breadcrumb-item>
    </el-breadcrumb>

    <div class="handle-box">
      <div>
        <el-row style="margin-top:3%">
          <el-col :span="12" >
            <div id="chart1"></div>
          </el-col>
            <el-col :span="12">
            <div id="chart2"></div>
          </el-col>
        </el-row>
      </div>
    </div>
  </div>
  
</template>
<script>
  import 'echarts/map/js/china';
  import 'echarts/map/js/province/guangdong';
  import { CITY_GEO_COORDS } from '../geo.js'
  import { restful_path } from '../util.js'
  export default {
    data() {
      return {
        formFilter: {
          select_industry: '',
        },
        items: [],
        data:[],
        valueDate: '',
        valueWeek: ''
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
        console.log(this.valueWeek)
      },
      handleDatePick() {
        this.valueWeek = '';
      },
      showCharts() {
        this.drawLine()
      },
      drawLine(){
				var chart1 = document.getElementById('chart1');
				var chart2 = document.getElementById('chart2');
				var chart1Container = function () {
				    chart1.style.width = ((window.innerWidth - 300)/2) +'px';
				    chart1.style.height = ((window.innerHeight - 200)) +'px';
				};
				var chart2Container = function () {
				    chart2.style.width = ((window.innerWidth - 300)/2) + 'px';
				    chart2.style.height = ((window.innerHeight - 200)) +'px';
				};
				chart1Container();
        chart2Container();
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
                  var data = [
                      {name: '东莞', value: 10780},
                      {name: '北京', value: 10722},
                      {name: '广州', value: 9636},
                      {name: '深圳', value: 8951},
                      {name: '珠海', value: 7225},
                      {name: '佛山', value: 5388},
                      {name: '上海', value: 4540},
                      {name: '云浮', value: 4374},
                      {name: '汕头', value: 2292},
                      {name: '江门', value: 1997},
                      {name: '惠州', value: 1771},
                      {name: '杭州', value: 1559},
                      {name: '中山', value: 1375},
                      {name: '福州', value: 1369},
                      {name: '揭阳', value: 1241},
                      {name: '梅州', value: 1091},
                      {name: '肇庆', value: 902},
                      {name: '厦门', value: 780},
                      {name: '南宁', value: 761},
                      {name: '湛江', value: 716},
                      {name: '天津', value: 546},
                      {name: '苏州', value: 415},
                      {name: '衡阳', value: 386},
                      {name: '青岛', value: 361},
                      {name: '无锡', value: 343},
                      {name: '南京', value: 338},
                      {name: '武汉', value: 310},
                      {name: '长沙', value: 220},
                      {name: '扬州', value: 214},
                      {name: '潮州', value: 178},
                      {name: '金华', value: 178},
                      {name: '济南', value: 158},
                      {name: '西安', value: 154},
                      {name: '桂林', value: 148},
                      {name: '徐州', value: 129},
                      {name: '郑州', value: 126},
                      {name: '宁波', value: 104},
                      {name: '重庆', value: 101},
                      {name: '盐城', value: 96},
                      {name: '成都', value: 96},
                      {name: '舟山', value: 89},
                      {name: '洛阳', value: 82},
                      {name: '汕尾', value: 80},
                      {name: '温州', value: 76},
                      {name: '茂名', value: 74},
                      {name: '襄阳', value: 73},
                      {name: '泉州', value: 71},
                      {name: '台州', value: 66},
                      {name: '株洲', value: 59},
                      {name: '三亚', value: 58},
                      {name: '淮安', value: 53},
                      {name: '南通', value: 46},
                      {name: '桃园市', value: 38},
                      {name: '常州', value: 37},
                      {name: '盘锦', value: 36},
                      {name: '益阳', value: 31},
                      {name: '昌江黎族自治县', value: 30},
                      {name: '屯昌县', value: 30},
                      {name: '宿迁', value: 26},
                      {name: '镇江', value: 26},
                      {name: '湖州', value: 25},
                      {name: '海口', value: 25},
                      {name: '哈尔滨', value: 24},
                      {name: '南昌', value: 24},
                      {name: '常德', value: 24},
                      {name: '合肥', value: 22},
                      {name: '绵阳', value: 19},
                      {name: '廊坊', value: 18},
                      {name: '石家庄', value: 17},
                      {name: '莆田', value: 17},
                      {name: '嘉兴', value: 16},
                      {name: '阜新', value: 16},
                      {name: '绍兴', value: 15},
                      {name: '黄石', value: 14},
                      {name: '景德镇', value: 14},
                      {name: '沈阳', value: 14},
                      {name: '铁岭', value: 12},
                      {name: '辽阳', value: 11},
                      {name: '昆明', value: 9},
                      {name: '三明', value: 9},
                      {name: '呼和浩特', value: 9},
                      {name: '吉安', value: 9},
                      {name: '烟台', value: 8},
                      {name: '中卫', value: 7},
                      {name: '台中市', value: 7},
                      {name: '上饶', value: 6},
                      {name: '梧州', value: 6},
                      {name: '济宁', value: 4},
                      {name: '清远', value: 4},
                      {name: '台北市', value: 4},
                      {name: '孝感', value: 4},
                      {name: '九江', value: 3},
                      {name: '兰州', value: 3},
                      {name: '泰州', value: 3},
                      {name: '丽水', value: 2},
                      {name: '宿州', value: 2},
                      {name: '鄂州', value: 2},
                      {name: '黔西南布依族苗族自治州', value: 2},
                      {name: '鞍山', value: 2},
                      {name: '乌兰察布', value: 2},
                      {name: '贵阳', value: 2},
                      {name: '咸宁', value: 2},
                      {name: '许昌', value: 1},
                      {name: '大连', value: 1},
                      {name: '平顶山', value: 1},
                      {name: '抚州', value: 1},
                      {name: '安康', value: 1},
                      {name: '巴中', value: 1},
                      {name: '玉林', value: 1},
                      {name: '西宁', value: 1},
                      {name: '赣州', value: 1},
                      ];

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
          //console.log(res)
          return res;
        };

        // 基于准备好的dom，初始化echarts实例
        chart1 = this.$echarts.init(chart1);
        chart2 = this.$echarts.init(chart2);
        // 绘制图表
        chart1.setOption({
          backgroundColor: '#FFF',
            title: {
              text: '域名所在地分布（广东）',
              left: 'center',
              textStyle: {
                  color: '#000'
              }
            },
            tooltip : {
              trigger: 'item'
            },
            geo: {
              map: '广东',
              zoom: 1.1,
              roam: true,
              label: {
                emphasis: {
                  show: true,
                  textStyle:{
                    color:'#FFF'
                  }
                }
              },
              center: [113.23, 23.16],
              itemStyle: {
                normal: {
                  areaColor: '#FDF9D5',
                  borderColor: '#EEC591'
                },
                emphasis: {
                  areaColor: '#F8F197'
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
                      color: '#F37737'
                  }
                }
              },
              {
                name: 'Top 5',
                type: 'effectScatter',
                coordinateSystem: 'geo',
                data: convertData(data.sort(function (a, b) {
                    return b.value - a.value;
                }).slice(0, 6)),
                symbolSize: function (val) {
                    return val[2] / 600;
                },
                showEffectOn: 'emphasis',
                rippleEffect: {
                    brushType: 'stroke'
                },
                hoverAnimation: true,
                label: {
                  normal: {
                    formatter: '{b}',
                    position: 'right',
                    show: false
                  }
                },
                itemStyle: {
                  normal: {
                    color: '#F37737',
                    shadowBlur: 5,
                    shadowColor: '#F37737'
                  }
                },
                zlevel: 1
              }
            ]
          }); 
         chart2.setOption({
          backgroundColor: '#FFF',
          title: {
            text: '域名所在地分布（全国）',
            left: 'center',
            textStyle: {
                color: '#000'
            }
          },
          tooltip : {
            trigger: 'item'
          },
          geo: {
            map: 'china',
            zoom: 1.2,
            roam: true,
            label: {
              emphasis: {
                show: true,
                textStyle:{
                  color:'#FFF'
                }
              }
            },
            center:[103.73, 36.03],
            itemStyle: {
              normal: {
                areaColor: '#FDF9D5',
                borderColor: '#EED5B7'
              },
              emphasis: {
                areaColor: '#F8F197'
              }
            }
          },
          series : [
            {
              name: '数量',
              type: 'scatter',
              coordinateSystem: 'geo',
              data: convertData(data),
              symbolSize: function (val) {
                  return val[2] / 600;
              },
              label: {
                  normal: {
                      formatter: '{b}',
                      position: 'right',
                      show: false
                  },
                  emphasis: {
                      show: true
                  }
              },
              itemStyle: {
                normal: {
                    color: '#CD3700'
                }
              }
            },
            {
              name: 'Top 5',
              type: 'effectScatter',
              coordinateSystem: 'geo',
              data: convertData(data.sort(function (a, b) {
                  return b.value - a.value;
              }).slice(0, 5)),
              symbolSize: function (val) {
                  return val[2] / 700;
              },
              showEffectOn: 'emphasis',
              rippleEffect: {
                  brushType: 'stroke'
              },
              hoverAnimation: true,
              label: {
                normal: {
                  formatter: '{b}',
                  position: 'right',
                  show: true
                }
              },
              itemStyle: {
                normal: {
                  color: '#F37737',
                  shadowBlur: 5,
                  shadowColor: '#F37737'
                }
              },
              zlevel: 1
            }
          ]
        }); 
      }
    },
    mounted(){
      this.drawLine();
    }
  }
</script>
<style lang="scss" scoped>
  .handle-box{
    margin-top: 20px;
  }
  .el-select-dropdown__item {
    text-align: center;
  }
  .el-input__inner {
    margin-right: 10px;
  }
  .el-input--small {
    .el-input__inner {
      margin-top: 10px;
    }
    .el-input__icon {
      margin-top: 5px;
    }
  }
  .el-form-item__content {
    line-height:50px;
  }
  .el-select {
    .el-input {
      .el-select__caret {
        margin-top: 2px
      }
    }
  }
</style>