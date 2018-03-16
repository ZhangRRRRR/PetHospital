<template>
  <div>
    <div class="layout">
      <Layout :style="{minHeight: '100vh'}">
        <Sider collapsible :collapsed-width="78" v-model="isCollapsed">
          <Menu active-name="1-2" theme="dark" width="auto" :class="menuitemClasses" @on-select="jumpToPage">
            <MenuItem name="TestLibrary">
              <Icon type="ios-navigate"></Icon>
              <span>题库</span>
            </MenuItem>
            <MenuItem name="MockTest">
              <Icon type="search"></Icon>
              <span>测试</span>
            </MenuItem>
            <MenuItem name="OfficialTest">
              <Icon type="settings"></Icon>
              <span>考试</span>
            </MenuItem>
          </Menu>
        </Sider>
        <Layout>
          <Header :style="{background: '#fff', boxShadow: '0 2px 3px 2px rgba(0,0,0,.1)'}">
            <p style="display: online">题库搜索</p>
            <Button type="ghost" shape="circle" icon="ios-search"></Button>
          </Header>

          <Content :style="{margin: '88px 20px 0', background: '#fff', minHeight: '500px'}">
            <router-view/>
          </Content>
        </Layout>
      </Layout>
    </div>
  </div>
</template>

<script>
// import PHHeader from '../components/PHHeader.vue'
// import PHFooter from '../components/PHFooter.vue'

import {Layout, Header, Content, Footer, Sider} from 'iview'

export default {
  components: {Layout, Header, Content, Footer, Sider},
  data () {
    return {
      isCollapsed: false
    }
  },
  computed: {
    menuitemClasses: function () {
      return [
        'menu-item',
        this.isCollapsed ? 'collapsed-menu' : ''
      ]
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

<style scoped>
  body {
    color: #405685;
  }

  .layout-con {
    height: 100%;
    width: 100%;
  }

  .menu-item span {
    display: inline-block;
    overflow: hidden;
    width: 69px;
    text-overflow: ellipsis;
    white-space: nowrap;
    vertical-align: bottom;
    transition: width .2s ease .2s;
  }

  .menu-item i {
    transform: translateX(0px);
    transition: font-size .2s ease, transform .2s ease;
    vertical-align: middle;
    font-size: 16px;
  }

  .collapsed-menu span {
    width: 0px;
    transition: width .2s ease;
  }

  .collapsed-menu i {
    transform: translateX(5px);
    transition: font-size .2s ease .2s, transform .2s ease .2s;
    vertical-align: middle;
    font-size: 22px;
  }
</style>
