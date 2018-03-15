<template>
  <div>
    <PHHeader></PHHeader>
      <button v-on:click="logOut()">登出</button>
      <button v-on:click="jumpToPage('RolePlayPage')">角色扮演</button>
      <button v-on:click="jumpToPage('CaseLearningPage')">病例学习</button>
      <button v-on:click="jumpToPage('MainPage')">回到主页</button>
    <PHFooter></PHFooter>
  </div>
</template>

<script>
import PHHeader from '../../components/PHHeader.vue'
import PHFooter from '../../components/PHFooter.vue'
export default {
  components: { PHHeader, PHFooter },
  data () {
    return {
    }
  },
  created () {
    this.checkLogin()
  },
  methods: {
    checkLogin () {
      var isAlreadyLogin = this.$api.checkLoginStatus()
      if (isAlreadyLogin === true) {
        // do nothing
      } else {
        this.login()
      }
    },
    login () {
      this.$router.push({
        name: 'LoginPage',
        params: {
          jumpFromPage: 'MainPage'
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
