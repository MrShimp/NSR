<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
  @import url('https://fonts.googleapis.com/css?family=Lato:400,700|Montserrat:400,700|Oswald:200,300,700&display=swap');
  * {
    margin: 0px;
    padding: 0px;
  }
  html, body {
    height:100%;
    width:100%;
    margin: 0px;
    padding: 0px;
  }
  #app{
    height:100%;
    width:100%;
  }
</style>
