<template>
  <div class="explore">
      <mynavbar></mynavbar>
      <div style="background-color:white;">
        <block
          v-if = "showblock"></block>
      </div>

      <!-- rankdetail -->
      <moredetail
        v-if = "showmore"
        ></moredetail>

      <div class = "map_layer">
        <testmap></testmap>
      </div>

      <colorinfo></colorinfo>
  </div>
</template>

<style scoped>
.explore {
  height: 100%;
}

.map_layer{
  height: 100%;
  width: 100%;
  z-index: -1;
}

.fade-enter-active, .fade-leave-active {
  transition: opacity .5s;
}
.fade-enter, .fade-leave-to {
  opacity: 0;
}
</style>


<script>
import Mynavbar from '@/components/navbar.vue'
import Block from '@/components/block.vue'
import Moredetail from '@/components/moredetail.vue'
import store from '@/store/store.js'
import Testmap from '@/views/testmap.vue'
import Colorinfo from '@/components/colorinfo'

export default{
  components: {
    Block,
    Mynavbar,
    Moredetail,
    Testmap,
    Colorinfo
  },
  data () {
    return {
    }
  },
  computed: {
    showmore () {
      return store.state.explore_showmore
    },
    curlocation () {
      return store.state.cur_location
    },
    showblock () {
      if(store.state.cur_location && store.state.explore_showblock){
        return true
      }
      return false
    }
  },
  methods: {
  }
}
</script>
