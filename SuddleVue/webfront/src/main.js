// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import MintUI from 'mint-ui'
import 'mint-ui/lib/style.css'
import axios from 'axios'
import scss from 'scss'
import '@/assets/icon/iconfont.css'



Vue.prototype.$sudleurl="http://192.168.123.130:8080/api"
Vue.prototype.$axios = axios
Vue.use(MintUI)
Vue.config.productionTip = false
Vue.use(ElementUI)
Vue.use(scss)
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
