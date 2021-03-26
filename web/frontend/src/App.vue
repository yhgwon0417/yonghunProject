<template>
  <div id="app">
    <Header />
    <div class="wrap">
    <div class="container"> <!-- class 추가 -->
      <router-view />
    </div>
    </div>
    <Footer />
  </div>
</template>

<script>
import Header from './components/common/Header';
import Footer from './components/common/Footer';


export default {
  name: 'App',
  components: {
    Header
    ,Footer  
  }
}
</script>

//css 수정
<style>
html,body{padding:0; margin:0;}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}


.wrap{width:100%;}
.container{width:80%; padding:10px; margin:0 auto;}


</style>