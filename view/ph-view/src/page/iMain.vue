<style scoped>
  .layout{
    border: 1px solid #d7dde4;
    background: #f5f7f9;
    position: relative;
    border-radius: 4px;
    overflow: hidden;
  }
  .layout-logo{
    width: 100px;
    height: 30px;
    background: #5b6270;
    border-radius: 3px;
    float: left;
    position: relative;
    top: 15px;
    left: 20px;
  }
  .layout-nav{
    width: 600px;
    margin: 0 auto;
    margin-right: 20px;
  }
  .layout-footer-center{
    text-align: center;
  }
</style>
<template>
  <div class="layout">
    <Layout>
      <Header >
        <Menu mode="horizontal" theme="dark"  @on-select="jumpToPage">
          <div class="layout-logo"></div>
          <div class="layout-nav">
            <MenuItem name="WelcomePage" >
              <Icon type="ios-navigate"></Icon>
              回到首页
            </MenuItem>
            <MenuItem name="PHGuidingPage" >
              <Icon type="ios-navigate"></Icon>
              3D导览
            </MenuItem>
            <MenuItem name="DutyLearningPage">
              <Icon type="ios-keypad"></Icon>
              职能学习
            </MenuItem>
            <MenuItem name="3">
              <Icon type="ios-analytics"></Icon>
              测试
            </MenuItem>
            <Submenu name="4">
              <template slot="title">
                <Icon type="stats-bars"></Icon>
                用户中心
              </template>
              <MenuItem name="UserCenter">
                用户中心
              </MenuItem>
              <MenuItem name="logout">
                登出
              </MenuItem>
            </Submenu>
          </div>
        </Menu>
      </Header>
      <Content :style="{margin: '88px 20px 0', background: '#fff', minHeight: '500px'}">
        <router-view/>
      </Content>
      <Footer class="layout-footer-center">2011-2016 &copy; TalkingData</Footer>
    </Layout>
  </div>
</template>
<script>
export default {
  components: {},
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
      console.log(pageName)
      if (pageName === 'logout') {
        this.logOut()
      } else {
        this.$router.push({
          name: pageName
        })
      }
    },
    logOut () {
      this.$api.setLoginStatus('LOGOUT')
      this.jumpToPage('LoginPage')
    }
  }
}
</script>
