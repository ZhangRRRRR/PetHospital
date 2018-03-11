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
  methods: {
    login () {
      this.$api.post('jsondemo/login', {
        username: this.username,
        password: this.password},
      r => {
        if (r.success === 'TRUE') {
          this.$api.setLoginStatus('LOGIN')
          console.log('true')
          this.returnToFromPage()
        } else {
          this.$api.setLoginStatus('LOGOUT')
          this.responseMessage = '登陆失败, 请核对您的用户名和密码'
        }
      }, r => {
        this.responseMessage = '网络问题请重试'
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
    }
  }
}
</script>
