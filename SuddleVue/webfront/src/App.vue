<template>
  <el-container>
  <!-- title="快速问医生" -->
   <mt-header >
      <router-link to="/" slot="left" style="width: 10%">
         <mt-button icon="back width-auto">返回</mt-button>            
        <input class="width-height-auto"   placeholder="请输入你的内容"/>
      </router-link>
     
      <mt-button icon="more "  class="width-auto" slot="right"></mt-button>      
   </mt-header>
    <el-main class="container_wrap">
      <router-view/>
    </el-main>

    <el-footer class="foot">
      <mt-tabbar >
        <mt-tab-item id="首页">
          <router-link :to="'one'">首页</router-link>
        </mt-tab-item>
        <mt-tab-item id="正文">
           <router-link :to="'two'">正文</router-link>
        </mt-tab-item>
        <mt-tab-item id="发现">
           <router-link :to="'three'">发现</router-link>
        </mt-tab-item>
        <mt-tab-item id="我的">
           <router-link :to="'four'">我的</router-link>
        </mt-tab-item>
      </mt-tabbar>
    </el-footer>
  </el-container>
</template>
<script>

export default {
  name: 'App',
   data () {
    return {
      msg: '我来了',
      ass:1,
    
   
    }
  }
}









</script>
<style >
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
.pig-sise{
  width: 100%;
  height: 100%;
  display: inline-block;
}
.width-height-auto{
  width: 250px;
  height: 100%;
  background:#fff;
  margin-left: 10px;
  border-radius: 50px;
  border: 1px solid #ddd;
}

</style>
