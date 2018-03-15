<template>
  <div>
    <div class="container-fluid">
      <div class = "row">
        <div class = "title_row">
          <div class="col-xs-9">
            <div class="left_title_part">
              <p class = "software_title">虚拟宠物医院</p>
            </div>
          </div>
          <div class="col-xs-2">
            <div class="middle_title_part">
              <!--<p class = "hello_title">欢迎, 新进干员</p>-->
              <button class="title_button" v-on:click="logOut()">登出</button>
              <button class="title_button" v-on:click="jumpToPage('MainPage')">回到主页</button>
            </div>
          </div>
          <div class="col-xs-1">
            <div class="right_title_part">
              <img class = "header_img" src="../../static/img/header.jpg"/>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
.title_row{
  background: #405685;
  width:100%;
  height:85px;
}

.title_button{
  color:#fff;
  background:#405685;
  border-color:#405685;
}
.left_title_part{
  padding-top:20px;
  padding-left: 75px;
  padding-right: 0px;
  text-align:left;
}
.software_title{
  font-size: 30px;
  letter-spacing: 5px;
  color:white;
}

.middle_title_part{
  margin-left: 70px;
  padding-top:35px;
}
.hello_title{
  font-size: 10px;
  letter-spacing: 3px;
  color:white;
}

.right_title_part{
  padding-top:10px;
}
.header_img{
  height: 64px;
  width: 64px;
  border: 2px;
  border-radius: 50%;
  border-color:  #5894cc;
}
</style>
