<template>
<div class = "detail_container">
<!-- top -->
<div class = "top">
  <div class = "inside">
    <img class="goback" src="../assets/left.png" alt="">
        <span style="color: white;">Calure Index</span>
  </div>
</div>
<!-- mid -->
<div class="mid inside">
  <h6 class="title">Index Details</h6>
  <div class = "indicators">
    <div>
      <span class="indicators_title">Indicators</span>
      <div class="checkboxs">
        <div class="checkbox left">
          <input type="checkbox" aria-label="Checkbox for following text input">
          <span class="indicators_font">Goal_1</span>
        </div>
        <div class="checkbox left">
          <input type="checkbox" aria-label="Checkbox for following text input">
          <span>Goal_4</span>
        </div>
        <div class="checkbox left">
          <input type="checkbox" aria-label="Checkbox for following text input">
          <span>Goal_8</span>
        </div>
        <div class="checkbox left">
          <input type="checkbox" aria-label="Checkbox for following text input">
          <span>Goal_9</span>
        </div>
        <div class="checkbox left">
          <input type="checkbox" aria-label="Checkbox for following text input">
          <span>Goal_11</span>
        </div>
      </div>
  </div>
  </div>
  <hr class="split"></hr>
  <div>
    <div>#1/20</div>
  <div>
  <hr class="split"></hr>
  <div>
    <div></div>
  <div>
</div>
<!-- bot -->
<div>
  <div></div>
  <div></div>
</div>
</div>
</template>

<script>
import store from '@/store/store.js'

export default {
  data: function () {
    return {

    }
  }
}
</script>

<style scoped>
.left{
  float: left;
}

.right{
  float: right;
}

.detail_container{
  border-radius: 5px;
  border: 0.5px;
  box-shadow: 0px 0px 5px #CDCFD1;
  width: 20%;
  height: 80%;
  position: absolute;
  left: 5%;
  top:5%;
  z-index: 1;
}

.top {
  font-family: 'Muli', sans-serif;
  font-weight: light;
  font-size: 20px;
  background-color: #5CC9F3;
  width: 100%;
  height: 15%;
  position: relative;
  }

  .inside {
    margin:0 auto;
    position: absolute;
    left: 10%;
  }

  .mid {
    width: 90%;
    height: 85%;
  }
  .goback{
  width: 10%;
  height: 10%;
  float: left;
  top: 5%;
}

.title{
  margin-top: 10%;
  margin-bottom: 5%;
}
.split{
  width: 100%;
}

.indicators {
  width: 95%;
  height: 20%
}

.indicators_title{
  margin-top: 10px;
  margin-bottom: 10px;
}

.checkboxs{
  width: 100%;
}

.checkbox{
  width: 50%;
}
</style>
