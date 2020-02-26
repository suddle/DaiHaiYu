<template>
  <div class="container">
    <h3>欢迎来到我的个人博客</h3>
    <div @click="run()">{{ass}}</div>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: '我来了',
      ass:1
    }
  },
   created(){
            
        },
  methods: {
      run:function(){
         	this.$axios({
                method:'post',
                url:'api',
                data:this.qs.stringify({    //这里是发送给后台的数据
                      userId:this.userId,
                      token:this.token,
                })
            }).then((response) =>{          //这里使用了ES6的语法
                console.log(response)       //请求成功返回的数据
            }).catch((error) =>{
                console.log(error)       //请求失败返回的数据
            })
      }
    
	}
}

</script>
<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}


</style>
