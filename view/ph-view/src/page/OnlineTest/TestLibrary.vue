<template>
  <div>
    <button v-on:click="logOut()">登出</button>
    <button v-on:click="jumpToPage('WelcomePage')">回到主页</button>
  </div>
</template>

<script>
export default {
  name: 'test-library'
}
</script>

<style scoped>

</style>
