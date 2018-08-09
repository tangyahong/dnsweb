import Vue from 'vue'
import Router from 'vue-router'
import store from '../store'
import { restful_path } from '../components/util.js'

Vue.use(Router);

const router = new Router({
  routes: [
    {
      path: '/',
      redirect: '/login'
    },
    {
      path: '/login',
      meta: {
        title: 'DNS日志管理系统'
      },
      component: resolve => require(['../components/Login.vue'], resolve)
    },
    {
      path: '/show',
      component: resolve => require(['../components/show.vue'], resolve)
    },
    {
      path: '/show-topn',
      component: resolve => require(['../components/show_topn.vue'], resolve)
    },
    {
      path: '/dns-industrial-internet',
      component: resolve => require(['../components/dashboard_zx.vue'], resolve)
    },
    {
      path: '/index',
      meta: {
        title: 'DNS日志分析系统'
      },
      component: resolve => require(['../components/container.vue'], resolve),
      children: [
        {
          path: '/dns-dashboard',
          component: resolve => require(['../components/dns/dashboard.vue'], resolve)
        },
        {
          path: '/dns-topn',
          component: resolve => require(['../components/dns/topnanalysis.vue'], resolve)
        },
        {
          path: '/dns-resourceanalysis',
          component: resolve => require(['../components/dns/resourceanalysis.vue'], resolve)
        },
        {
          path: '/dns-cdnanalysis',
          component: resolve => require(['../components/dns/cdnanalysis.vue'], resolve)
        },
        {
          path: '/dns-industry',
          component: resolve => require(['../components/dns/industry.vue'], resolve)
        },
        {
          path: '/dns-keydomain',
          component: resolve => require(['../components/dns/keydomain.vue'], resolve)
        },
        {
          path: '/dns-keydomainmanage',
          component: resolve => require(['../components/dns/keydomainmanage.vue'], resolve)
        },
        {
          path: '/dns-ip-inverse-query',
          component: resolve => require(['../components/dns/ipinversequery.vue'], resolve)
        },
        {
          path: '/dns-beiansearch',
          component: resolve => require(['../components/dns/beiansearch.vue'], resolve)
        },

        {
          path: '/dns-features',
          component: resolve => require(['../components/dns/features.vue'], resolve)
        },
        {
          path: '/dns-customer-manage',
          component: resolve => require(['../components/dns/customermanage.vue'], resolve)
        },
        {
          path: '/user',
          component: resolve => require(['../components/dns/user.vue'], resolve)
        },
        {
          path: '/test',
          component: resolve => require(['../components/dns/test.vue'], resolve)
        }

      ]
    }
  ]
})

/* router.beforeEach((to, from, next) => {
  if(to.meta.requireAuth){
    if (localStorage.getItem('isAuthenticated') && localStorage.getItem('token')) {
    //if (store.state.authModule.isAuthenticated) {
      next();
    } else{
      next({
        path: '/login',
        query: {redirect: to.fullPath}
      })
    }
  } else {
    next();
  }
}) */

router.beforeEach((to, from, next) => {
  if (to.meta.requireAuth) {
    if (localStorage.getItem('token')) {
      axios({
        method: 'get',
        url: restful_path + '/api/user'
      }).then((response) => {
        if (response.data.status) {
          //getRoute();
          next();
        } else {
          next({
            path: '/login',
            query: { redirect: to.fullPath }
          })
        }
      })
    } else {
      next('/login');
    }
  } else {
    next()
  }
})

export default router


function requireAuth(to, from, next) {
  axios({
    method: 'get',
    url: restful_path + '/api/identify-menu'
  }).then((response) => {
    if (response.data.data.indexOf(to.path) != -1) {
      sessionStorage.setItem('privilege', response.data.data);
      next()
    }
    else { next('*') }
  })
}