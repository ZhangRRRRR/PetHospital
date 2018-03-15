import Vue from 'vue'
import Router from 'vue-router'
import MainPage from '@/page/MainPage'
import LoginPage from '@/page/LoginPage'
import PHGuidingPage from '@/page/Guiding/PHGuidingPage'
import PHGuidingDetail from '@/page/Guiding/PHGuidingDetail'
import CaseLearningPage from '@/page/DutyLearning/CaseLearningPage'
import RolePlayPage from '@/page/DutyLearning/RolePlayPage'
import DutyLearningPage from '@/page/DutyLearning/DutyLearningPage'
import DeseaseSeriesDetail from '@/page/DutyLearning/deseaseSeriesDetail'
import iMain from '@/page/iMain'
import WelcomePage from '@/page/WelcomePage'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/Main',
      name: 'MainPage',
      component: MainPage
    },
    {
      path: '/',
      name: 'iMain',
      component: iMain,
      children: [
        {
          path: '',
          name: 'WelcomePage',
          component: WelcomePage
        },
        {
          path: 'profile',
          component: MainPage
        },
        {
          path: 'phguiding',
          name: 'PHGuidingPage',
          component: PHGuidingPage
        },
        {
          path: 'dutylearning',
          name: 'DutyLearningPage',
          component: DutyLearningPage
        },
        {
          path: '/phguiding/:id',
          name: 'PHGuidingDetail',
          component: PHGuidingDetail
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
    },
    {
      path: '/login',
      name: 'LoginPage',
      component: LoginPage
    }
  ]
})
