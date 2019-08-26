<template>
  <div class="index_container">
    <mynavbar></mynavbar>
    <!-- map behind title -->
    <div class = "below_map">
      <test></test>
    </div>
    <!-- left title and other -->
    <div class = "title_on_map" v-if = "!search_show">
      <div class = "introduction">
        <h1 class="introduction_title">Welcome to New Sun Rising's Vibrancy Index Dashboard!</h1>
        <h2 class="introduction_content">This tool is designed to help you gain deeper insight into socioeconomic conditions in your community. Our goal is to encourage strategic investments into local assets based upon these needs. The Vibrancy Index Dashboard displays data organized by the United Nations Sustainable Development Goals (UN SDGs).
Enter an address to view a specific census tract or explore freely by clicking the map. While in the 'Explore' page, you can research the following data in Allegheny County:</h2>
        <span class="text">1.Indexes for Vibrancy, Culture, Sustainability, and Opportunity</span>
        <span class="text">2.Raw data for specific socioeconomic indicators aligned with the UN SDGs</span>
        <span class="text">3.Ranking of your census tract index compared to others in Allegheny County</span>
        <h2 class="introduction_content" style="float:left; margin-right: 80%;">Guide of Site</h2>
        <span class="text">1.Click start to enter your address or skip to view the general map</span>
        <span class="text">2.Click indexes of Culture, Sustainability, and Opportunity to see the detail</span>
        <span class="text">3.Click different tracts on the map to see the data in that tract</span>
      </div>
      <div class = "guide">
        <button class="explore_button"
          v-on:click="startbuttonclick">
          START
        </button>
      </div>
    </div>
    <div class="search_on_map"
      v-if = "search_show"
      v-on: click = "hide">
      <search></search>
    </div>

  </div>
</template>

<style scoped>
.index_container {
  height : 100%;
  width : 100%;
  background-color: white;
}

.below_map{
  position: absolute;
  width : 80%;
  height : 400px;
  top: 20%;
  left: 10%;
  opacity: 0.2;
  z-index: 1;
}

.title_on_map{
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  z-index: 2;
}

.guide {
  position: absolute;
  left: 10%;
  top: 100%;
}
.search_on_map{
  position: absolute;
  top: 50%;
  left: 35%;
  z-index: 2;
}

.introduction{
  margin-left: 10%;
  margin-top: 5%;
}

.introduction_title{
  color : #1C3854;
  font-family: 'Oswald', 'Helvetica Neue', Arial, Helvetica, sans-serif;
  font-size: 30px;
}

.introduction_content{
  margin-top : 30px;
  color : #1C3854;
  font_family:'Lato', sans-serif;
  font-size: 20px;
  opacity: 0.8;
  font-weight: 260;
}

.explore_button{
  margin-top: 30px;
  width: 150px;
  height: 45px;
  border-radius: 5px;
  border: none;
  background-color: #F68331;
  color: #EDEDED;
  font-family: 'Oswald', 'Helvetica Neue', Arial, Helvetica, sans-serif;
  font-size: 15px;
  font-weight: 400;
  background-size: 7px 7px;
  background-image: radial-gradient(white 5%, transparent 0), radial-gradient(white 15%, transparent 0);
}

.search_container{
  height: 100%;
  width: 100%;
  background: black;
  z-index: 2;
}

.text {
  float: left;
  color : #1C3854;
  font_family:'Lato', sans-serif;
}

</style>

<script>
import Mynavbar from '@/components/navbar.vue'
import Test from '@/components/test.vue'
import Search from '@/components/search.vue'

export default{
  components: {
    Mynavbar,
    Test,
    Search
  },
  data: function () {
    return {
      search_show: false
    }
  },
  methods: {
    startbuttonclick: function () {
      this.search_show = true
    },
    hide: function () {
      this.search_show = false
    }
  }
}
</script>
