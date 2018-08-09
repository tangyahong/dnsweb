<template>
  <div class="container" style="height:100%">
    <el-container style="height: 100%;">
      <el-header style="font-size: 14px; background-color:#25374F; height: 45px;" id="header">
        <div style="text-align: center; margin-left:-10px">
          <div style="width:180px">
            <div style="height: 45px; float:left;">
              <icon name="LOGOicon" scale="3.5" height="45px"></icon>
            </div>
            <div style="height: 45px; float:left;">
              <span style="font-size: 15px; font-weight:bold; margin-left:0px; color:#FFF">DNS日志分析系统</span>
            </div>
          </div>
          <div style="height: 45px; float:left; margin-left:20px">
            <icon name="open" id="right" scale="1.5" style="height: 45px; cursor: pointer;" @click.native="collapse"></icon>
          </div>
        </div>
        <div style="float:right">
          <el-badge is-dot class="item" style="margin-right:10px" :hidden=true>
            <el-button class="share-button" size="small" style="padding:5px 5px; background-color:#C12E34; border: 0px;"><icon name="avatar" scale="2"></icon></el-button>
          </el-badge>
        <el-dropdown @command="handleCommand">
            <span class="el-dropdown-link">
              {{ username }}<i class="el-icon-arrow-down el-icon--right"></i>
            </span>
            <el-dropdown-menu slot="dropdown" align="center">
              <!-- <el-dropdown-item command="user">个人信息</el-dropdown-item> -->
              <el-dropdown-item command="changePassword">修改密码</el-dropdown-item>
              <el-dropdown-item command="quit">退出</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
        </div>
      </el-header>

      <el-container>
        <div style="background-color: #25374F; position:relative; height:calc(100vh - 45px);">
          <el-menu
            id = "menu"
            class="el-menu-vertical-demo"
            :router="true"
            :unique-opened="false"
            :default-active=default_active
            style="background-color: #25374F; border:0px; "
            :collapse="isCollapse"
            active-text-color="#FFF"
            background-color="#25374F"
            text-color="#FFF">

<!--             <el-menu-item index="/dns-dashboard" v-if="dashboardShow">
              <icon name="dashboard" scale="1.8" style="padding-right: 5px"></icon>
              <span slot="title">Dashboard</span>
            </el-menu-item> -->

