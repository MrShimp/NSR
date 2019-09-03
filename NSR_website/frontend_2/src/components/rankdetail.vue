<template>
<div class = "blocks_container">
  <!-- conclusion info -->
  <div class = "blocks_detail_container">
    <div class="title">
      <img class="goback" src="../assets/arrowleft.png" alt="" @click = "goback">
      <span>{{info}} INDEX</span>
    </div>
    <div class="search_area">
      <input type="text" name="" value="" class="search_input" v-model='search'>
      <img src="../assets/search.png" style="float:right; width:25px; margin-right: 5%;" alt="">
    </div>
    <div class="bot">
      <div class="name">
        <span style="float:left">Tracks</span>
        <span style="float:right">Rank</span>
      </div>
      <hr class="split">
      <div class="rankbox">
        <div
          v-for="(item, index) in items"
          @mouseover = "onMouseOver(index)"
          @mouseout = "onMouseOut"
          @mousedown = "onMouseClick(index)"
          v-bind:class = "{ block_choose: isHovering == index }">
          <span style="float:left">{{item.Tract}}</span>
          <span style="float:right">{{index+1}}</span>
        </div>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import store from '@/store/store.js'

export default {
  props: ['info'],
  data: () => ({
    showing: true,
    items: [],
    testdata: false,
    search: '',
    target: '',
    isHovering: -1
  }),
  mounted () {
    this.getdata()
  },
  watched: {
    'store.state.indexname': function () {
      this.getdata()
    }
  },
  computed: {
    info() {
      return store.state.indexname
    }
  },
  methods: {
    goback: function () {
      console.log('this is block click')
      var set = false
    },
    getdata: function () {
      this.testdata++
      this.items = []
      var vm = this
      this.testdata = true

      this.$axios.get('http://127.0.0.1:8000/nsr/explore/' + store.state.indexname).then(function (response) {
        vm.items = response.data
      })
    },
    onMouseOver: function (index) {
      this.isHovering = index
    },
    onMouseOut: function () {
      this.isHovering = -1
    },
    onMouseClick: function (index) {
      var set = true
      store.commit('changeexplore_showpopup', set)
    }
  },
  computed: {
    searchData: function () {
      var searchdata = this.searchData
      if (searchdata) {
        return this.items.filter(post => {
          return Object.Tracts.toLowerCase().includes(searchdata.toLowerCase())
        })
      }
      return this.items
    }
  }
}
</script>

<style scoped>
  .blocks_container{
    background-color: white;
    border-radius: 5px;
    border: 0.5px;
    box-shadow: 0px 0px 5px #CDCFD1;
    width: 22%;
    height: 80%;
    position: absolute;
    left: 5%;
    top:10%;
    z-index: 1;
  }

  .blocks_detail_container{
    width: 100%;
    height: 100%;
  }

  .title {
    font-family: 'Muli', sans-serif;
    font-weight: Bold;
    font-size: 20px;
    margin-left: 13px;
    margin-top: 15px;
  }

  .split{
    width: 100%;
  }

  .bot{
    position: absolute;
    margin-left: 20px;
    margin-right: 10px;
    top: 20%;
    width: 85%;
    height: 80%;
  }

  .rankbox{
    height: 80%;
    overflow: auto;
  }

  .goback{
    width: 10%;
    height: 10%;
    float: left;
  }
  .name {
    height: 35px;
    width: 100%;
    font-family: 'Raleway', sans-serif;
  }

  .search_area{
    border: 1px solid #A2A5A8;
    width: 90%;
    height: 30px;
    margin-left: 5%;
    border-radius: 50px;
    margin-top: 50px;
  }

  .search_input{
    width: 60%;
    border: none;
    margin-left: 5%;
    border-radius: 50px;
  }

  .block_choose{
    background-color : #CDCFD1;
    color: red;
  }


</style>
