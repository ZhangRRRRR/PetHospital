<template>
  <div>
    <PHHeader></PHHeader>
    <p>您的学习的知识和技能将成为他们唯一的依靠</p>
    <button v-on:click="logOut()">登出</button>
    <button v-on:click="jumpToPage('PHGuidingPage')">医院导览</button>
    <PHFooter></PHFooter>
  </div>
</template>

<script>
import PHHeader from '../components/PHHeader.vue'
import PHFooter from '../components/PHFooter.vue'
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