<!--             <el-submenu index="1" v-if="devicemanageShow || conconfigCompareShow">
              <template slot="title">
                <icon name="audit" scale="1.8" style="padding-right: 5px;"></icon>
                <span slot="title">日志审计</span>
              </template>
              <el-menu-item index="/audit-devicemanage" v-if="devicemanageShow">审计设备管理</el-menu-item>
              <el-menu-item index="/audit-configcompare" v-if="configCompareShow">配置变更查询</el-menu-item>
            </el-submenu>
            <el-menu-item index="/audit-log" v-if="logShow">
              <icon name="log" scale="1.8" style="padding-right: 5px"></icon>
              <span slot="title">操作记录审计</span>
            </el-menu-item>
            <el-menu-item index="user" v-if="userShow">
              <icon name="user" scale="1.8" style="padding-right: 5px"></icon>
              <span slot="title">用户管理</span>
            </el-menu-item> -->

            <el-menu-item index="/dns-dashboard" v-if="dashboardShow">
              <icon name="dashboard" scale="1.8" style="padding-right: 5px"></icon>
              <span slot="title">Dashboard</span>
            </el-menu-item>
            <el-menu-item index="/dns-topn" v-if="topnShow">
              <icon name="TopN" scale="1.8" style="padding-right: 5px"></icon>
              <span slot="title">TOPN域名分析</span>
            </el-menu-item>
            <el-menu-item index="/dns-resourceanalysis" v-if="resourceAnalysisShow">
              <icon name="resource" scale="1.8" style="padding-right: 5px"></icon>
              <span slot="title">资源分布分析</span>
            </el-menu-item>
            <el-menu-item index="/dns-cdnanalysis" v-if="cdnAnalysisShow">
              <icon name="cdn" scale="1.8" style="padding-right: 5px"></icon>
              <span slot="title">CDN分析</span>
            </el-menu-item>
            <el-menu-item index="/dns-industry" v-if="industryShow">
              <icon name="industry" scale="1.8" style="padding-right: 5px"></icon>
              <span slot="title">重点行业分析</span>
            </el-menu-item>
            <el-submenu index="1" v-if="keyDomainShow || keyDomainManageShow">
              <template slot="title">
                <icon name="domain" scale="1.8" style="padding-right: 5px;"></icon>
                <span slot="title">重点域名分析</span>
              </template>
              <el-menu-item index="/dns-keydomain" v-if="keyDomainShow">重点域名展示</el-menu-item>
              <el-menu-item index="/dns-keydomainmanage" v-if="keyDomainManageShow">重点域名管理</el-menu-item>
            </el-submenu>
            <el-submenu index="2" v-if="ipInverseQueryShow || beianSearchShow">
              <template slot="title">
                <icon name="search" scale="1.8" style="padding-right: 5px;"></icon>
                <span slot="title">多维度查询</span>
              </template>
              <el-menu-item index="/dns-ip-inverse-query" v-if="ipInverseQueryShow">IP地址反查</el-menu-item>
              <el-menu-item index="/dns-beiansearch" v-if="beianSearchShow">备案信息查询</el-menu-item>
            </el-submenu>
            <el-submenu index="3" v-if="customerFeaturesShow || customerManageShow">
              <template slot="title">
                <icon name="draw" scale="1.8" style="padding-right: 5px;"></icon>
                <span slot="title">专线用户分析</span>
              </template>
              <el-menu-item index="/dns-features" v-if="customerFeaturesShow">专线用户画像</el-menu-item>
              <el-menu-item index="/dns-customer-manage" v-if="customerManageShow">专线用户管理</el-menu-item>
              <el-menu-item index="/dns-industrial-internet" v-if="customerManageShow">工业互联网分析</el-menu-item>
            </el-submenu>
            <el-menu-item index="/show" v-if="showShow">
              <icon name="screen" scale="1.7" style="padding-right: 5px; margin-left:-1px"></icon>
              <span slot="title">大屏展示</span>
            </el-menu-item>
            <el-menu-item index="/user" v-if="userShow">
              <icon name="user" scale="1.8" style="padding-right: 5px"></icon>
              <span slot="title">用户管理</span>
            </el-menu-item>
<!--             <el-menu-item index="/test" v-if="userShow">
              <icon name="user" scale="1.8" style="padding-right: 5px"></icon>
              <span slot="title">测试</span>
            </el-menu-item> -->
          </el-menu>
        </div>
        <el-container>
          <el-main style="overflow:auto; height:calc(100vh - 45px); width:180px;">
            <transition name="fade" mode="out-in">
              <router-view></router-view>
            </transition>
          </el-main>
        </el-container>
      </el-container>
    </el-container>

    <el-dialog title="修改密码" :visible.sync="dialogChangePasswordFormVisible" width="40%" :close-on-click-modal=false>
      <el-row :gutter="10">
        <el-col :sm="24" :md="24" :lg="24">
          <el-form ref="changePasswordForm" :model="changePasswordForm" label-width="80px" :rules="changePasswordRules">
            <el-form-item label="旧密码" prop="oldPassword">
              <el-input v-model="changePasswordForm.oldPassword" size="small" type="password"></el-input>
            </el-form-item>
            <el-form-item label="新密码" prop="newPassword">
              <el-input v-model="changePasswordForm.newPassword" size="small" type="password"></el-input>
            </el-form-item>
            <el-form-item label="确认密码" prop="confirmPassword">
              <el-input v-model="changePasswordForm.confirmPassword" size="small" type="password"></el-input>
            </el-form-item>
          </el-form>
        </el-col>
      </el-row>
      <el-row>
        <div style="text-align:center;">
          <el-button type="primary" @click="onChangePasswordSubmit" size="small">确定</el-button>
          <el-button size="small" @click="cancelChangePasswordForm">取消</el-button>
        </div>
      </el-row>
    </el-dialog>
  </div>
