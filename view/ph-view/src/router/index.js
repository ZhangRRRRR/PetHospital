import Vue from 'vue'
import Router from 'vue-router'
import MainPage from '@/page/MainPage'
import LoginPage from '@/page/LoginPage'
import PHGuidingPage from '@/page/PHGuidingPage'
import PHGuidingDetail from '@/page/PHGuidingDetail'
import CaseLearningPage from '@/page/CaseLearningPage'
import RolePlayPage from '@/page/RolePlayPage'
import DutyLearningPage from '@/page/DutyLearningPage'
import DeseaseSeriesDetail from '@/page/deseaseSeriesDetail'
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
    },
    {
      path: '/dutylearning',
      name: 'DutyLearningPage',
      component: DutyLearningPage
    },
    {
      path: '/caselearning',
      name: 'CaseLearningPage',
      component: CaseLearningPage
    },
    {
      path: '/roleplay',
      name: 'RolePlayPage',
      component: RolePlayPage
    },
    {
      // 病种
      path: '/deseaseseries/:id',
      name: 'DeseaseSeriesDetail',
      component: DeseaseSeriesDetail
    }
  ]
})
