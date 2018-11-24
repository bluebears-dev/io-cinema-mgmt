// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Vuetify from 'vuetify'
import router from './router'
import store from './store'

Vue.use(Vuetify, {
  options: {
    customProperties: true,
  },
  theme: {
    gold: "#deb853",
    charcoal: "#373737",
    black: "#101010",
    white: "#fffffe"
  }
})
Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>'
})
