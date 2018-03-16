<template>
  <div>
    <p>role play</p>
    <ul>
      <li v-for="role in rolePlaysData.roles" :key="role.id">
        <router-link :to="'/role/' + role.id">
          <p v-bind:title="role.description">{{role.name}}</p>
        </router-link>
      </li>
    </ul>
    <button v-on:click="logOut()">登出</button>
    <button v-on:click="jumpToPage('WelcomePage')">回到主页</button>
  </div>
</template>

<script>
export default {
  data () {
    return {
      rolePlaysData: {
        'roles': [
          {'id': '000001', 'name': '狗狗鸡儿的小天使', 'description': '帮狗狗换尿布'},
          {'id': '000002', 'name': 'ROLE2', 'description': 'this is role 2'},
          {'id': '000003', 'name': 'ROLE3', 'description': 'this is role 3'}
        ]
      }
    }
  },
  methods: {
    created () {
      this.checkLogin()
      this.getRolePlaysData()
    },
    getRolePlaysData () {
      // axios
    },
    checkLogin () {
      var isAlreadyLogin = this.$api.checkLoginStatus()
      if (isAlreadyLogin === true) {
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
