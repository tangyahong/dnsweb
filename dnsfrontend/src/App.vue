<template>
  <div id="app">
    <router-view v-wechat-title="$route.meta.title"></router-view>
  </div>
</template>

<script>
/*  import container from './components/Container.vue'
  import home from './components/Home.vue'*/
  export default {
    name: 'app',
    components: {
    }
  }
</script>

<style>
/*   #app {
     font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center; 
    color: #2c3e50; 
  } */
</style>
