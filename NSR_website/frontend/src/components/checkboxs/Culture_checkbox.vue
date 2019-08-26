<template>
<div class="checkboxs">
    <div class="checkbox">
      <input type="checkbox"
        aria-label="Checkbox for following text input"
        v-model = "checkedFeature" value="goal_1" id="goal_1">
      <span class="indicators_font">goal_1</span>
    </div>
    <div class="checkbox">
      <input type="checkbox"
        aria-label="Checkbox for following text input"
        v-model = "checkedFeature" value="goal_2" id="goal_2">
      <span class="indicators_font">goal_2</span>
    </div>
    <div class="checkbox">
      <input type="checkbox"
        aria-label="Checkbox for following text input"
        v-model = "checkedFeature" value="goal_3" id="goal_3">
      <span class="indicators_font">goal_3</span>
    </div>
    <div class="checkbox">
      <input type="checkbox"
        aria-label="Checkbox for following text input"
        v-model = "checkedFeature" value="goal_4" id="goal_4">
      <span class="indicators_font">goal_4</span>
    </div>
    <div class="checkbox">
      <input type="checkbox"
        aria-label="Checkbox for following text input"
        v-model = "checkedFeature" value="goal_5" id="goal_5">
      <span class="indicators_font">goal_5</span>
    </div>
    <span>{{checkedFeature}}</span>
</div>
</template>

<style scoped>
.checkboxs{
  width: 100%;
}

.checkbox{
  width: 50%;
  float: left;
}
</style>

<script>
import store from '@/store/store.js'

export default {
  data () {
    return {
      checkedFeature: []
    }
  },
  computed: {

  },
}
</script>
