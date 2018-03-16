<template>
  <div>
    <button v-on:click="logOut()">登出</button>
    <button v-on:click="jumpToPage('CaseLearningPage')">病例学习</button>
    <button v-on:click="jumpToPage('WelcomePage')">回到主页</button>
    <Content :style="{padding: '0 16px 16px'}">
      <Breadcrumb :style="{margin: '16px 0'}">
        <BreadcrumbItem>Home</BreadcrumbItem>
        <BreadcrumbItem>Components</BreadcrumbItem>
        <BreadcrumbItem>Layout</BreadcrumbItem>
      </Breadcrumb>
      <Card>
        <div style="height: 600px">Content</div>
      </Card>
    </Content>
  </div>
</template>

<script>
export default {
  name: 'official-test'
}
</script>

<style scoped>

</style>
