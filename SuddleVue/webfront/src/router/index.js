import Vue from 'vue'
import Router from 'vue-router'
import one from '@/pages/one'
import index from '@/pages/index'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'index',
      component: index
    },
    {
      path: '/one',
      name: 'one',
      component: one
    }
  ]
})
