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
  methods: {
      run:function(){
      this.ass=10
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