</template>

<script>
  import { restful_path } from './util.js'
  export default {
    data() {
      return {
        id: '',
        username: '',
        openeds: ['2'],
        isCollapse:false,
        default_active: '/dashboard',
        deg: 0,

        dashboardShow: false,
        topnShow: false,
        resourceAnalysisShow: false,
        cdnAnalysisShow: false,
        industryShow: false,
        keyDomainShow: false,
        keyDomainManageShow: false,
        ipInverseQueryShow: false,
        beianSearchShow: false,
        customerManageShow: false,
        customerFeaturesShow: false,
        showShow: false,
        userShow: false,

        dialogChangePasswordFormVisible:false,
        changePasswordForm: {
          oldPassword:'',
          newPassword:'',
          confirmPassword:''
        },
        changePasswordRules: {
          oldPassword:[{ required: true, message: '请输入旧密码' }],
          newPassword:[{ required: true, message: '请输入新密码' }],
          confirmPassword:[{ required: true, message: '请确认新密码' }]
        }
      }
    },
    //props: ['isCollapse'],
    methods: {
      showInfo () {
        this.$http({
          method: 'get',
          url: restful_path + '/api/user'
        }).then((response) => {
            if(response.data.status){
              this.username = response.data.data.name;
              this.id = response.data.data.id;
            }
          }
        ).catch(error => {
          console.log(error);
        });
      },

      showMenu () {
        let menuArr = sessionStorage.getItem('privilege');
        if(menuArr.indexOf('/dns-dashboard') != -1){ this.dashboardShow = true; }
        if(menuArr.indexOf('/dns-topn') != -1){ this.topnShow = true; }
        if(menuArr.indexOf('/dns-resourceanalysis') != -1){ this.resourceAnalysisShow = true; }
        if(menuArr.indexOf('/dns-cdnanalysis') != -1){ this.cdnAnalysisShow = true; }
        if(menuArr.indexOf('/dns-industry') != -1){ this.industryShow = true; }
        if(menuArr.indexOf('/dns-keydomain') != -1){ this.keyDomainShow = true; }
        if(menuArr.indexOf('/dns-keydomainmanage') != -1){ this.keyDomainManageShow = true; }
        if(menuArr.indexOf('/dns-ip-inverse-query') != -1){ this.ipInverseQueryShow = true; }
        if(menuArr.indexOf('/dns-beiansearch') != -1){ this.beianSearchShow = true; }
        if(menuArr.indexOf('/dns-customer-manage') != -1){ this.customerManageShow = true; }
        if(menuArr.indexOf('/dns-features') != -1){ this.customerFeaturesShow = true; }
        if(menuArr.indexOf('/show') != -1){ this.showShow = true; }
        if(menuArr.indexOf('/user') != -1){ this.userShow = true; }
      },

      selectItem() {
        this.default_active = this.$route.path;
      },

      collapse() {
        this.isCollapse = !this.isCollapse;
        this.$store.dispatch('change');
        this.deg += 90;
        document.getElementById("right").style.transform = "rotate(" + this.deg + "deg)";
      },

      logout() {
        this.$router.push({path:'/login'});
        this.$lockr.rm('token')
      },

      changePassword() {
        this.dialogChangePasswordFormVisible = true;
        //this.$refs.changePasswordForm.resetFields();
        console.log(this.id)
      },

      onChangePasswordSubmit() {
        this.$refs.changePasswordForm.validate((valid) => {
          if(valid){
            //console.log(this.id)
            //let para = Object.assign({}, this.changePasswordForm);
            let crypto = require('crypto');
            let oldPassword = this.changePasswordForm.oldPassword;
            let old_password_hash = crypto.createHash('sha1').update(oldPassword).digest('hex');
            let newPassword = this.changePasswordForm.newPassword;
            let new_password_hash = crypto.createHash('sha1').update(newPassword).digest('hex');
            let confirmPassword = this.changePasswordForm.confirmPassword;
            let confirm_password_hash = crypto.createHash('sha1').update(confirmPassword).digest('hex');
            this.$http({
              method: 'post',
              url: restful_path + '/api/change-password',
              data: {
                'id': this.id,
                'oldPassword': old_password_hash,
                'newPassword': new_password_hash,
                'confirmPassword': confirm_password_hash
              }
            }).then((response) => {
              if (response.data.status){
                this.$message({ type: 'success', message: '修改密码成功!' });
                this.dialogChangePasswordFormVisible = false;
                this.$refs.changePasswordForm.resetFields();
              } else {
                if(response.data.data != ""){
                  this.$message({ type: 'error', message: response.data.data });
                } else {
                  this.$message({ type: 'error', message: '修改密码失败!' });
                }
              }
            }).catch(error => {
              //console.log(error);
            });
          }
        })
      },

      cancelChangePasswordForm() {
        this.dialogChangePasswordFormVisible = false;
        this.$refs.changePasswordForm.resetFields();
      },

      handleCommand(command){
        if(command == 'quit'){
          this.logout()
        } else if(command == 'changePassword'){
          this.changePassword()
        } else if(command == 'user'){
          this.logout()
        }

      }
    },
    created () {
      this.showInfo();
      this.showMenu();
      //this.getRoute();
    },
    mounted () {
      this.showMenu();
      //this.showInfo();
      this.selectItem();
    }
  }
