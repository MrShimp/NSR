<template >
<div class = "blocks_container">
  <!-- first -->
    <div class="title">
      Vibrancy Index
    </div>
    <div class="top">
      <span class="allscore">{{AllScore}}</span>
      <div class="smallinfo">
        <span>{{cur_location_name}}</span>
      </div>
      <div class="cat_text">Rank:{{Allrank}} </div>
      <div class="cat_text">Max:{{max_value}}</div>
      <div class="cat_text">Min:{{min_value}}</div>
    </div>
    <div class="bot">
      <hr class="split">
      <div style="height:100%">
        <div class = "indexinfo"
          v-for = "(item,index) in items"
          @mouseover = "onMouseOver(index)"
          @mouseout = "onMouseOut"
          @mousedown = "onMouseClick(index)"
          v-bind:class = "{ hover_block_choose: isHovering == index }">
          <div class="sum_info_score" id="sum_info_score"
            :class="{blue: index == 0, navy : index == 1 ,green : index==2}"
            >{{item.score}}</div>
          <div class="cat_text">{{item.name}} Index</div>
          <div class="cat_text">Rank #{{item.rank}}/404</div>
        </div>
      </div>
    </div>
</div>
</template>

<script>
import store from '@/store/store.js'

export default {
  components: {
  },
  data: () => ({
    isHovering: -1,
    first_show: true,
    list: 1,
    msg: 'info',
    curdata: [],
    loc: null,
    AllScore: 80,
    Allrank: 1,
    cur_location_name: null,
    class_green: 'green'
  }),
  computed: {
    items () {
      var vm = this
      var target = store.state.cur_location
      if (target != this.loc) {
        this.loc = target
        this.$axios.get('http://127.0.0.1:8000/nsr/detail/' + target).then(function (response) {
           vm.curdata = response.data
        })
        this.$axios.get('http://127.0.0.1:8000/nsr/getname/' + target).then(function (response) {
           vm.cur_location_name = response.data
        })
        this.$axios.get('http://127.0.0.1:8000/nsr/getvibrancyrank/' + target).then(function (response) {
           vm.Allrank = response.data
        })
      }
      var s = vm.curdata
      var sum = 0
      for(var i in s){
        sum = sum + s[i].score
      }
      this.AllScore = (sum/3).toFixed(2)
      return vm.curdata
    },
    max_value () {
      return store.state.vibrancy_max
    },
    min_value () {
      return store.state.vibrancy_min
    }

  },
  watch: {
  },
  methods: {
    onMouseOver: function (index) {
      this.isHovering = index
    },
    onMouseOut: function () {
      this.isHovering = -1
    },
    onMouseClick: function (index) {
      if (index === 0) {
        this.list = this.list + 1
        this.msg = 'CULTURE'
      }
      if (index === 1) {
        this.msg = 'SUSTAINABILITY'
      }
      if (index === 2) {
        this.msg = 'OPPORTUNITY'
      }
      store.commit('change_indexname', this.msg)
      store.commit('change_explore_showmore', this.first_show)
      store.commit('change_explore_showblock', !this.first_show)
    },
    calculateAll: function () {
      var s = vm.curdata
      var sum = 0
      for(var i in s){
        sum = sum + s[i].score
      }
      this.AllScore = (sum/3).toFixed(2)
    }
  }
}

</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Muli|Rubik|Cabin|Dosis|Josefin+Sans|Nunito+Sans|Quicksand|Raleway:300,300i,400,400i,500,500i,700,700i&display=swap');

#viewDiv {
  height: 100%;
  width: 100%;
  z-index: 1;
}

.blocks_container{
  background-color: white;
  border-radius: 5px;
  border: 0.5px;
  box-shadow: 0px 0px 5px #CDCFD1;
  width: 23%;
  height: 80%;
  position: absolute;
  left: 5%;
  top:20%;
  z-index: 1;
}

.sum_info{
  height: 20%;
  margin-top: 10px;
  margin-bottom: 10px;
}

.sum_info_score{
  font-family: 'Raleway', sans-serif;
  font-size: 25px;
}

.cat_text{
  height: 20px;
  width: 100%;s
  color: #A2A5A8;
  font_family:'Lato', sans-serif;
  font-weight: 200;
  font-size: 15px;
}

.title {
  font-family: 'Oswald', 'Helvetica Neue', Arial, Helvetica, sans-serif;
  font-weight: Bold;
  font-size: 25px;
  margin-left: 13px;
  margin-top: 15px;
}

.split{
  width: 100%;
}

.top{
  margin-left: 20px;
  margin-right: 10px;
  width: 100%;
  height: 22%;
}

.bot{
  position: absolute;
  margin-left: 20px;
  margin-right: 10px;
  width: 85%;
  height: 70%;
}
.allscore{
  color: #FBA92A;
  font_family:'Montserrat', sans-serif;
  font-weight: 300;
  font-size: 30px;
}

.a_score{
  font_family:'Montserrat', sans-serif;
  font-weight: Light;
}

.hover_block_choose{
  background-color : #CDCFD1;
}

.first{
  display: none;
}

.indexinfo{
  width: 100%;
  height: 30%;
}

.green {
  color: #6BBC45;
}

.blue {
  color: #00B0D9;
}

.navy {
  color: #5469A2;
}
</style>
