<template>
  <div class="google-map" :id="mapName">
	</div>
</template>

<script>
import store from '@/store/store.js'

export default {
  name: 'google-map',
  props: ['name'],
  data: function () {
    return {
      mapName: this.name + '-map',
      map: null,
      bounds: null,
      cur_fea: null,
      colorData: [],
      all_vibrancy_data: [],
      zoom_num: 11,
      cur_color_boundary: [51.8, 55.48, 58.552]
    }
  },
  created: function () {
    var vm = this;
    this.$axios.get('http://127.0.0.1:8000/nsr/explore/target' ).then(function (response) {
      vm.colorData = response.data
    })
    store.commit('change_all_color_data', this.colorData)
  },
  mounted: function () {
    this.bounds = new google.maps.LatLngBounds();
    const element = document.getElementById(this.mapName)
    const options = {
      center: this.center,
			zoom: this.zoom_num
    }
    this.map = new google.maps.Map(element, options)
    this.map.data.setStyle(this.styleFeature)
    this.map.data.addListener('mouseover', this.mouseInToRegion)
    this.map.data.addListener('mouseout', this.mouseOutOfRegion)
    this.map.data.addListener('mousedown', this.mouseClickRegion)
    var vm = this
    this.map.data.loadGeoJson('../../../static/data/Allegheny_County_Census_Tracts_2016.json', { idPropertyName: 'GEOID' },
      function (features) {
         vm.$options.methods.loadCensusData(vm.map, vm.colorData);
    });
  },
  computed: {
    center () {
      if (store.state.cur_center != {lat: 40.440624, lng: -79.995888}) {
        this.zoom_num = 15
      }
      return store.state.cur_center
    },
    color_feature () {
      return store.state.selected_feature
    },
    index () {
      return store.state.indexname
    }
  },
  watch: {
    color_feature (newval) {
      this.loadCensusData(this.map, this.colorData)
    },
    index () {
      this.loadCensusData(this.map, this.colorData)
    }
  },
	methods: {
		loadCensusData: function (map, data) {
        var censusData = data
        var new_array = []
        var vm = this
				censusData.forEach(function(row) {
          var censusVariable = 0
          if(store.state.indexname == 'all'){
            censusVariable = parseInt(row['Vibrant_Index'])
          }else{
            if(store.state.indexname == 'culture'){
              censusVariable = parseInt(row['Cult_Index'])
            }else if(store.state.indexname == 'sustainability'){
              censusVariable = parseInt(row['Sust_Index'])
            }else{
              censusVariable = parseInt(row['Opt_Index'])
            }
            var selected = store.state.selected_feature
            for(var i = 0; i<selected.length; i++){
              censusVariable += parseInt(row[selected[i]])
            }
            censusVariable = censusVariable/(selected.length+1)
          }
          new_array.push(censusVariable)
          vm.all_vibrancy_data = new_array
					var stateId = row['GEOID']
          if(map.data.getFeatureById(stateId)){
            map.data.getFeatureById(stateId).setProperty('score', censusVariable)
          }
				})
		},
		styleFeature: function (feature) {
	    var partyColours = ['#FF0000', '#ff9d00', '#FFFF00', '#008000']
      var boundary = this.cur_color_boundary
	    if (feature.getProperty('score') > boundary[2]) {
	      return {
            strokeColor: '#fff',
            fillColor: partyColours[3],
            fillOpacity: 0.4
	        }
	    }
      if (feature.getProperty('score') > boundary[1] && feature.getProperty('score')<boundary[2]) {
	      return {
            strokeColor: '#fff',
            fillColor: partyColours[2],
            fillOpacity: 0.4
	        }
	    }
	    if (feature.getProperty('score') > boundary[0] && feature.getProperty('score') < boundary[1]) {
	      return {
            strokeColor: '#fff',
            fillColor: partyColours[1],
            fillOpacity: 0.4
	        }
	    }
	    return {
	          strokeColor: '#fff',
	          fillColor: partyColours[0],
	          fillOpacity: 0.4
	    }
	  },
	  mouseInToRegion: function (e) {
	        e.feature.setProperty('state', 'hover')
	  },
	  mouseOutOfRegion: function (e) {
	    e.feature.setProperty('state', 'normal')
	  },
    mouseClickRegion: function (e) {
      store.state.cur_location = e.feature.getId()
      this.map.setZoom(15);
      this.map.setCenter(e.latLng)
    },
    getrank: function () {
      var cur = this.all_vibrancy_data.sort()
      var len = cur.length
      store.commit('change_vibrancy_min', cur[0])
      store.commit('change_vibrancy_max', cur[len-1])
      var cur_boundary = [cur[100], cur[200], cur[300]]
      this.cur_color_boundary = cur_boundary
      store.commit('change_color_boundary', cur_boundary)
    }
  }
};
</script>

<style scoped>
.google-map {
  width: 100%;
  height: 100%;
  margin: 0 auto;
  background: gray;
}
</style>
