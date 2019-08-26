// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import axios from 'axios'
import $ from 'jquery'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min'
import * as VueGoogleMaps from 'vue2-google-maps'
import VueAxios from 'vue-axios'

Vue.use(VueAxios, axios)

Vue.prototype.$axios = axios
Vue.config.productionTip = false
axios.defaults.headers.post['Content-Type'] = 'application/x-www-fromurlencodeed'

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyAeRMoJJ9yGwCuVVeNqR06I7rvbTz20SW4',
    libraries: 'places'
  }
})


/* eslint-disable no-new */
new Vue({
  el: '#app',
  data: {
    currentRoute: window.location.pathname
  },
  router,
  render: h => h(App)
})
