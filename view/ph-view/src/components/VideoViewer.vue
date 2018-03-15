<template>
  <div v-on:mouseenter="showCurrentVideo()" >
    <video-player class="video-player-box"
                  ref="videoPlayer"
                  :options="playerOptions"
                  :playsinline="true"
                  customEventName="customstatechangedeventname"
                  @play="onPlayerPlay($event)"
                  @pause="onPlayerPause($event)"
                  @ready="playerReadied">
    </video-player>
    <p></p>
    <button v-on:click="previousVideo()">previous</button>
    <button v-on:click="nextVideo()">next</button>
  </div>
</template>

<script>
import 'video.js/dist/video-js.css'
import { videoPlayer } from 'vue-video-player'

export default {
  components: {
    videoPlayer
  },
  props: {
    urls: Array
  },
  data () {
    return {
      playerOptions: {
        muted: true,
        language: 'en',
        playbackRates: [0.7, 1.0, 1.5, 2.0],
        sources: [{
          type: 'video/mp4',
          // this src is for no error init, try to find a way to solve the problem
          src: 'http://vjs.zencdn.net/v/oceans.mp4'
        }]
      },
      currentIndex: 0,
      src: '',
      urlLength: 0
    }
  },
  mounted () {
    // console.log('this is current player instance object', this.player)
  },
  computed: {
    player () {
      return this.$refs.videoPlayer.player
    }
  },
  methods: {
    onPlayerPlay (player) {
      // console.log('player play!', player)
    },
    onPlayerPause (player) {
      // console.log('player pause!', player)
    },
    playerStateChanged (playerCurrentState) {
      // console.log('player current update state', playerCurrentState)
    },
    playerReadied (player) {
      // console.log('the player is readied', player)
    },
    showCurrentVideo () {
      this.src = this.urls[this.currentIndex].url
      this.playerOptions.sources[0].src = this.src
    },
    nextVideo () {
      this.urlLength = this.urls.length
      this.nextIndex()
      this.showCurrentVideo()
    },
    previousVideo () {
      this.urlLength = this.urls.length
      this.previousIndex()
      this.showCurrentVideo()
    },
    nextIndex () {
      var length = this.urlLength
      if (this.currentIndex === length - 1) {
        this.currentIndex = 0
      } else {
        this.currentIndex++
      }
    },
    previousIndex () {
      var length = this.urlLength
      if (this.currentIndex === 0) {
        this.currentIndex = length - 1
      } else {
        this.currentIndex--
      }
    }
  }
}
</script>
