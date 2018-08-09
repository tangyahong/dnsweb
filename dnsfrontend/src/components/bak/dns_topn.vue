<template>

  <div style="width:100%; height:100%">
    <el-row>
  		<el-col>
  			<div id="dns-topn-chart" style="top:20px;"></div>
  		</el-col>
  	</el-row>


    <el-table
        :data="data"
        border
        style="width: 100%; top:30px"
        ref="multipleTable"
        size="mini">
      <el-table-column type="selection" width="40" align="center">
      </el-table-column>
      <el-table-column prop="id" label="id" align="center" v-if="false">
      </el-table-column>
      <el-table-column prop="city" label="地市" width="80" align="center">
      </el-table-column>
      <el-table-column prop="ipAddressLoopbackUsed" label="Loopback地址占用数" align="center" >
      </el-table-column>
      <el-table-column prop="ipAddressLoopbackIdle" label="Loopback地址空闲数" align="center" >
      </el-table-column>
      <el-table-column prop="LoopbackRate" label="Loopback地址使用率" align="center" >
      </el-table-column>
      <el-table-column prop="ipAddressinterfaceUsed" label="接口地址占用数" align="center" >
      </el-table-column>
      <el-table-column prop="ipAddressinterfaceIdle" label="接口地址空闲数" align="center" >
      </el-table-column>
      <el-table-column prop="interfaceRate" label="接口地址使用率" align="center" >
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
	import echarts from "echarts"
	export default {
		data(){
			return {
				data:[{
					'city':'清远',
					'ipAddressLoopbackUsed': '100',
					'ipAddressLoopbackIdle': '100',
					'LoopbackRate': '50%',
					'ipAddressinterfaceUsed': '100',
					'ipAddressinterfaceIdle': '100',
					'interfaceRate': '50%'
        },
        {
					'city':'清远',
					'ipAddressLoopbackUsed': '100',
					'ipAddressLoopbackIdle': '100',
					'LoopbackRate': '50%',
					'ipAddressinterfaceUsed': '100',
					'ipAddressinterfaceIdle': '100',
					'interfaceRate': '50%'
				}]
			}
		},
		methods: {
			drawLine(){
				var dnsTopnChart = document.getElementById('dns-topn-chart');
				var dnsTopnChartContainer = function () {
				    dnsTopnChart.style.width = (window.innerWidth - 300)+'px';
				    dnsTopnChart.style.height = '300px';
				};
				dnsTopnChartContainer();

        // 基于准备好的dom，初始化echarts实例
        dnsTopnChart = this.$echarts.init(dnsTopnChart);
        // 绘制图表
        dnsTopnChart.setOption({
/* 					title: {
            text: 'TOP N'
          }, */
          tooltip: {
            trigger: 'axis'
          },
          legend: {
            data:['解析量']
          },
          grid: {
            left: '5%',
            right: '1.5%',
            bottom: '3%',
            containLabel: true
          },
          xAxis: {
            type: 'category',
            boundaryGap: false,
            data: ['周一','周二','周三','周四','周五','周六','周日']
          },
          yAxis: {
            type: 'value'
          },
          series: [
            {
              name:'解析量',
              type:'line',
              stack: '总量',
              data:[120, 132, 101, 134, 90, 230, 210]
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

<style lang="scss" scopd>

</style>