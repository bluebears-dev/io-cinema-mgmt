// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import Vuetify from 'vuetify'
import '@mdi/font/css/materialdesignicons.css'

import cookie from './utils/cookie'
import App from './App'
import router from './router'
import store from './store'

Vue.use(Vuetify, {
  options: {
    customProperties: true,
    iconfont: 'mdi'
  },
  theme: {
    gold: '#DEB853',
    sand: '#B9AC81',
    charcoal: '#373737',
    black: '#101010',
    white: '#F4F4F4',
    bronze: '#292518'
  },
  iconfont: 'mdi'
})
Vue.config.productionTip = false

Vue.prototype.$cookie = cookie
/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: {App},
  template: '<App/>'
})
