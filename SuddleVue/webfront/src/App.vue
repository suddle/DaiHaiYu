<template>
  <el-container>

   <mt-header title="快速问医生">
      <router-link to="/" slot="left">
         <mt-button icon="back">返回</mt-button>
        <!--  <mt-button @click="handleClose">close</mt-button> -->
       </router-link>
       <mt-button icon="more" slot="right"></mt-button>
   </mt-header>
  
  <!--   轮播图 -->
  <mt-swipe :auto="3000" class="swipe-banner">
    <mt-swipe-item>图片1</mt-swipe-item>
    <mt-swipe-item>图片2</mt-swipe-item>
    <mt-swipe-item>图片3</mt-swipe-item>
  </mt-swipe>

<!--   内容 -->
    <el-main class="container_wrap">
      <div id="app" class="container">
       <!--  <router-view/> -->
       <div  class="swipe-banner2">
          <picture class="pic"><p class="h60">图片1</p><p class="h40">快速问诊</p></picture>
          <picture class="pic"><p class="h60">图片1</p><p class="h40">快速问诊</p></picture>
          <picture class="pic"><p class="h60">图片1</p><p class="h40">快速问诊</p></picture>
          <picture class="pic"><p class="h60">图片1</p><p class="h40">快速问诊</p></picture>
       </div>

        <div  class="swipe-banner margin-bottom10">
        
       </div>
       <div  class="swipe-banner margin-bottom10">
        
       </div>
       <div  class="swipe-banner margin-bottom10">
        
       </div>
       <div  class="swipe-banner margin-bottom10">
        
       </div>
        
      </div>
    </el-main>
    <el-footer class="foot">
      <mt-tabbar v-model="selected">
        <mt-tab-item id="首页">
          <router-link :to="'one'">首页</router-link>
        </mt-tab-item>
        <mt-tab-item id="正文">
          正文
        </mt-tab-item>
        <mt-tab-item id="发现">
          发现
        </mt-tab-item>
        <mt-tab-item id="我的">
          我的
        </mt-tab-item>
      </mt-tabbar>
    </el-footer>
  </el-container>
</template>
<script>

export default {
  name: 'App'
}
</script>
<style>
.head{
padding:0;
}
.foot{
padding:0;
}
.container{
padding:0;
}
.container_wrap{
padding:0;
}
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
body,html{
width:100%;
height:100%;
margin:0;
padding:0;
}
header{
  height:10%;
}
footer{
  height:10%;
}
main{
  height:80%;
}
.el-container{
height:100%;
}
.swipe-banner{
  height: 120px;
  padding-top: 0;
  background: #ccc;
}
.swipe-banner2{
  height: 120px;
  background: yellow;
   display: flex;
   display: -webkit-flex;
   align-items:center;
   justify-content:center;
}
.pic{
  width: 20%;
  height: 80%;
  background: #fff;
  display: inline-block;
  margin: 0 10px 0 10px;
}
.h60{
  height: 40%;
}
.h40{
  height: 20%;
}
.margin-bottom10{
  margin-bottom: 10px
}
</style>
