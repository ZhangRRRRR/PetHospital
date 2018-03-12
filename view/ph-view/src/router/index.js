import Vue from 'vue'
import Router from 'vue-router'
import MainPage from '@/page/MainPage'
import LoginPage from '@/page/LoginPage'
import PHGuidingPage from '@/page/PHGuidingPage'
import PHGuidingDetail from '@/page/PHGuidingDetail'

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
    },
    {
      path: '/phguiding',
      name: 'PHGuidingPage',
      component: PHGuidingPage
    },
    {
      path: '/phguiding/:id',
      name: 'PHGuidingDetail',
      component: PHGuidingDetail
    }
  ]
})
