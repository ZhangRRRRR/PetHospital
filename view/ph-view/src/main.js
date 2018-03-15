// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'

import './style/fonts/glyphicons-halflings-regular.eot'
import './style/fonts/glyphicons-halflings-regular.svg'
import './style/fonts/glyphicons-halflings-regular.ttf'
import './style/fonts/glyphicons-halflings-regular.woff'
import './style/fonts/glyphicons-halflings-regular.woff2'
import './style/css/bootstrap.css'
import VueVideoPlayer from 'vue-video-player'
import 'video.js/dist/video-js.css'

import api from './api/index.js'
Vue.use(VueVideoPlayer)

Vue.prototype.$api = api

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
