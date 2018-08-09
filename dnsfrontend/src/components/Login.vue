<template>
  <div class="login-container">
    <!--<div class="ms-title">后台管理系统</div>-->
    <div class="ms-login">
      <h3 class="title">DNS日志分析系统</h3>
      <el-form :model="loginForm" :rules="rules" ref="loginForm">
        <el-form-item prop="username">
          <el-input v-model="loginForm.username" placeholder="用户名"></el-input>
        </el-form-item>
        <el-form-item prop="password">
          <el-input type="password" placeholder="密码" v-model="loginForm.password" @keyup.enter.native="submitForm('loginForm')"></el-input>
        </el-form-item>
        <div class="login-btn">
          <el-button type="success" @click="submitForm('loginForm')">登录</el-button>
        </div>
      </el-form>
    </div>
    <div class="foot-login">
      <span class="foot">建议使用Chrome访问系统 Copyright©2017</span>
    </div>
  </div>
</template>

<script>
  import { restful_path } from './util.js'
  export default {
    data: function(){
      return {
        isLogin: false,
        loginForm: {
          username: '',
          password: ''
        },
        rules: {
          username: [
            { required: true, message: '请输入用户名', trigger: 'blur' }
          ],
          password: [
            { required: true, message: '请输入密码', trigger: 'blur' }
          ]
        }
      }
    },
    methods: {
      submitForm(formName) {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            let crypto = require('crypto');
            let password = this.loginForm.password;
            let password_hash = crypto.createHash('sha1')
              .update(password).digest('hex');
            this.$http({
              method: 'post',
              url: restful_path + '/api/login',
              data: {
                'username': this.loginForm.username,
                'password': password_hash
              }
            }).then((response) => {
                if(response.data.status){
                  localStorage.setItem('token',response.data.data);
                  this.$message({
                    type: 'success',
                    message: '登录成功！'
                  });
                  this.$http({
                    method:'get',
                    url:restful_path + '/api/identify-menu'
                  }).then((response) => {
                      sessionStorage.setItem('privilege', response.data.data);
                      if(response.data.data.indexOf('/dns-dashboard') != -1) {
                        setTimeout(() => { this.$router.push('/dns-dashboard');}, 1000);
                      } else{
                        setTimeout(() => { this.$router.push('/index');}, 1000);
                      }
                  })
                } else {
                  this.$message({
                    type: 'error',
                    message: '用户名或密码错误!'
                  });
                  this.$lockr.rm('token');
                }
              }
            ).catch(error => {
              //console.log(error);
            });
          } else {
            return false;
          }
        });
      }
    }
  }
</script>

<style scoped>
  @import '../assets/normalize.css';
  body {
    margin: 0;
  } 
  .login-container{
    text-align: center;
    position: absolute;
    width:100%;
    height:100%;
    background-image: url('../assets/background3.jpg');
    background-repeat: no-repeat;
    background-size: 100% 100%
  }
  .title {
    color: #FCFCFC;
    text-align: center;
    font-size: 24px;
  }
  .ms-login{
    display: inline-block;
    width:300px;
    height:160px;
    margin: 0 auto;
    margin-top: 15%;
    border-radius: 5px;
  }
  .login-btn{
    text-align: center;
  }
  .login-btn button{
    width:100%;
    height:36px;
  }
  .foot-login {
    position: absolute;
    left: 0;
    right: 0;
    bottom: 5%;
  }
  .foot {
    font-size: 12px;
    color: #FCFCFC;
  }
</style>