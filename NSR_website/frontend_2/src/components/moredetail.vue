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
        <span class="indicators_title">{{indexname}} Indicators</span>
        <div class="checkboxs">
            <div
              v-for="item in goals"
              class="checkbox left">
              <input type="checkbox"
                v-bind:id="item.name"
                v-bind:value = "item.name"
                v-model = "checkedFeature" >
              <span class="indicators_font">{{item.SDG}}</span>
              <span></span>
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
        v-for="item in cur_rowdata"
        class="row_data_item">
        <span class="indicators_font">{{item.name}}:  {{item.value}}</span>
        <hr class="split_2"></hr>
      </div>
    </div>
  </div>
</div>
</template>

<script>
import store from '@/store/store.js'
import json from '@/assets/total_selected.json'

export default {
  data: function () {
    return {
      goals: [],
      row_data: [],
      cur_rowdata: [],
      cur: null
    }
  },
  created: function () {
    this.getAlldata()
  },
  mounted () {
  },
  computed: {
    indexname () {
      this.getRawData()
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
      var hash = new Map()
      hash.set('Goal_2', ['INDI_2_2', 'INDI_2_1'])
      hash.set('Goal_1', ['INDI_1_21n1_fam', 'INDI_1_21n1_sing_women', 'INDI_1_31n4', 'INDI_1_31n3', 'INDI_1_31n7', 'INDI_1_31n8'])
      hash.set('Goal_3', ['INDI_3_41n1', 'INDI_3_41n3', 'INDI_3_41n2', 'INDI_3_51n3', 'INDI_3_61n1'])
      hash.set('Goal_4', ['INDI_4_22n1', 'INDI_4_31n1', 'INDI_4_31n2', 'INDI_4_31n3', 'INDI_4_31n4', 'INDI_4_31n5', 'INDI_4_31n6'])
      hash.set('Goal_5', ['INDI_5_1'])
      hash.set('Goal_6', ['INDI_6_31n3', 'INDI_6_31n2'])
      hash.set('Goal_7', ['INDI_7_12n1', 'INDI_7_1', 'INID_11_71n1 .'])
      hash.set('Goal_8', ['INDI_8_52n1', 'INDI_8_61n1', 'INDI_8_61n2_1', 'INDI_8_61n2_2'])
      hash.set('Goal_9', ['INDI_9_22n1', 'INDI_9_c1n1'])
      hash.set('Goal_10', ['INDI_10_2', 'INDI_10_3'])
      hash.set('Goal_11', ['INDI_10_2', 'INDI_10_3'])
      hash.set('Goal_12', ['12_toxic_release_of_air'])
      hash.set('Goal_15', ['INDI_15_1.1n1'])
      var cur_raw = []
      var cur_feature = store.state.selected_feature
      if (cur_feature) {
        var len = cur_feature.length
        for (var i=0; i<len; i++) {
          var cur_indicator = hash.get(cur_feature[i])
          var len2 = this.row_data.length
          for (var j=0; j<len2; j++) {
            if (cur_indicator.includes(this.row_data[j]['id'])) {
              cur_raw.push(this.row_data[j])
            }
          }
        }
        this.cur_rowdata = cur_raw
      }
      if(cur_raw.length < 1){
        this.cur_rowdata = this.row_data
      }
    },
    getAlldata: function () {
      var vm = this
      this.$axios.get('static/data/total_selected.json' ).then(function (response) {
        vm.cur = response.data
      })
    },
    getRawData: function () {
      var map = new Map()
      map.set('INDI_2_2', "Percent of population that is obese")
      map.set('INDI_2_1', "Percent of population receiving SNAP benefits")
      map.set('INDI_1_21n1_fam', "Current poverty levels as defined by USA, by sections of the population. {woman}")
      map.set('INDI_1_21n1_sing_women', "Current poverty levels as defined by USA, by sections of the population. {parents}")
      map.set('INDI_1_31n4', "Percent of people covered by at least one social protection benefit, by sections of the population")
      map.set('INDI_1_31n3', "Percentage of population receiving TANF, by sections of the population.")
      map.set('INDI_1_31n7', "Percent of people with severe disabilities receiving disability cash benefit, by sections of the population")
      map.set('INDI_1_31n8', "Percent of people receiving unemployment cash benefit, by sex, or other relevant sections of population, by sections of the population")
      map.set('INDI_3_41n1', "Percent of people with cardiovascular disease, by section of population")
      map.set('INDI_3_41n3', "Percent of people with diabetes disease, by section of population")
      map.set('INDI_3_41n2', "Percent of people with cancer, by section of population")
      map.set('INDI_3_61n1', "Number or percent of people who are experiencing issues with substance abuse and/or addiction")
      map.set('INDI_4_22n1', "Percentage of 2, 3, and 4 year children attending preschool programs, by section of population")
      map.set('INDI_4_31n1', "Percentage of adults with did not complete high school or high school equivalency, by section of population")
      map.set('INDI_4_31n2', "Percentage of adults that the highest educational level is high school or high school equivalency, by section of population.")
      map.set('INDI_4_31n3', "Percentage of adults who have attending college, by section of population.")
      map.set('INDI_4_31n4', "Percentage of adults with did not complete high school or high school equivalency, by section of population")
      map.set('INDI_4_31n5', "Percentage of adults who have earned a 4 year degree, by section of population.")
      map.set('INID_11_71n1', "Sustainable Cities & Communities")
      map.set('INDI_10_2', "Income distribution")
      map.set('INDI_10_3', "Racial segregation")
      map.set('INDI_3_51n3', "Number or percent of people who are experiencing issues with substance abuse and/or addiction")
      map.set('INDI_5_1', "Median earnings gap between women and men")
      map.set('INDI_4_31n6', "Percentage of adults who have earned a Graduate degree or higher, by section of population.")
      map.set('INDI_8_52n1', "Unemployment rate, by section of population.")
      map.set('INDI_8_61n1', "Employment rate of youth ages 15 - 21, by section of the population.")
      map.set('INDI_8_61n2_1', "Pecentage of High school completion rate, for people over 25 years old")
      map.set('INDI_8_61n2_2', "Pecentage of High school completion rate, for people between 18 and 24 years old")
      map.set('8_Disc_labor', "Percentage of 15 to 24 years old that participate in the workforce")
      map.set('8_Disc_sc_enroll', "Percentage of 15 to 24 years old that are enrolled in the school")
      map.set('8_STEM_major', "Percentage of Adults (>=25) that get a Bachelor degree from a STEM field, as percentage of total people with a bachelor degree")
      map.set('INDI_9_22n1', "Ratio of manufacturing jobs to all jobs, by section of population.")
      map.set('INDI_9_c1n1', "Availability of high speed data services. (percentage of homes)")
      map.set('11_inad_plum', "Percentage of house with no plumbing system")
      map.set('11_inad_rooms', "Percentage of house with more than one people living in each room")
      map.set('11_use_pub_trans', "Percentage of workers that use public transportation when they don't work at home, and they have vehicles available")
      map.set('11_Earn_lessthan_35K_30p_house_cost', "Housing cost as percentage of household income, families that earn less than 35K yearly")
      map.set('11_percent_of_renters', "Percentage as renters of total households")
      map.set('INDI_6_31n3', "Number of Green Infrastructure projects.")
      map.set('INDI_6_31n2', "Typical Year Overflow Volume (MG) by sewershed.")
      map.set('INDI_7_12n1', "Percent of population with primary reliance on clean fuels and technology, by sections of populations. ")
      map.set('INDI_7_1', "Household utility costs")
      map.set('INID_11_71n1 .', "Number of parks and green space.")
      map.set('11_Walkability_Score', "Walkability Score")
      map.set('12_toxic_release_of_air', "Lbs toxic release of air, water, and land per sq mile")
      map.set('INDI_15_1.1n1', "Forest are in square miles")
      map.set('15_green_open_space', "Green open space meters per capita")
      if(this.cur){
        var len = this.cur.length
        for(var i=0; i<len; i++){
          if(this.cur[i]['GEOID'] == "42003010300"){
            for (var obj in this.cur[i]) {
              this.row_data.push({
                'id': obj,
                'name': map.get(obj)? map.get(obj):obj,
                'value': this.cur[i][obj]
              });
            }
          }
        }
        this.cur_rowdata = this.row_data
      }
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
    height: 55%;
    margin-top: 50%;
  }

  .row_data {
    overflow: auto;
    height: 85%;
    font_family:'Lato', sans-serif;
  }

  .row_data_item{
    width:100%;
  }

  .split_2{
    width: 20%;
  }
</style>
