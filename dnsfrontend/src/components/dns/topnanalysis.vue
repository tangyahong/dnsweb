<template>
  <div>
    <el-breadcrumb 
      separator-class="el-icon-arrow-right" 
      style="font-size: 14px" >
      <el-breadcrumb-item :to="{ path: '/index' }"><i class="el-icon-menu"></i> 首页</el-breadcrumb-item>
      <el-breadcrumb-item>DNS日志分析</el-breadcrumb-item>
      <el-breadcrumb-item>TOP N域名分析</el-breadcrumb-item>
    </el-breadcrumb>

      <div class="handle-box">
        <div class="block">
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
        </div>
        <div class="block">
          <el-date-picker
            v-model="valueDate"
            type="date"
            size="small"
            @change="handleDatePick"
            value-format="yyyyMMdd"
            placeholder="选择日期">
          </el-date-picker>
        </div>
        <div>
          <el-row>
            <el-col :span="24" style="text-align:center" v-show="showCharts">
              <div id="dns-topn-chart" style="margin-top:-30px; margin-right:20px; margin-bottom:20px; display:inline-block"></div>
            </el-col>
          </el-row>
        </div>

      </div>
      <el-table
          :data="data.slice((currentPage-1)*pageSize,currentPage*pageSize)"
          border
          style="width: 100%; margin-top:10px;"
          ref="multipleTable"
          size="mini">
        <el-table-column prop="id" label="id" align="center" v-if="false">
        </el-table-column>
        <el-table-column prop="rank" label="排名" width="60" align="center">
        </el-table-column>
        <el-table-column label="域名" width="180" align="center" >
          <template slot-scope="scope">
            <el-button size="mini" type="text" @click="showSingleDomain(scope.row)" >{{ scope.row.domain }}</el-button>
          </template>
        </el-table-column>
        <el-table-column prop="service_name" label="首页名称" width="110" align="center" >
        </el-table-column>
        <el-table-column prop="category_name" label="域名分类" width="110" align="center" >
        </el-table-column>
        <el-table-column prop="resolved_ip" label="IP解析" align="center" >
        </el-table-column>
        <el-table-column prop="count" label="解析量" width="80" align="center" >
        </el-table-column>
        <el-table-column prop="success_rate" label="解析成功率" width="100" align="center" >
        </el-table-column>
        <el-table-column prop="drill" label="钻取分析" width="200" align="center" >
          <template slot-scope="scope">
            <el-button size="mini" type="text" @click="showWhoisInfo(scope.row)">Whois</el-button>
            <el-button size="mini" type="text" @click="showICPInfo(scope.row)">ICP详情</el-button>
            <el-button size="mini" type="text" @click="showISPInfo(scope.row)">ISP详情</el-button>
          </template>
        </el-table-column>
      </el-table>

      <el-dialog title="近一周解析量" :visible.sync="dialogChartsVisible" style="text-align:center">
        <div id="dns-domain-chart" style="width:600px; height:300px; display:inline-block"></div>
      </el-dialog>

      <el-dialog title="ISP详情" :visible.sync="dialogISPTableVisible" style="width:1400px; height:600px; text-align:center">
        <div style="display:inline-block">
          <el-table :data="ispData" stripe size="mini">
            <el-table-column property="resolved_ip" label="IP" width="150" align="center"></el-table-column>
            <el-table-column property="subnet" label="子网" width="150" align="center"></el-table-column>
            <el-table-column property="country" label="国家" width="100" align="center"></el-table-column>
            <el-table-column property="province" label="省份" width="100" align="center"></el-table-column>
            <el-table-column property="operator" label="运营商" width="100" align="center"></el-table-column>
          </el-table>
        </div>
      </el-dialog>

      <el-dialog title="ICP详情" :visible.sync="dialogICPTableVisible" style="width:1400px; height:1000px; text-align:center">
        <div style="display:inline-block">
          <el-table :data="icpData" stripe size="mini">
            <el-table-column property="tld" label="二级域名" width="150" align="center"></el-table-column>
            <el-table-column property="name" label="站点名称" width="150" align="center"></el-table-column>
            <el-table-column property="siteBeianCode" label="网站备案号" width="150" align="center"></el-table-column>
            <el-table-column property="companyBeianCode" label="公司备案号" width="150" align="center"></el-table-column>
          </el-table>
        </div>
      </el-dialog>

      <el-dialog title="Whois信息" :visible.sync="dialogWhoisVisible" style="width:1400px; height:600px; text-align:center">
        <div style="display:inline-block">
          <el-table :data="whoisData" stripe border size="mini" :show-header="false">
            <el-table-column property="name" label="" width="150" align="center"></el-table-column>
            <el-table-column property="value" label="" width="500" align="center"></el-table-column>
          </el-table>
        </div>
      </el-dialog>


      <div class="pagination" style="float: right; margin-top:10px; margin-right:20px">
        <el-pagination
          @size-change="handleSizeChange"
          @current-change="handleCurrentChange"
          :current-page="currentPage"
          layout="total, sizes, prev, pager, next, jumper"
          :page-sizes="[5, 10, 20, 50]"
          :page-size="pageSize"
          :total="data.length">
        </el-pagination>
      </div>
    </div>
