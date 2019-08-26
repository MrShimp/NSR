<template>
<div class = "detail_container">
  <!-- top -->
  <div class = "top">
    <div class = "inside" style="margin-top: 10px;">
      <img class="goback" src="../assets/left.png" alt="" @click="goback">
      <span style="color: white;">{{indexname}} Index</span>
    </div>
  </div>
<!-- mid -->
  <div class="mid inside">
    <div class = "">
      <div class = "indicators">
        <span class="indicators_title">{{cur_name}}Indicators</span>
        <div class="checkboxs">
            <div
              v-for="item in goals"
              class="checkbox left">
              <input type="checkbox"
                v-bind:id="item.name"
                v-bind:value = "item.name"
                v-model = "checkedFeature" >
              <span class="indicators_font">{{item.SDG}}</span>
            </div>
        </div>
      </div>
    </div>
    <hr class="split"></hr>
  </div>
<!-- bot -->
  <div class="bot inside">
    <h6 class="title">Raw Data</h6>
    <div class="row_data">
      <div
        v-for="item in row_data"
        class="row_data_item">
        <span class="indicators_font">{{item.name}}:{{item.value}}</span>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import store from '@/store/store.js'

export default {
  data: function () {
    return {
      goals: [],
      row_data: [],
      cur_rowdata: []
    }
  },
  computed: {
    indexname () {
      var target = store.state.cur_location + ";" + store.state.indexname
      var vm = this
      this.$axios.get('http://127.0.0.1:8000/nsr/raw_data/' + target).then(function (response) {
        vm.row_data = response.data
        vm.cur_rowdata = response.data
      })
      if (store.state.indexname == 'CULTURE') {
         this.goals = [
          {name: 'Goal_2', SDG: 'Zero Hunger'},
          {name: 'Goal_3', SDG: 'Good Health & Well-being'},
          {name: 'Goal_5', SDG: 'Gender Equality'},
          {name: 'Goal_10', SDG: 'Reduced Inequalities'}]
      }
      if (store.state.indexname == 'SUSTAINABILITY') {
        this.goals = [
          {name: 'Goal_6', SDG: 'Clean Water & Sanitation'},
          {name: 'Goal_7', SDG: 'Affordable & Clean Energy'},
          {name: 'Goal_11', SDG: 'Sustainable Cities & Communities'},
          {name: 'Goal_12', SDG: 'Responsible Consumption & Production'},
          {name: 'Goal_15', SDG: 'Life on Land'}]
      }
      if (store.state.indexname == 'OPPORTUNITY') {
        this.goals = [
          {name: 'Goal_1', SDG: 'No Poverty'},
          {name: 'Goal_4', SDG: 'Quality Education'},
          {name: 'Goal_8', SDG: 'Decent Work & Economic Growth'},
          {name: 'Goal_9', SDG: 'Industry, Innovation, & Infrastructure'},
          {name: 'Goal_11', SDG: 'Sustainable Cities & Communities'}]
       }

      return store.state.indexname
    },
    checkedFeature: {
      get: function () {
        return store.state.selected_feature
      },
      set: function (value) {
        store.commit('change_selected_feature', value)
        this.showRow_data()
      }
    }
  },
  watched: {
  },
  methods: {
    goback: function () {
      var set = true
      store.commit('change_explore_showblock', set)
      store.commit('change_explore_showmore', !set)
      store.commit('change_indexname', 'all')
      store.commit('change_selected_feature', [])
    },
    showRow_data: function () {
      var hash = {}
      hash.put('goal_2', ['INDI_2_2', 'INDI_2_1'])
      hash.put('goal_1', ['INDI_1_21n1_fam', 'INDI_1_21n1_sing_women', 'INDI_1_31n4', 'INDI_1_31n3', 'INDI_1_31n7', 'INDI_1_31n8'])
      hash.put('goal_3', ['INDI_3_41n1', 'INDI_3_41n3', 'INDI_3_41n2', 'INDI_3_51n3', 'INDI_3_61n1'])
      hash.put('goal_4', ['INDI_4_22n1', 'INDI_4_31n1', 'INDI_4_31n2', 'INDI_4_31n3', 'INDI_4_31n4', 'INDI_4_31n5', 'INDI_4_31n6'])
      hash.put('goal_5', ['INDI_5_1'])
      hash.put('goal_6', ['INDI_6_31n3', 'INDI_6_31n2'])
      hash.put('goal_7', ['INDI_7_12n1', 'INDI_7_1', 'INID_11_71n1 .'])
      hash.put('goal_8', ['INDI_8_52n1', 'INDI_8_61n1', 'INDI_8_61n2_1', 'INDI_8_61n2_2'])
      hash.put('goal_9', ['INDI_9_22n1', 'INDI_9_c1n1'])
      hash.put('goal_10', ['INDI_10_2', 'INDI_10_3'])
      hash.put('goal_12', ['12_toxic_release_of_air'])
      hash.put('goal_15', ['INDI_15_1.1n1'])

      var cur_raw = []
      var cur_feature = store.state.selected_feature
      if (store.state.selected_feature) {
        for (var item in cur_feature) {
          var cur_indicator = hash.get(item)
          for (var data in this.raw_data) {
            if (cur_indicator.includes(data['id'])) {
              cur_raw.append(data)
            }
          }
        }
      }
      this.cur_rowdata = cur_raw
    }
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Lato:400,700|Montserrat:400,700|Oswald:200,300,700&display=swap');

.left{
  float: left;
}

.right{
  float: right;
}

.detail_container{
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

.top {
  font-family: 'Oswald', 'Helvetica Neue', Arial, Helvetica, sans-serif;
  font-weight: light;
  font-size: 20px;
  background-color: #5CC9F3;
  width: 100%;
  height: 10%;
  position: relative;
}

  .inside {
    margin:0 auto;
    position: absolute;
    left: 10%;
  }

  .mid {
    width: 90%;
    height: 35%;
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
    height: 30%;
    overflow: auto;
  }

  .indicators_title{
    margin-top: 10px;
    margin-bottom: 10px;
    font_family:'Montserrat', sans-serif;
  }

  .indicators_font{
    font-size: 13px;
    font_family:'Lato', sans-serif;
  }
  .checkboxs{
    width: 100%;
  }

  .checkbox{
    width: 50%;
  }

  .bot{
    width: 90%;
    height: 65%;
    margin-top: 32%;
  }

  .row_data {
    overflow: auto;
    height: 85%;
    font_family:'Lato', sans-serif;
  }

  .row_data_item{
    width:100%;
  }
</style>
