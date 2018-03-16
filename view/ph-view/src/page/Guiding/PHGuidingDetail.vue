<template>
  <div>
    <p>正在浏览: {{ departmentData.departmentName }}</p>
    <p>{{ departmentData.position }}</p>
    <p>{{ departmentData.usage }}</p>
    <p>{{ departmentData.description }}</p>
    <button v-on:click="logOut()">登出</button>
    <button v-on:click="jumpToPage('PHGuidingPage')">查看其它科室</button>
    <button v-on:click="jumpToPage('WelcomePage')">回到主页</button>
  </div>
</template>

<script>
import PHHeader from '../../components/PHHeader.vue'
import PHFooter from '../../components/PHFooter.vue'
export default {
  components: { PHHeader, PHFooter },
  data () {
    return {
      departmentId: this.$route.params.id,
      msg: '',
      departmentData: {}
    }
  },
  created () {
    this.checkLogin()
    this.getDepartmentDetail()
  },
  methods: {
    getDepartmentDetail () {
      this.$api.get('intro/' + this.departmentId, null, r => {
        this.departmentData = r
      })
    },
    checkLogin () {
      var isAlreadyLogin = this.$api.checkLoginStatus()
      if (isAlreadyLogin === true) {
        this.welcomeMessage = '欢迎, 新进干员'
      } else {
        this.login()
      }
    },
    login () {
      this.$router.push({
        name: 'LoginPage',
        params: {
          jumpFromPage: 'WelcomePage'
        }
      })
    },
    jumpToPage (pageName) {
      this.$router.push({
        name: pageName
      })
    },
    logOut () {
      this.$api.setLoginStatus('LOGOUT')
      this.jumpToPage('LoginPage')
    }
  }
}
</script>
