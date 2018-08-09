<template>
  <div>
    <el-breadcrumb separator-class="el-icon-arrow-right" style="font-size: 14px">
      <el-breadcrumb-item :to="{ path: '/index' }"><i class="el-icon-menu"></i> 首页</el-breadcrumb-item>
      <el-breadcrumb-item :to="{ path: '/dns-dashboard' }">DNS日志分析</el-breadcrumb-item>
      <el-breadcrumb-item>备案信息查询</el-breadcrumb-item>
    </el-breadcrumb>

    <div class="handle-box">
      <el-form :model="formFilter" ref="formFilter" style="display:inline-block">
        <el-row :gutter="10">
          <el-col :span="6" class="input">
            <el-form-item prop="input_beianCode">
              <el-input placeholder=""  size="small" v-model="formFilter.input_beianCode" @keyup.enter.native="DataFilter()"></el-input>
            </el-form-item>
          </el-col>
          
          <el-tooltip content="通过域名查询ICP备案号" placement="top">
          <el-col :span="6">
            <el-form-item>
              <el-button type="primary" icon="el-icon-search" size="small" @click="qeury()">正向查询</el-button>
            </el-form-item>
          </el-col>
          </el-tooltip>

          <el-tooltip content="通过ICP备案号查询域名" placement="top">
          <el-col :span="6">
            <el-form-item>
              <el-button type="primary" icon="el-icon-search" size="small" @click="inverse_query()">反向查询</el-button>
            </el-form-item>
          </el-col>
          </el-tooltip>
        </el-row>
      </el-form>
    </div>

    <el-table
        :data="data.slice((currentPage-1)*pageSize,currentPage*pageSize)"
        border
        style="width: 100%;"
        ref="multipleTable"
        size="mini">
      <el-table-column prop="tld" label="二级域名" width="250" align="center">
      </el-table-column>
      <el-table-column prop="name" label="网站名称" align="center">
      </el-table-column>
      <el-table-column prop="siteBeianCode" label="网站备案号" width="250" align="center" >
      </el-table-column>
      <el-table-column prop="companyBeianCode" label="公司备案号" width="250" align="center">
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
          input_beianCode: ''
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

      inverse_query() {
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/get-icp-info-by-beiancode',
          data: {
            'beianCode': this.formFilter.input_beianCode
          }
        }).then(response => {
          if(response.data.status){
            this.data = response.data.data;
          }
        }).catch(error => {});
      },

      inverse_query() {
        this.$http({
          method: 'post',
          url: restful_path + '/api/dns/get-icp-info-by-beiancode',
          data: {
            'beianCode': this.formFilter.input_beianCode
          }
        }).then(response => {
          if(response.data.status){
            this.data = response.data.data;
          }
        }).catch(error => {});
      },
    }
  }
</script>

<style lang="scss" scoped>
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
