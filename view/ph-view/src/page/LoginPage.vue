<template>
  <div>
    <p>login here</p>
    <p>{{responseMessage}}</p>
    <input v-model="username" placeholder="用户名" type="text"/>
    <input v-model="password" placeholder="密码" type="password"/>
    <button v-on:click="login">登录</button>
  </div>
</template>

<script>
export default {
  data () {
    return {
      responseMessage: '',
      username: '',
      password: ''
    }
  },
  created () {
    this.checkLogin()
  },
  methods: {
    login () {
      this.$api.post('login', {
        username: this.username,
        password: this.password},
      r => {
        if (r.success === 'TRUE') {
          this.$api.setLoginStatus('LOGIN')
          // jump back to the page which was interrupted
          this.returnToFromPage()
        } else {
          this.$api.setLoginStatus('LOGOUT')
          this.responseMessage = '登陆失败, 请核对您的用户名和密码'
        }
      }, r => {
        this.responseMessage = '网络连接异常请检查网络后重试'
      })
    },
    returnToFromPage () {
      var jumpFromPage = this.$route.params.jumpFromPage
      if (jumpFromPage) {
        this.jumpToPage(jumpFromPage)
      } else {
        this.jumpToPage('MainPage')
      }
    },
    jumpToPage (pageName) {
      this.$router.push({
        name: pageName
      })
    },
    checkLogin () {
      var isAlreadyLogin = this.$api.checkLoginStatus()
      if (isAlreadyLogin === true) {
        this.jumpToPage('MainPage')
      } else {
        // do nothing
      }
    }
  }
}
</script>
