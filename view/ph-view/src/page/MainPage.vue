<template>
  <div>
    <p>good</p>
  </div>
</template>

<script>
export default {
  data () {
    return {
      message: ''
    }
  },
  created () {
    this.checkLogin()
  },
  methods: {
    checkLogin () {
      var isAlreadyLogin = this.$api.checkLoginStatus()
      if (isAlreadyLogin === true) {
        // do something
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
    }
  }
}
</script>
