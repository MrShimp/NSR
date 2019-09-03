import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
export default new Vuex.Store({
  state: {
    indexname: 'all',
    explore_showblock: true,
    explore_showrank: false,
    explore_showpopup: false,
    explore_showmore: false,
    mapdata_num: null,
    cur_location: null,
    vibrancy_rank: 1,
    selected_feature:[],
    cur_center: {lat: 40.440624, lng: -79.995888},
    vibrancy_max: 65.278,
    vibrancy_min: 26.823,
    color_boundary: [51.8, 55.48, 58.552],
    all_color_data: []
  },
  getters: {

  },
  mutations: {
    change_indexname (state, data) {
      state.indexname = data
    },
    change_explore_showblock (state, data) {
      state.explore_showblock = data
    },
    change_explore_showrank (state, data) {
      state.explore_showrank = data
    },
    change_explore_showpopup (state, data) {
      state.explore_showpopup = data
    },
    change_explore_showmore (state, data) {
      state.explore_showmore = data
    },
    change_mapdata_num (state, data) {
      state.mapdata_num = data
    },
    change_cur_location (state, data) {
      state.cur_location = data
    },
    change_selected_feature (state, data) {
      state.selected_feature = data
    },
    change_cur_center (state, data) {
      state.cur_center = data
    },
    change_vibrancy_max (state, data) {
      state.vibrancy_max = data
    },
    change_vibrancy_min (state, data) {
      state.vibrancy_min = data
    },
    change_color_boundary (state, data) {
      state.color_boundary = data
    },
    change_all_color_data (state, data) {
      state.all_color_data = data
    },
    change_vibrancy_rank (state, data) {
      state.vibrancy_rank = data
    }
  },
  actions: {

  }

})