</template>

<script>
  import { restful_path } from '../util.js'
	export default {
		data(){
			return {
        data:[],
        valueWeek:'',
        valueDate:'20171201',
        currentPage:1,
        pageSize:10,
        showCharts:false,
        dialogChartsVisible: false,
        dialogISPTableVisible: false,
        dialogICPTableVisible: false,
        dialogWhoisVisible: false,
        ispData:[],
        icpData:[],
        whoisData:[]
			}
		},
		methods: {
      handleSizeChange(size) {
       this.pageSize = size;
      },

      handleCurrentChange(currentPage) {
        this.currentPage = currentPage;
      },

			drawLine(list1, list2) {
				var dnsTopnChart = document.getElementById('dns-topn-chart');
				var dnsTopnChartContainer = function () {
				    dnsTopnChart.style.width = (window.innerWidth - 280)+'px';
				    dnsTopnChart.style.height = '350px';
				};
				dnsTopnChartContainer();

        dnsTopnChart = this.$echarts.init(dnsTopnChart);
        dnsTopnChart.setOption({
					title : {
            text: '解析量',
          },
          tooltip : {
            trigger: 'axis'
          },
/*           legend: {
            data:['解析量']
          }, */
          grid: { 
            x: 60,
            y: 40,
            x2: 10,
            y2: 110  
          },
          calculable : true,
          xAxis : [
            {
              type : 'category',
              data : list1,
              axisLabel:{  
                interval:0,
                rotate:-90
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
      },
/*       showData() {
        setTimeout(() => {
          this.$http({
          method: 'get',
          url: 'http://127.0.0.1:5000/api/dns/topn/100'
          }).then(response => { 
            this.data = response.data.data;
          }).catch(error => {
            console.log(error);
          });
        }, 10);
      }, */
/*       handleTimePick(val){
        console.log(val)
      }, */
      handleWeekPick(){
        this.valueDate = ''
        //console.log(this.valueWeek)
        let d = new Date(this.valueWeek);
        let weekFormat = d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate();
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/topn',
          data: {
            'date': '',
            'week': weekFormat,
            'count': 100
          }
        }).then(response => {
          //console.log(Boolean(response.data.data))
          if(response.data.status && response.data.data.length > 0) {
            //console.log('1');
            this.data = response.data.data;
            this.showCharts = true;
            let name_list = []
            let value_list = []
            for(var i = 0; i < 40; i ++) {
              name_list.push(response.data.data[i]['domain']);
              value_list.push(response.data.data[i]['count']);
            }
            this.drawLine(name_list, value_list);
          } else {
            this.showCharts = false;
            this.data = [];
          }
        }).catch(error => {
          console.log(error);
        });
      },
      handleDatePick(){
        this.valueWeek = ''
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/topn',
          data: {
            'date': this.valueDate,
            'week': '',
            'count': 100
          }
        }).then(response => {
          if(response.data.status && response.data.data.length > 0) {
            this.data = response.data.data;
            this.showCharts = true;
            let name_list = []
            let value_list = []
            for(var i = 0; i < 40; i ++) {
              name_list.push(response.data.data[i]['domain']);
              value_list.push(response.data.data[i]['count']);
            }
            this.drawLine(name_list, value_list);
          } else {
            this.showCharts = false;
            this.data = [];
          }
        }).catch(error => {
          console.log(error);
        });
      },

      showISPInfo(row) {
        this.dialogISPTableVisible = true;
        let ip = row.resolved_ip.split(';')
        console.log(ip)
        this.$http({
          method: 'post',
          url: restful_path  + '/api/dns/ip-isp-query-list',
          data: {
            'resolved_ip': ip
          }
        }).then(response => {
          if(response.data.status){
            this.ispData = response.data.data;
          }
        }).catch(error => {});
      },

      showICPInfo(row) {
        this.dialogICPTableVisible = true;
        console.log(row.tld);
        //let ip = row.resolved_ip.split(';')
        //console.log(ip)
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/get-icp-info',
          data: {
            'tld': row.tld
          }
        }).then(response => {
          if (response.data.status){
            this.icpData = response.data.data;
          }
          //console.log(response.data);
        }).catch(error => {});
      },

      showWhoisInfo(row) {
        this.dialogWhoisVisible = true;
        //console.log(row.tld);
        //let ip = row.resolved_ip.split(';')
        //console.log(ip)
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/get-whois-info',
          data: {
            'tld': row.tld
          }
        }).then(response => {
          if (response.data.status){
            this.whoisData = response.data.data;
          }
        }).catch(error => {});
      },


      showSingleDomain(row) {
        this.dialogChartsVisible = true;
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/topn/singledomain',
          data: {
            'domain': row.domain
          }
        }).then(response => {
          //var name_list = []
          //let value_list = []
          if(response.data.status) {
            //this.data = response.data.data;
            //this.showCharts = true;
            var name_list = []
            var value_list = []
            var period = response.data.data.length;
            if (period > 7) { period = 7;} 
            for(var i = period - 1; i >= 0 ; i --) {
              name_list.push(response.data.data[i]['name']);
              value_list.push(response.data.data[i]['value']);
            }
            //this.drawLine(name_list, value_list);
            setTimeout(() => {
              var dnsDomainChart = document.getElementById('dns-domain-chart');
              dnsDomainChart = this.$echarts.init(dnsDomainChart);
              dnsDomainChart.setOption({
                title: {
                  text: row.domain
                },
                tooltip : {
                  trigger: 'axis',
                  axisPointer: {
                    type: 'cross',
                    label: {
                      backgroundColor: '#6a7985'
                    }
                  }
                },
                legend: {
                  data:['解析量']
                },
/*                 toolbox: {
                  feature: {
                    saveAsImage: {}
                  }
                }, */
                grid: {
                  left: '3%',
                  right: '5%',
                  bottom: '3%',
                  containLabel: true
                },
                xAxis : [
                  {
                    type : 'category',
                    boundaryGap : false,
                    data : name_list
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
                    type:'line',
                    stack: '总量',
                    areaStyle: {normal: {}},
                    data: value_list
                  }
                ]
              }); 
            }, 100);
          }
        }).catch(error => {
          //console.log(error);
        });
      }
		},
		mounted(){
	    //this.drawLine();
    },
    created() {
      // this.showData();
    }
	}
</script>

<style lang="scss" scoped>
  .handle-box {
    /* margin-top: 20px; */
    text-align: center;
    margin-right: -20px;
  }
  .div-css {
    border:1px solid #EEEEE0; 
    margin-left:20px; 
    margin-top:20px; 
    margin-right:20px;
    box-shadow:0px 0px 5px 2px #EEEEE0;
  }

  .el-date-editor.el-input__inner {
    float: right;
    margin-right: 20px;
    margin-top: 20px;
    z-index: 2;
  }
/*   .el-input--small .el-input__inner {
    float: right;
    margin-right: 20px;
    margin-top: 20px;
    z-index: 2;
  } */
  .block {
    position: relative;
    float: right;
    margin-right: 20px;
    margin-top: 20px;
    z-index: 1;
  }
</style>