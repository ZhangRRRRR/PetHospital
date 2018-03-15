<template>
  <div v-on:mouseenter="showCurrentPage()">
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
    showCurrentPage () {
      this.src = this.urls[this.currentIndex].url
    },
    nextPhoto () {
      this.urlLength = this.urls.length
      this.nextIndex()
      this.showCurrentPage()
    },
    previousPhoto () {
      this.urlLength = this.urls.length
      this.previousIndex()
      this.showCurrentPage()
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
