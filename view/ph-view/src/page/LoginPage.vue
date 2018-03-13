<template>
  <div>
    <PHHeader></PHHeader>
    <div class="container-fluid">
      <div class="row">
        <div class="col-xs-7">
          <div class="login_ad_part">
            <transition name="login_ad_top_trans">
              <p v-if="showInput" class="login_ad_top">「磨炼您的技能, 帮助人类的伙伴」</p>
            </transition>
            <img class="login_ad" src = "../../static/img/login_ad_bg.gif"/>
          </div>
        </div>
        <div class="col-xs-5">
          <div class="login_part">
            <p class="title">欢迎光临虚拟宠物医院</p>
            <p class="responseMessage_style">{{responseMessage}}</p>
            <transition name="username_fadein">
              <p v-if="showInput"><input class="inputbox_style" v-model="username" placeholder="用户名" type="text"/></p>
            </transition>
            <transition name="password_fadein">
              <p v-if="showInput"><input class="inputbox_style" v-model="password" placeholder="密码" type="password"/></p>
            </transition>
            <transition name="button_style_trans">
              <button v-if="showInput" class="button_style" v-on:click="login">登录</button>
            </transition>
          </div>
        </div>
      </div>
    </div>
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
      responseMessage: '',
      username: '',
      password: '',
      showInput: false
    }
  },
  created () {
    this.checkLogin()
  },
  mounted () {
    this.showInput = true
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

<style>
.login_ad_top{
  font-size: 30px;
  padding-top: 20px;
  padding-bottom: 15px;
}
.login_ad{
  padding-top: 0px;
  width: 1066px;
  height: 600px;
}
.login_ad_part{
  width: 1066px;
  height: 600px;
  margin-top: 0px;
  margin-left: 10px;
  padding:0px;
}

.login_part{
  margin-left: 35px;
  padding-top: 255px;
  width: 700px;
  height: 700px;
  margin-top: 20px;
  margin-right: 120px;
  background-image: url('../../static/img/login_bg.gif');
  background-size: contain;
  background-repeat: no-repeat;
}
.responseMessage_style{
  font-size: 10px;
  color:red;
}

.title{
  font-size: 2em;
  letter-spacing: 3px;
}

.button_style{
  border: none;
  border-radius: 5px;
  text-decoration: none;
  width: 30%;
  height: 45px;
  margin-top: 5px;
  margin-bottom: 5px;
  font-size: 25px;
  letter-spacing: 2px;
  text-rendering: optimizeLegibility;
}

.button_style:hover{
  background: #bfd7ec;
  font-size: 27px;
  transition: all 0.2s;
}

.inputbox_style {
  background: #405685;
  border: none;
  border-radius: 50px;
  padding: .65em 4em .65em 1em;
  width: 50%;
  height: 45px;
  margin-top: 5px;
  margin-bottom: 5px;
  color: #ffffff;
  font-size: 2em;
  letter-spacing: 2px;
  box-shadow: inset 0 2px 0px rgba(0, 0, 0, 0.1), 0 2px 0px rgba(147, 174, 247, 0.2);
  text-rendering: optimizeLegibility;
}
.inputbox_style:hover{
  background: #5894cc;
  transition: background 0.5s;
}

/* animation here */
.username_fadein-enter-active, .username_fadein-leave-active {
  transition: all 0.5s ease;
}
.username_fadein-enter, .username_fadein-leave-to{
  transform: translateY(10px);
  opacity: 0;
}

.password_fadein-enter-active, .password_fadein-leave-active {
  transition: all 1s ease;
}
.password_fadein-enter, .password_fadein-leave-to{
  transform: translateY(15px);
  opacity: 0;
}

.button_style_trans-enter-active, .button_style_trans-leave-active {
  transition: all 1.5s ease;
}
.button_style_trans-enter, .button_style_trans-leave-to{
  transform: translateY(20px);
  opacity: 0;
}

.login_ad_top_trans-enter-active, .login_ad_top_trans-leave-active {
  transition: all 0.5s ease;
}
.login_ad_top_trans-enter, .login_ad_top_trans-leave-to{
  transform: translateX(100px);
  opacity: 0;
}
</style>
