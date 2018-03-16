<template>
  <div>
    <button v-on:click="logOut()">登出</button>
    <button v-on:click="jumpToPage('RolePlayPage')">角色扮演</button>
    <button v-on:click="jumpToPage('CaseLearningPage')">病例学习</button>
    <button v-on:click="jumpToPage('WelcomePage')">回到主页</button>
  </div>
</template>

<script>
export default {
  name: 'mock-test'
}
</script>

<style scoped>

</style>
