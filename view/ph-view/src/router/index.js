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
import RoleDetail from '@/page/RoleDetail'
import UserCenter from '@/page/UserCenter/UserCenter'
import ManageMain from '@/page/ManageCenter/ManageMain'
Vue.use(Router)

export default new Router({
  routes: [
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
        },
        {
          path: '/roleplay',
          name: 'RolePlayPage',
          component: RolePlayPage
        },
        {
          path: '/role/:id',
          name: 'RoleDetail',
          component: RoleDetail
        },
        {
          path: '/usercenter',
          name: 'UserCenter',
          component: UserCenter
        }
      ]
    },
    {
      path: '/managecenter',
      name: 'ManageMain',
      component: ManageMain,
      children: []
    },
    {
      path: '/login',
      name: 'LoginPage',
      component: LoginPage
    }
  ]
})
