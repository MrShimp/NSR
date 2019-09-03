<template>
  <div class="main_area">
    <div id="cover">
      <div class="tb">
        <div class="td">
          <input type="text"
            placeholder="Input location..."
            id="placeinput"
            v-model="location"
            >
          <input type="text"
            placeholder="Input ZipCode..."
            id="zipinput"
            v-model="zipcode"
            >
        </div>
        <div class="td" id="s-cover">
          <button type="submit" @click = "submit">
            <div id="s-circle"></div>
            <span></span>
          </button>
        </div>
      </div>
      <div class = "skip">
        <a href="/explore">skip</a>
      </div>
    </div>

  </div>
</template>

<script>
import VLink from '@/components/VLink.vue'
import store from '@/store/store.js'

export default {
  components: {
    VLink
  },
  props: ['name'],
  data: function () {
    return {
      autocomplete: null,
      location: null,
      center: [],
      geoid: null,
      zipcode: null
    }
  },
  mounted: function () {
    var input = document.getElementById('placeinput')
    this.autocomplete = new google.maps.places.Autocomplete(input)
    var vm = this
    this.autocomplete.addListener('place_changed', function() {
      vm.location = vm.autocomplete.getPlace().name;
      vm.center = vm.autocomplete.getPlace().geometry.location;
    })
  },
  methods: {
    submit: function () {
      var target = this.location.replace(/\s+/g, '+')
      var zip = this.zipcode
      var vm = this
      this.$axios.get('http://127.0.0.1:8000/nsr/getaddress/?address=' + target +'&zip=' + zip).then(function (response) {
        vm.geoid = response.data
      })
      store.commit('change_cur_center', this.center)
      this.$router.push('/explore')
    }
  }
}
</script>

<style scoped>
  @import url('https://fonts.googleapis.com/css?family=Red+Hat+Display:400,400i,500&display=swap');

  .main_area{
    position: absolute;
    top: 30%;
    left: 30%;
    width: 50%;
    height: 50%;
    background-color: lightgrey;
  }

  .tb{
    display: table;
    width: 100%;
  }

  .td{
    display: table-cell;
    vertical-align: middle;
  }

  input, button{
    color: #fff;
    font-family: 'Red Hat Display', sans-serif;
    padding: 0;
    margin: 0;
    border: 0;
    background-color: transparent;
  }

  #cover{
    position: absolute;
    top: 50%;
    left: 0;
    right: 0;
    width: 650px;
    padding: 35px;
    margin: -83px auto 0 auto;
    background-color: #1C3854;
    border-radius: 20px;
    transform: scale(0.6);
  }

  .skip {
    height: 30px;
    width: 50px;
    margin-right: 30px;
    margin-botton: 20px;
    font-size: 20px;
    font-family: 'Red Hat Display', sans-serif;
  }

  input[type="text"]{
      width: 100%;
      height: 96px;
      font-size: 30px;
      line-height: 1;
  }

  input[type="text"]::placeholder{
      color: #e16868;
  }

  #s-cover{
      width: 1px;
      padding-left: 35px;
  }

  button{
      position: relative;
      display: block;
      width: 84px;
      height: 96px;
      cursor: pointer;
  }

  #s-circle{
      position: relative;
      top: -8px;
      left: 0;
      width: 65px;
      height: 65px;
      margin-top: 0;
      border-width: 15px;
      border: 15px solid #fff;
      background-color: transparent;
      border-radius: 50%;
      transition: 0.5s ease all;
  }

  button span{
      position: absolute;
      top: 68px;
      left: 43px;
      display: block;
      width: 37px;
      height: 19px;
      background-color: transparent;
      border-radius: 10px;
      transform: rotateZ(52deg);
      transition: 0.5s ease all;
  }

  button span:before, button span:after{
      content: '';
      position: absolute;
      bottom: 0;
      right: 0;
      width: 45px;
      height: 15px;
      background-color: #fff;
      border-radius: 10px;
      transform: rotateZ(0);
      transition: 0.5s ease all;
  }

  #s-cover:hover #s-circle{
      top: -1px;
      width: 67px;
      height: 15px;
      border-width: 0;
      background-color: #fff;
      border-radius: 20px;
  }

  #s-cover:hover span{
      top: 50%;
      left: 56px;
      width: 25px;
      margin-top: -9px;
      transform: rotateZ(0);
  }

  #s-cover:hover button span:before{
      bottom: 11px;
      transform: rotateZ(52deg);
  }

  #s-cover:hover button span:after{
      bottom: -11px;
      transform: rotateZ(-52deg);
  }
  #s-cover:hover button span:before, #s-cover:hover button span:after{
      right: -6px;
      width: 40px;
      background-color: #fff;
  }
</style>
