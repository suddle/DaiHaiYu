<template>
  <el-container>
    <el-header class="head">
      <mt-header fixed title="固定在顶部"></mt-header>
    </el-header>
    <el-main class="container_wrap">
      <div id="app" class="container">
        <router-view/>

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
</style>
