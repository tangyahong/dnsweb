// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import ElementUI from 'element-ui'
import axios from 'axios'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App'
import router from './router'
import echarts from 'echarts'
/* import Vuex from 'vuex' */
import store from './store'
import Blob from './vendor/Blob'
import Export2Excel from './vendor/Export2Excel'
import VueWechatTitle from 'vue-wechat-title'
import Lockr from 'lockr'
import 'normalize.css'
import Icon from 'vue-svg-icon/Icon.vue'
import 'babel-polyfill'

Vue.use(ElementUI);
Vue.use(VueWechatTitle);
Vue.component('icon', Icon);
Vue.prototype.$http = axios;
Vue.prototype.$echarts = echarts;
Vue.prototype.$lockr = Lockr;

//http request拦截器
axios.interceptors.request.use(
  config => {
    if (store.state.authModule.token) {
      config.headers.Authorization = `Bearer ${store.state.authModule.token}`;
    }
    return config;
  }, error => {
    return Promise.reject(error);
  }
)

//http request拦截器
axios.interceptors.request.use(
  config => {
    let token = localStorage.getItem('token')
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  }, error => {
    return Promise.reject(error);
  }
)

new Vue({
  el: '#app',
  router,
  axios,
  store,
  render: h => h(App)
});
