<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right" style="font-size: 14px">
      <el-breadcrumb-item :to="{ path: '/index' }"><i class="el-icon-menu"></i> 首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/dns-dashboard' }">DNS日志分析</el-breadcrumb-item>
      <el-breadcrumb-item>重点域名展示</el-breadcrumb-item>
    </el-breadcrumb>

    <div class="handle-box">
      <el-form :model="formFilter" ref="formFilter" style="display:inline-block">
        <el-row :gutter="10">
          <el-col class="handle-select-input">
            <el-form-item prop="select_domain">
              <el-select placeholder="域名"  size="small" v-model="formFilter.select_domain" clearable >
                <el-option v-for="item in items" :label="item" :value="item" :key="item"></el-option>
              </el-select>
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

    <div>
      <el-row >
        <el-col :span="8" style="text-align:center">
          <div id="chart1" style="display:inline-block"></div>
        </el-col>
        <el-col :span="8" style="text-align:center">
          <div id="chart2" style="display:inline-block"></div>
        </el-col>
        <el-col :span="8" style="text-align:center">
          <div id="chart3" style="display:inline-block"></div>
        </el-col>
      </el-row>
    </div>

    <el-table
        :data="data"
        border
        style="width: 100%;"
        ref="multipleTable"
        size="mini">
      <el-table-column prop="date" label="日期" width="120" align="center">
      </el-table-column>
      <el-table-column prop="domain" label="域名" width="200" align="center">
      </el-table-column>
      <el-table-column prop="resolved_ip" label="IP地址" align="center" >
      </el-table-column>
      <el-table-column prop="count" label="解析量" width="120" align="center">
      </el-table-column>
      <el-table-column prop="success_rate" label="解析成功率" width="120" align="center">
      </el-table-column>
      <el-table-column label="状态" width="140" align="center">
        <template slot-scope="scope">
          <el-button size="mini" :type="scope.row.status | statusFilter" round>{{ scope.row.status }}</el-button>
        </template>
      </el-table-column>
    </el-table>



    <div class="pagination" style="float: right; margin-top:10px">
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
    data() {
      return {
        data: [],
        items: [],
        formFilter: {
          select_domain: ''
        },
        pageSize:10,
        currentPage:1
      }
    },
    filters: {
      statusFilter(status) {
        const statusMap = {
          '正常':'success',
          '异常':'danger'
        }
        return statusMap[status]
      }
    },
/*    created() {
      this.showData();
    },*/
    methods: {

      handleSizeChange(size) {
       this.pageSize = size;
      },

      handleCurrentChange(currentPage) {
        this.currentPage = currentPage;
      },

      getDropDownList () {
        this.$http({
          method: 'get',
          url: restful_path + '/api/dns/get-key-domain-name'
        }).then(response => {
          if(response.data.status){
            this.items = response.data.data;
          }
        }).catch(error => {});
      },

      DataFilter() {
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/single-domain',
          data: {
            'domain': this.formFilter.select_domain
          }
        }).then(response => {
          if(response.data.msg){
            this.data = response.data.data;
            //console.log(response.data.data)
            let name_list = []
            let count_list = []
            let success_rate_list = []
            let ip_monitor_list = []
            for (var i = response.data.data.length -1 ; i >= 0; i --) {
              name_list.push(response.data.data[i].date);
              //console.log(response.data.data[i].date)
              count_list.push(response.data.data[i].count);
              if(response.data.data[i].status == '正常'){
                ip_monitor_list.push('1');
              } else {
                ip_monitor_list.push('-1');
              }
              success_rate_list.push(response.data.data[i].success_rate.replace('%',''));
            }
            this.drawLine(name_list, count_list, success_rate_list, ip_monitor_list)
          }
        }).catch(error => {
          //console.log(error);
        });
      },
      drawLine(list1, list2, list3, list4){
        //console.log(list3)
				var chart1 = document.getElementById('chart1');
        var chart2 = document.getElementById('chart2');
        var chart3 = document.getElementById('chart3');
				var chart1Container = function () {
				    chart1.style.width = ((window.innerWidth - 300)/3) +'px';
				    chart1.style.height = '300px';
				};
				var chart2Container = function () {
				    chart2.style.width = ((window.innerWidth - 300)/3) + 'px';
				    chart2.style.height = '300px';
        };
				var chart3Container = function () {
				    chart3.style.width = ((window.innerWidth - 300)/3) + 'px';
				    chart3.style.height = '300px';
				};
				chart1Container();
        chart2Container();
        chart3Container();

        // 基于准备好的dom，初始化echarts实例
        chart1 = this.$echarts.init(chart1);
        chart2 = this.$echarts.init(chart2);
        chart3 = this.$echarts.init(chart3);
        // 绘制图表
        chart1.setOption({
					title : {
            text: '域名解析量',
          },
          tooltip : {
            trigger: 'axis'
          },
/*           legend: {
            data:['解析量']
          }, */
          calculable : true,
          grid: { 
            x: 60,
            y: 50,
            x2: 30,
            y2: 60  
          },
          xAxis : [
            {
              type : 'category',
              data : list1
/*               axisLabel:{  
                interval:0,
                rotate:-30
              }  */
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
              //barWidth: 20,
              type:'bar',
              data:list2
            }
          ]
        });
        chart2.setOption({
          title: {
            text: '解析成功率'
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
/*           legend: {
            data:['解析成功率']
          }, */
          grid: { 
            x: 60,
            y: 50,
            x2: 30,
            y2: 60  
          },
          xAxis : [
            {
              type : 'category',
              boundaryGap : false,
              data : list1
            }
          ],
          yAxis : [
            {
              type : 'value',
              min:50,
              max:100,
              //boundaryGap: ['0%', '20%'],
              axisLabel: {
                formatter: '{value} %'
              }
            }
          ],
          series : [
            {
              name:'解析成功率',
              type:'line',
              //stack: '成功率',
              areaStyle: {normal: {}},
              data: list3
            }
          ]
        }); 
        chart3.setOption({
					title : {
            text: 'IP变化情况',
          },
          tooltip : {
            trigger: 'axis'
          },
/*           legend: {
            data:['解析量']
          }, */
          calculable : true,
          grid: { 
            x: 60,
            y: 50,
            x2: 30,
            y2: 60  
          },
          xAxis : [
            {
              type : 'category',
              data : list1
/*               axisLabel:{  
                interval:0,
                rotate:-30
              }  */
            }
          ],
          yAxis : [
            {
              type : 'value',
              min: -1,
              max: 1,
              interval: 1,
              axisLabel:{
                formatter: function (value) {
                  var texts = [];
                  if(value == 1){
                    texts.push('正常');
                  }
                  else if(value == 0){
                    texts.push('');
                  }
                  else{
                    texts.push('异常');
                  }
                  return texts;
                }
              }
            }
          ],
          series : [
            {
              name:'解析量',
              barWidth: 20,
              type:'bar',
              data:list4
            }
          ]
        });
      }
    },
    created(){
      this.getDropDownList();
    },
    computed: {
      ButtonType(val) {
        if(val == '正常'){
          return'success'
        } else {
          return 'warning'
        }
      }
    }
  }
</script>

<style lang="scss" scoped>
  .handle-box{
    margin-top: 20px;
    text-align: center;
  }
  .handle-select-input{
    width: 200px;
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
</style>
