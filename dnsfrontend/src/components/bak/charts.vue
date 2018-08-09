<template>
  <div style="width:100%; height:100%">
    <el-table
        :data="data"
        border
        style="width: 100%; margin-top:20px;"
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

  	<el-row>
  		<el-col :span="12">
  			<div id="chartLoopback" style="top:20px"></div>
  		</el-col>
  		  <el-col :span="12">
  			<div id="chartInterface" style="top:20px"></div>
  		</el-col>
  	</el-row>
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
				}]
			}
		},
		methods: {
			drawLine(){
				var chartLoopback = document.getElementById('chartLoopback');
				var chartInterface = document.getElementById('chartInterface');
				var chartLoopbackContainer = function () {
				    chartLoopback.style.width = (window.innerWidth - 300)/2+'px';
				    chartLoopback.style.height = '400px';
				};
				var chartInterfaceContainer = function () {
				    chartInterface.style.width = (window.innerWidth - 300)/2+'px';
				    chartInterface.style.height = '400px';
				};
				chartLoopbackContainer();
				chartInterfaceContainer();

        // 基于准备好的dom，初始化echarts实例
        chartLoopback = this.$echarts.init(chartLoopback);
        chartInterface = this.$echarts.init(chartInterface);
        // 绘制图表
        chartLoopback.setOption({
					title : {
		        text: 'Loopback地址使用情况',
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
		        data: ['已使用','未使用']
			    },
			    series : [
		        {
	        		name: 'Loopback地址',
	            type: 'pie',
	            radius : '55%',
	            center: ['50%', '40%'],
	            data:[
                {value:35, name:'已使用'},
                {value:310, name:'未使用'}
	            ],
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
        chartInterface.setOption({
					title : {
		        text: '接口地址使用情况',
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
		        data: ['已使用','未使用']
			    },
			    series : [
		        {
	        		name: '接口地址',
	            type: 'pie',
	            radius : '55%',
	            center: ['50%', '40%'],
	            data:[
                {value:53, name:'已使用'},
                {value:200, name:'未使用'}
	            ],
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
/*        window.onresize = function () {
			    chartLoopbackContainer();
			    chartInterfaceContainer();
			    chartLoopback.resize();
			    chartInterface.resize();
		  	};*/
			}
		},
		mounted(){
	    this.drawLine();
	  }
	}
</script>

<style lang="scss" scopd>

</style>