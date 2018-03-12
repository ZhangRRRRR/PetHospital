<template>
  <div>
    <PHHeader></PHHeader>
    <p>医院导览</p>
    <p>{{ welcomeMessage }}</p>
    <ul>
      <li v-for= "department in departmentList" :key= "department.id">
        <router-link :to="'/phguiding/' + department.id">
            {{ department.name }}
        </router-link>
      </li>
    </ul>
    <button v-on:click="logOut()">登出</button>
    <button v-on:click="jumpToPage('MainPage')">回到主页</button>
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
      welcomeMessage: '',
      departmentList: []
    }
  },
  created () {
    this.checkLogin()
    this.getDepartmentList()
  },
  methods: {
    getDepartmentList () {
      this.$api.get('intros', null, r => {
        this.departmentList = r.departments
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
