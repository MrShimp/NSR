<template>
<div class = "indexinfo_container">
  <div class = "indicators">
    <span class="indicators_title">{{cur_name}}Indicators</span>
    <div class="checkboxs">
        <div
          v-for="(item, index) in goals"
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
</template>

<script>
import store from '@/store/store.js'

export default {
  props:['cur_name'],
  data: function () {
    return {
      index_name: null
    }
  },
  computed: {
    checkedFeature: {
      get: function () {
        return store.state.selected_feature
      },
      set: function (value) {
        if(this.index_name == 'CULTURE'){
          store.commit('change_cul_selected_feature', value)
        }
        if(this.index_name == 'SUSTAINABILITY'){
          store.commit('change_sus_selected_feature', value)
        }
        if(this.index_name == 'OPPORTUNITY'){
          store.commit('change_opt_selected_feature', value)
        }
      }
    },
    goals: function () {
      console.log(this.index_name)
      var temp = []
      if(this.index_name == 'CULTURE'){
         temp = [
          {name: 'Goal_2', SDG: 'Zero Hunger'},
          {name: 'Goal_3', SDG: 'Good Health & Well-being'},
          {name: 'Goal_5', SDG: 'Gender Equality'},
          {name: 'Goal_10', SDG: 'Reduced Inequalities'},
          {name: 'Goal_11', SDG: 'Sustainable Cities & Communities'},
          {name: 'Goal_16', SDG: 'Peace, Justice, & Strong Institutions'}]
      }
      if(this.index_name == 'SUSTAINABILITY'){
        temp = [
          {name: 'Goal_6', SDG: 'Clean Water & Sanitation'},
          {name: 'Goal_7', SDG: 'Affordable & Clean Energy'},
          {name: 'Goal_11', SDG: 'Sustainable Cities & Communities'},
          {name: 'Goal_12', SDG: 'Responsible Consumption & Production'},
          {name: 'Goal_15', SDG: 'Life on Land'}]
      }
      if(this.index_name == 'OPPORTUNITY'){
        temp = [
          {name: 'Goal_1', SDG: 'No Poverty'},
          {name: 'Goal_4', SDG: 'Quality Education'},
          {name: 'Goal_8', SDG: 'Decent Work & Economic Growth'},
          {name: 'Goal_9', SDG: 'Industry, Innovation, & Infrastructure'},
          {name: 'Goal_11', SDG: 'Sustainable Cities & Communities'}]
       }
       return temp
    }
  },
  watch: {
    cur_name: function (newVal){
      this.index_name = newVal
    }
  },
  methods: {
  }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css?family=Muli|Rubik|Cabin|Dosis|Josefin+Sans|Nunito+Sans|Quicksand|Raleway:300,300i,400,400i,500,500i,700,700i&display=swap');

  .left{
    float: left;
  }

  .right{
    float: right;
  }

  .indexinfo_container{
    width: 100%;
    height: 30%;
    position: absolute;
  }

  .indicators {
    width: 95%;
    height: 60%;
    overflow: auto;
    margin-left: 10px;
  }

  .indicators_title{
    margin-top: 10px;
    margin-bottom: 10px;
  }

  .indicators_font{
    font-size: 12px;
    font_family:'Muli', sans-serif;
  }
  .checkboxs{
    width: 100%;
    height: 60%;
  }

  .checkbox{
    width: 50%;
  }
</style>
