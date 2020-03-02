<template>
	<!--   内容 -->
    <el-main class="container_wrap">
      <div id="app" class="container">
       <!--  <router-view/> -->
        <!--   轮播图 -->
        <mt-swipe :auto="3000" class="swipe-banner">
        <mt-swipe-item v-for="(val,idnex) in imgList">
           <img v-bind:src="val" class="pig-sise"/>
        </mt-swipe-item>
       </mt-swipe>
       <div  class="swipe-banner2">
          <picture class="pic">
			   <i class="icon iconfont icon-wenzhen"></i>
			   <p class="h40">快速问诊</p>
		   </picture>
		    <picture class="pic">
			   <i class="icon iconfont icon-nvxing"></i>
			   <p class="h40">呵护女性</p>
		   </picture>
		   <picture class="pic">
			   <i class="icon iconfont icon-nanxing_"></i>
			   <p class="h40">男性健康</p>
		   </picture>
		   <picture class="pic">
			   <i class="icon iconfont icon-menzhen"></i>
			   <p class="h40">开药门诊</p>
		   </picture>
       </div>

        <div  class="swipe-banner margin-bottom10 jian-kan">
        	<span class="padding-jian">健康圈  </span>
        	<span class="padding-jian">更多社区</span>
       </div>
       
       <div  class="swipe-banner-style margin-bottom10">
        	<p class="h40"><img src="http://www.51yuansu.com/pic2/cover/00/29/35/580c19c949b62_610.jpg" class="w100 h100"></p>
        	<p class="h10  jian-kan">
        		<span class="padding-jian">包图</span>
        		<span class="padding-jian">热贴</span>
        	</p>
        	<p class="h50">《100种最有利健康的食物》一书对100种有利于健康的觉食物进行了详细的解读，从食物的营养成分、功效、性质、适用及不适用者、食物的宜与忌到食物搭配的相生相克，娓娓道来，既通俗易懂又注重实用性和可操作性。</p>
       </div>
        <div  class="swipe-banner-style margin-bottom10">
        	<p class="h40"><img src="http://www.51yuansu.com/pic2/cover/00/29/35/580c19c949b62_610.jpg" class="w100 h100"></p>
        	<p class="h10  jian-kan">
        		<span class="padding-jian">包图</span>
        		<span class="padding-jian">热贴</span>
        	</p>
        	<p class="h50">《100种最有利健康的食物》一书对100种有利于健康的觉食物进行了详细的解读，从食物的营养成分、功效、性质、适用及不适用者、食物的宜与忌到食物搭配的相生相克，娓娓道来，既通俗易懂又注重实用性和可操作性。</p>
       </div>
        <div  class="swipe-banner-style margin-bottom10">
        	<p class="h40"><img src="http://www.51yuansu.com/pic2/cover/00/29/35/580c19c949b62_610.jpg" class="w100 h100"></p>
        	<p class="h10  jian-kan">
        		<span class="padding-jian">包图</span>
        		<span class="padding-jian">热贴</span>
        	</p>
        	<p class="h50">《100种最有利健康的食物》一书对100种有利于健康的觉食物进行了详细的解读，从食物的营养成分、功效、性质、适用及不适用者、食物的宜与忌到食物搭配的相生相克，娓娓道来，既通俗易懂又注重实用性和可操作性。</p>
       </div>
      
        
      </div>
    </el-main>

</template>
<script type="text/javascript">
	
	/*import './assets/icon/iconfont.js';*/
	
</script>
<script type="text/javascript">


export default {
  name: 'App',
   data () {
    return {
      msg: '我来了',
      ass:1,
      imgList:[]
   
    }
  },
   created(){
   
          this.run();
  },
  methods: {
    
      run:function(){
         const that = this;
          that.$axios({
                method:'get',
                url:this.$sudleurl+'/getpic/',
                data:""
            }).then((response) =>{          //这里使用了ES6的语法
                console.log(response)       //请求成功返回的数据
                  for(var i=0;i<response.data.data.length;i++){
                       that.imgList.push(response.data.data[i].img)
                       console.log(response.data.data[i].img,1111111)
                  }
                  console.log(that.imgList)
                 
            }).catch((error) =>{
                console.log(error)       //请求失败返回的数据
            })
      },
  /*  searchFun:function() {
      this.$router.replace({name:'search'})
    }*/
    
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
height: 100%;
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
  background: #fff;
   display: flex;
   display: -webkit-flex;
   align-items:center;
   justify-content:center;
}
.pic{
  width: 20%;
  height: 50%;
  background: #fff;
  display: inline-block;
  margin: 0 10px 0 10px;
  margin-bottom: 10px;
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

.iconfont {
  font-family: "iconfont" !important;
  font-size: 35px;
  font-style: normal;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.jian-kan{
	display: flex;
	justify-content: space-between;
	align-items:center;	
	height: 50px;
}
.padding-jian{
	padding: 0 20px 0 20px;
}
.swipe-banner-style{
	height: 200px;
	width: 100%;
	border-bottom: 1px solid #ddd;
	margin-bottom: 10px;
}
.h10{
	height: 10%;	
}
.h40{
	height: 40%;	
}
.h50{
	height: 50%;	
}
.h60{
	height: 60%;	
}
.h100{
	height: 100%;
	
}
.w100{
	width: 100%;
}
</style>
