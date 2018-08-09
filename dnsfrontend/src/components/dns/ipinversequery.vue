<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right" style="font-size: 14px">
      <el-breadcrumb-item :to="{ path: '/index' }"><i class="el-icon-menu"></i> 首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/dns-dashboard' }">DNS日志分析</el-breadcrumb-item>
      <el-breadcrumb-item>IP地址反查</el-breadcrumb-item>
    </el-breadcrumb>

    <div class="handle-box">
      <el-form :model="formFilter" ref="formFilter" style="display:inline-block">
        <el-row :gutter="10">
          <el-col :span="6" class="input">
            <el-form-item prop="input_ipAddress">
              <el-input placeholder="请输入IP地址"  size="small" v-model="formFilter.input_ipAddress" @keyup.enter.native="DataFilter()"></el-input>
            </el-form-item>
          </el-col>
          
          <el-col :span="2">
            <el-form-item>
              <el-button type="primary" icon="el-icon-search" size="small" @click="DataFilter()">查询</el-button>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
    </div>

    <el-table
        :data="data.slice((currentPage-1)*pageSize,currentPage*pageSize)"
        border
        style="width: 100%;"
        ref="multipleTable"
        size="mini">
      <el-table-column prop="id" label="id" align="center" v-if="false">
      </el-table-column>
      <el-table-column prop="ip" label="IP" width="180" align="center">
      </el-table-column>
      <el-table-column prop="domain" label="域名" align="center" >
      </el-table-column>
      <el-table-column prop="country" label="国家" width="180" align="center">
      </el-table-column>
      <el-table-column prop="province" label="省份" width="180" align="center">
      </el-table-column>
      <el-table-column prop="operator" label="运营商" width="180" align="center">
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
        currentPage:1,
        pageSize:10,
        formFilter: {
          ip: ''
        }
      }
    },
    methods: {

      handleSizeChange(size) {
       this.pageSize = size;
      },

      handleCurrentChange(currentPage) {
        this.currentPage = currentPage;
      },

      DataFilter() {
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/inverse-ip-query',
          data: {
            'ip': this.formFilter.input_ipAddress
          }
        }).then(response => {
          if(response.data.status){
            //console.log(response.data.data);
            this.data = response.data.data;
          }
        }).catch(error => {
          //console.log(error);
        });
      },
    }
  }
</script>

<style lang="scss" scopd>
  .handle-box{
    margin-top: 20px;
    text-align: center;
  }
  .handle-input{
    width: 300px;
  }

  .el-input__inner {
    margin-right: 10px;
  }
  .input {
    width:200px;
  }
</style>
