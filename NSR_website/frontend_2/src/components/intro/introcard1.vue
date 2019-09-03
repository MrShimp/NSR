<template>
  <div class="introcard">
    <div>
    </div>
    <div>
    </div>
    <div>
    <div>
  </div>
</template>

<style scoped>
  .introcard{
    height: 30%;
    width: 40%
    border-radius: 5px;
    border: 0.5px;
    box-shadow: 0px 0px 5px #CDCFD1;
    background: linear-gradient(0.25turn, #84AEAC, #D6E1E1);
  }

</style>

<script>
import Search from '@/components/search.vue'
import Mynavbar from '@/components/navbar.vue'

export default {
  components: {
    Search,
    Mynavbar
  },
  data () {
    return {
      title: ''
    }
  }
}
</script>
