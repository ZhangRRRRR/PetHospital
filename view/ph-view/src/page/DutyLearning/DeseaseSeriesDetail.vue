<template>
  <div>
    <ul>
      <li v-for="deseaseCase in deseaseCasesData.deseaseCases" :key="deseaseCase.id">
        <button v-on:click="showDeseaseCaseDetail()">{{deseaseCase.name}}</button>
      </li>
    </ul>
    <p v-show="isShowDetails">{{detailMessage}}</p>
    <button v-show="isShowPicture" v-on:click="showImages()">相关图片 {{pictureCount}} 张</button>
    <button v-show="isShowVideo" v-on:click="showVideo()">相关视频 {{videoCount}} 段</button>
    <ImageViewer v-show="isShowImageViewer" :urls="imageViewerUrls"></ImageViewer>
    <VideoViewer v-show="isShowVideoViewer" :urls="videoViewerUrls"></VideoViewer>
  </div>
</template>

<script>
<<<<<<< HEAD:view/ph-view/src/page/DutyLearning/DeseaseSeriesDetail.vue
import ImageViewer from '../../components/ImageViewer.vue'
=======
import ImageViewer from '../components/ImageViewer.vue'
import VideoViewer from '../components/VideoViewer.vue'
>>>>>>> ae1c1d097c13dc747ec38b2a9763883cbae11700:view/ph-view/src/page/DeseaseSeriesDetail.vue
export default {
  components: { ImageViewer, VideoViewer },
  data () {
    return {
      id: this.$route.params.id,
      pictureCount: 0,
      detailMessage: '',
      isShowDetails: false,
      isShowPicture: false,
      isShowVideo: false,
      videoCount: 0,
      isShowImageViewer: false,
      imageViewerUrls: [],
      isShowVideoViewer: false,
      videoViewerUrls: [],
      // data stubs, wait for axios
      deseaseCasesData: {
        'deseaseCases': [
          {
            'id': 'jekjckwlwpckke11',
            'name': '郑光煜可怜的小狗狗得了前列腺炎'
          },
          {
            'id': 'jekjl2223wpckke1ekje11',
            'name': '王俊杰的小乌龟头炸了'
          }
        ]
      },
      deseaseCaseData: {
        'deseaseCase': {
          'id': 'jekjl2223wpckke1ekje11',
          'name': '王俊杰的小乌龟头炸了',
          'description': '王俊杰在写代码, 二郎腿翘了太久了, 把自己养的小乌龟头挤炸了',
          'time': '上午9点',
          'picture': {
            'urls': [
              {'url': 'https://ss1.bdstatic.com/70cFuXSh_Q1YnxGkpoWK1HF6hhy/it/u=534386446,2383379323&fm=27&gp=0.jpg'},
              {'url': 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=3269230542,2079728320&fm=27&gp=0.jpg'},
              {'url': 'https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=3351311726,1166292474&fm=27&gp=0.jpg'},
              {'url': 'https://ss0.bdstatic.com/70cFvHSh_Q1YnxGkpoWK1HF6hhy/it/u=1258893326,3098157884&fm=27&gp=0.jpg'}
            ]
          },
          'video': {
            'urls': [
              {'url': 'http://clips.vorwaerts-gmbh.de/big_buck_bunny.mp4'},
              {'url': 'http://www.html5videoplayer.net/videos/toystory.mp4'}
            ]
          }
        }
      }
    }
  },
  created () {
    this.getDeseaseCasesData()
  },
  methods: {
    getDeseaseCasesData () {
      // get desease cases data
      return true
    },
    showDeseaseCaseDetail () {
      var isSuccess = this.getDeseaseCasesData()
      if (isSuccess === false) {
        this.isShowDetails = true
        this.detailMessage = '请检查网络连接'
        return
      }
      if (this.deseaseCaseData.deseaseCase.picture === 'NONE') {
        this.pictureCount = 0
        this.isShowPicture = false
      } else {
        this.pictureCount = this.deseaseCaseData.deseaseCase.picture.urls.length
        this.isShowPicture = true
      }
      if (this.deseaseCaseData.deseaseCase.video === 'NONE') {
        this.videoCount = 0
        this.isShowVideo = false
      } else {
        this.videoCount = this.deseaseCaseData.deseaseCase.video.urls.length
        this.isShowVideo = true
      }
      this.isShowDetails = true
      this.detailMessage = this.deseaseCaseData.deseaseCase.description + this.deseaseCaseData.deseaseCase.time
    },
    showImages () {
      this.isShowImageViewer = true
      this.imageViewerUrls = this.deseaseCaseData.deseaseCase.picture.urls
      this.unshowVideo()
    },
    showVideo () {
      this.isShowVideoViewer = true
      this.videoViewerUrls = this.deseaseCaseData.deseaseCase.video.urls
      this.unshowImages()
    },
    unshowImages () {
      this.isShowImageViewer = false
    },
    unshowVideo () {
      this.isShowVideoViewer = false
    }
  }
}
</script>
