<template>
  <div class = "row">
    <div class="footer_back">
      <div class="col-md-5">
        <div class="gongan_logo_part">
          <transition name="gongan_img_trans">
            <img v-if="show" class = "gongan_img" src="../../static/img/footer.jpg"/>
          </transition>
        </div>
      </div>
      <div class="col-md-7">
        <div class="gongan_text_part">
          <p class = "gongan_text">广播电视节目制作经营许可证：（沪）字第1248号 | 网络文化经营许可证：沪网文[2013]0480-056号 | 信息网络传播视听节目许可证：0910417 | 互联网ICP备案：沪ICP备13002172号-3 沪ICP证：沪B2-20100043 | 沪公网安备 31011002002436号</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data () {
    return {
      show: false
    }
  },
  mounted () {
    this.show = true
  }
}
</script>

<style>
.footer_back{
  width:100%;
  height:100px;
  background-color: #405685;
}
.gongan_logo_part{
  padding-left: 600px;
}
.gongan_img{
  margin-top: 12px;
  margin-bottom: 0px;
  width:80px;
  height:80px;
  border-radius: 50%;
}
.gongan_text_part{
  padding-right: 500px;
}
.gongan_text{
  font-size: 15px;
  margin-top: 20px;
  margin-bottom: 0px;
  color: #bdbaba;
}
/* animations here */
.gongan_img_trans-enter-active, .gongan_img_trans-leave-active {
  transition: all 0.5s ease;
}
.gongan_img_trans-enter, .gongan_img_trans-leave-to{
  transform: translateX(-30px);
  opacity: 0;
}

</style>
