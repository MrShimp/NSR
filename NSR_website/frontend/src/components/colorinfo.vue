<template>
  <div class="info_container">
    <div class="title">The Color represents:</div>
    <div class="info_session">
      <div class="color_block" style="background-color: green">
      </div>
      <span class="text">Top 25%</span>
    </div>
    <div class="info_session">
      <div class="color_block" style="background-color: yellow">
      </div>
      <span class="text">25% ~ 50%</span>
    </div>
    <div class="info_session">
      <div class="color_block" style="background-color: orange">
      </div>
      <span class="text">50% ~ 75%</span>
    </div>
    <div class="info_session">
      <div class="color_block" style="background-color: red">
      </div>
      <span class="text">75% ~ 100%</span>
    </div>
  </div>
</template>

<style scoped>
  .info_container {
    background-color: white;
    border-radius: 5px;
    border: 0.5px;
    box-shadow: 0px 0px 5px #CDCFD1;
    position: absolute;
    bottom: 3%;
    right: 5%;
    height: 20%;
    width: 18%;
    padding: 10px;
  }

  .title {
    height: 20%;
    width: 90%;
  }

  .info_session{
    height: 20%;
    width: 90%;
  }

  .color_block{
    height: 20px;
    width: 40px;
    margin-left: 3%;
    float: left;
    margin-top: 3%;
  }

  .text{
    margin-left: 30px;
    font-size: 15px;
    font-family: 'Muli', sans-serif;
  }


</style>

<script>
import store from '@/store/store.js'
export default {
  components: {

  },
  data () {
    return {

    }
  },
  computed: {
    colorData () {
      return store.state.color_boundary
    }
  },
}
</script>
