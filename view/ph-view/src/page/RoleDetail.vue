<template>
  <div>

  </div>
</template>

<script>
export default {
  data () {
    return {
      id: this.$route.params.id,
      rolePlayData: {
        'name': '换尿布',
        'description': '帮狗狗换尿布',
        'medias': [
          {
            'id': '000001',
            'imgUrls': [
              {'url': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1521130491201&di=4033099fdf0035ddd698a1774a8e2315&imgtype=0&src=http%3A%2F%2Fi0.hdslb.com%2Fbfs%2Farchive%2F7d3988de8b469e567b8253680afc99d028ad2b0e.jpg'},
              {'url': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1521130491200&di=c43028d180e7797c068faab9675e9ab4&imgtype=0&src=http%3A%2F%2Fww1.sinaimg.cn%2Flarge%2Fc5a9b5efjw1e673b3mofkj20go0d6my7.jpg'},
              {
                'url': 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1521130491200&di=3a2a1e0f8d6383e333389642a39f244e&imgtype=0&src=http%3A%2F%2Fimgsrc.baidu.com%2Fforum%2Fw%3D580%2Fsign%3Df401aa2cc2ef76093c0b99971edca301%2Fb46f0223dd54564e6aad4a88bade9c82d0584f77.jpg'
              }
            ],
            'words': [
              {'word': 'you are the most beautiful girl in this world'},
              {'word': 'you are the most handsome boy in this fucking deep dark fantacy dormitory, leather man'}
            ],
            'videoUrls': [
              {'url': ''}
            ]
          }
        ]
      }
    }
  },
  methods: {
    created () {
      this.checkLogin()
      this.getCurrRoleData()
    },
    getCurrRoleData () {
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
