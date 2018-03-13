<template>
  <div>
    <PHHeader></PHHeader>
    <img id="circle_img" class="circle_img_style" src = "../../static/img/ph-guiding-circle.png"/>
    <div class="row">
      <p>医院导览</p>
    </div>
    <div class="row">
      <div class="col-xs-8">
        <img class="phguding_img_style" src = "../../static/img/phguiding_main.jpg"/>
      </div>
      <div class="col-xs-4">
        <div class="room_list_part">
          <ul>
            <li v-for= "department in departmentList" :key= "department.id">
              <router-link :to="'/phguiding/' + department.id">
                <p v-on:mouseenter="showRoomPosition(department.name)" v-on:mouseleave="hideRoomPosition()">{{ department.name }}</p>
              </router-link>
            </li>
          </ul>
        </div>
      </div>
    </div>
    <button v-on:click="logOut()">登出</button>
    <button v-on:click="jumpToPage('MainPage')">回到主页</button>
    <PHFooter></PHFooter>
  </div>
</template>

<script>
import PHHeader from '../components/PHHeader.vue'
import PHFooter from '../components/PHFooter.vue'
export default {
  components: { PHHeader, PHFooter },
  data () {
    return {
      departmentList: [],
      circlePosData: [
        ['口腔科', '100x200'],
        ['皮肤科', '200x300'],
        ['肛门科', '300x100'],
        ['内分泌科', '400x500'],
        ['手术室', '200x800'],
        ['避孕室', '200x700'],
        ['瞎JB室', '200x300']
      ],
      imgVar: {},
      timer: {}
    }
  },
  created () {
    this.checkLogin()
    this.getDepartmentList()
  },
  mounted () {
    this.imgVar = document.getElementById('circle_img')
    this.imgVar.style.visibility = 'hidden'
  },
  methods: {
    showRoomPosition (name) {
      var pos = ''
      for (var i = 0; i !== this.circlePosData.length; i++) {
        if (this.circlePosData[i][0] === name) {
          pos = this.circlePosData[i][1]
          break
        }
      }
      if (pos !== '') {
        var poses = pos.split('x')
        var left = poses[0]
        var top = poses[1]
        this.imgVar.style.width = '0px'
        this.imgVar.style.height = '0px'
        this.imgVar.style.left = left + 'px'
        this.imgVar.style.top = top + 'px'
        this.imgVar.style.visibility = 'visible'
        this.timer = setInterval(function () {
          this.imgVar.style.width = this.imgVar.style.width + 10 + 'px'
          this.imgVar.style.height = this.imgVar.style.height + 10 + 'px'
          if (this.imgVar.style.width > 300) {
            clearInterval(this.timer)
          }
        }, 30)
      }
    },
    hideRoomPosition () {
      this.imgVar.style.visibility = 'hidden'
    },
    getDepartmentList () {
      this.$api.get('intros', null, r => {
        this.departmentList = r.departments
      })
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

<style>
.phguding_img_style{
  width:800px;
  height:800px;
}
.room_list_part{
  margin-top: 275px;
}
.circle_img_style{
  z-index: 100;
  position: absolute;
}
</style>
