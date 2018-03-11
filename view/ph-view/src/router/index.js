import Vue from 'vue'
import Router from 'vue-router'
import MainPage from '@/page/MainPage'
import LoginPage from '@/page/LoginPage'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'MainPage',
      component: MainPage
    },
    {
      path: '/login',
      name: 'LoginPage',
      component: LoginPage
    }
  ]
})
