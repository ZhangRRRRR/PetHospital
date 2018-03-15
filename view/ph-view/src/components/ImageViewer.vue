<template>
  <div>
    <img v-bind:src="src">
    <p></p>
    <button v-on:click="previousPhoto()">previous</button>
    <button v-on:click="nextPhoto()">next</button>
  </div>
</template>

<script>
export default {
  props: {
    urls: Array
  },
  data () {
    return {
      currentIndex: 0,
      src: '',
      urlLength: 0
    }
  },
  methods: {
    nextPhoto () {
      this.urlLength = this.urls.length
      this.nextIndex()
      this.src = this.urls[this.currentIndex].url
    },
    previousPhoto () {
      this.urlLength = this.urls.length
      this.previousIndex()
      this.src = this.urls[this.currentIndex].url
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