</script>

<style lang="scss" scoped>

  ::-webkit-scrollbar {
    width: 8px;
    height: 0px;
  }
  ::-webkit-scrollbar-thumb {
    border-radius: 5px;
    //-webkit-box-shadow: inset 0 0 3px rgba(0,0,0,0.3);
    //background: rgba(255,255,255,0.3);
    background: #D6D8DD
  }
/*   ::-webkit-scrollbar
  {
    width: 10px;
  } */

  #app {
    height: 100%;
  }

  html, body {
    margin: 0;
    height: 100%;
  }

  .el-header {
    line-height: 45px;
  }
  .el-menu-item {
    height:45px;
    line-height:43px;
  }

  .el-menu-item.is-active {
    //background-color: #E43C59!important;
    background-color:#C12E34!important;
  }

  .el-submenu {
    .el-menu-item {
      min-width: 100px;
    }
  }

  ul > li.el-submenu > ul > li.el-submenu > ul > li {
    margin-left:-20px;
  }

  .el-menu--horizontal .el-submenu>.el-menu {
    height:45px;
  }
  .el-dropdown-link {
    cursor: pointer;
    color:#FFF;
  }
  .el-icon-arrow-down {
    font-size: 12px;
  }
  .el-menu-vertical-demo:not(.el-menu--collapse) {
      width: 180px;
  }
  .el-menu--collapse {
    width: 52px;
    margin-left:-5px;
  }

</style>

<style lang="scss">
  .el-submenu__title {
    height: 45px;
    line-height:43px;
  }
  .el-menu--horizontal .el-submenu .el-submenu__title {
    height:45px;
    line-height:43px;
  }
  .el-badge__content.is-fixed.is-dot {
    top:5px;
  }
  .el-dialog__title {
    font-size: 16px;
  }
  .el-form-item__label {
    font-size: 13px;
  }
/*   .el-table {
    th {
      background-color: #FFA940;
      color: #FFF;
    }
    td {
      background-color: #FCFCFC;
    }
  } */
</style>