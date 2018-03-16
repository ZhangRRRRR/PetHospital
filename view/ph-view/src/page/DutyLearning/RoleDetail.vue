<template>
  <div>
    <p>{{rolePlayData.name}}</p>
    <p>{{rolePlayData.description}}</p>
    <ul>
      <li v-for="detail in rolePlayData.details" :key="detail.id">
        <button  v-on:click="showDetailMedia(detail.id)" v-bind:title="detail.description">{{detail.name}}</button>
      </li>
    </ul>
    <ul v-show="isShowWords">
      <li v-for="word in wordsMessage" :key="word.word">
        <p>{{word.word}}</p>
      </li>
    </ul>
    <button v-show="isShowPicture" v-on:click="showImages()">相关图片 {{pictureCount}} 张</button>
    <button v-show="isShowVideo" v-on:click="showVideo()">相关视频 {{videoCount}} 段</button>
    <ImageViewer v-show="isShowImageViewer" :urls="imageViewerUrls"></ImageViewer>
    <VideoViewer v-show="isShowVideoViewer" :urls="videoViewerUrls"></VideoViewer>
  </div>
</template>

<script>
import ImageViewer from '../../components/ImageViewer.vue'
import VideoViewer from '../../components/VideoViewer.vue'
export default {
  components: { ImageViewer, VideoViewer },
  data () {
    return {
      id: this.$route.params.id,
      videoCount: 0,
      pictureCount: 0,
      isShowWords: false,
      wordsMessage: [],
      isShowPicture: false,
      isShowVideo: false,
      isShowImageViewer: false,
      imageViewerUrls: [],
      isShowVideoViewer: false,
      videoViewerUrls: [],
      rolePlayData: {
        'name': '换尿布',
        'description': '帮狗狗换尿布',
        'details': [
          {
            'id': '000001',
            'name': '筋脉注射',
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
              {'url': 'http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4'},
              {'url': 'http://www.html5videoplayer.net/videos/toystory.mp4'}
            ]
          },
          {
            'id': '000002',
            'name': '搞比利',
            'imgUrls': [
              {'url': 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=534386446,2383379323&fm=27&gp=0.jpg'},
              {'url': 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3269230542,2079728320&fm=27&gp=0.jpg'},
              {'url': 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3351311726,1166292474&fm=27&gp=0.jpg'},
              {'url': 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1258893326,3098157884&fm=27&gp=0.jpg'}
            ],
            'words': [
              {'word': 'you may want to go to the leather man\'s block'},
              {'word': 'oh fuck you leather man, you may want to fullfill my fantacies, come on, let\'s do this'}
            ],
            'videoUrls': [
              {'url': 'http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4'}
            ]
          }
        ]
      }
    }
  },
  created () {
    this.checkLogin()
    this.getCurrRoleData()
  },
  methods: {
    showDetailMedia (detailId) {
      var details = this.rolePlayData.details
      var alignedId = -1
      for (var i = 0; i !== details.length; i++) {
        var currentId = details[i].id
        if (currentId === detailId) {
          alignedId = i
          break
        }
      }
      if (alignedId === -1) {
        // press button which does not exist, do nothing
      } else {
        var words = details[alignedId].words
        var imgUrls = details[alignedId].imgUrls
        var videoUrls = details[alignedId].videoUrls
        if (words === 'NONE') {
          this.isShowWords = false
        } else {
          this.isShowWords = true
          this.wordsMessage = words
        }
        if (videoUrls === 'NONE') {
          this.isShowVideo = false
        } else {
          this.isShowVideo = true
          this.videoCount = videoUrls.length
          this.videoViewerUrls = videoUrls
        }
        if (imgUrls === 'NONE') {
          this.isShowPicture = false
        } else {
          this.isShowPicture = true
          this.pictureCount = imgUrls.length
          this.imageViewerUrls = imgUrls
        }
      }
    },
    showImages () {
      this.isShowImageViewer = true
      this.unshowVideo()
    },
    showVideo () {
      this.isShowVideoViewer = true
      this.unshowImages()
    },
    unshowImages () {
      this.isShowImageViewer = false
    },
    unshowVideo () {
      this.isShowVideoViewer = false
    },
    getCurrRoleData () {
      // axios use current role id to fetch the whole json
      return true
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
