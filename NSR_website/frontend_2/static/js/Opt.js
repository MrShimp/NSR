function loadmap(){
	var map = new google.maps.Map(d3.select("#map").node(), {
	  zoom: 11,
	  center: new google.maps.LatLng(40.440624, -79.995888)
	});

	var overlay = new google.maps.OverlayView();
	overlay.onAdd = function() {}
	overlay.draw = function() {}
	overlay.setMap(map);

	function googleProjection(prj) {
	  return function(lnglat) {
	    ret = prj.fromLatLngToDivPixel(new google.maps.LatLng(lnglat[1],lnglat[0]))
	    return [ret.x, ret.y]
	  };
	}
	map.addListener('idle', function() {
	  var svg;
	  var path;

	  if(!svg) {
	    var projection = googleProjection(overlay.getProjection());
	    var northWest = projection([40.677695, -80.265123]);
	    var southEast = projection([40.079919, -79.728817]);
	    var width = southEast[0] - northWest[0];
	    var height = southEast[1] - northWest[1];
	    svg = d3.select(overlay.getPanes().overlayMouseTarget)
	            .append("svg")
				.style("top", northWest[1])
				.style("left", northWest[0])
	            .attr("height", 960)
	            .attr("width", 680);
	    path = d3.geo.path().projection(projection);
	  }

	  // add handler to clear svg contents on zoom change
	  map.addListener('zoom_changed', function() {
	    if(svg) {
	      svg.selectAll("*").remove();
	    }
	  });

	  // add handler to clear svg contents on drag drop
	  map.addListener('dragend', function() {
	    if(svg) {
	      svg.selectAll("*").remove();
	    }
	  });

	  d3.json('Allegheny_County_Census_Tracts_2016.geojson', function(error, data) {
	  	console.log(data.features);
	    svg.append("g")
	      .selectAll("path")
	      .data(data.features)
	      .enter().append("path")
	      .attr("d", path)
	      .attr("fill", "#666666")
	      .attr("fill-opacity", 0.3)
	      .attr("stroke", "black");
	  });
	});

	var tipSvg = d3.select('body').append('div')
	  .style('position', 'absolute')
	  .style('max-width', '400px')
	  .style('height', 'auto')
	  .style('background-color', '#ffffff')
	  .style('opacity', 0)
	  .style('width', 600)
	  .on("mouseover", mapMouseOver)
      .on("mouseout", mapMouseOut);
	// Load the station data. When the data comes back, create an overlay.


	function mapMouseOver(d) {
	  var tip = '<p>' + d.properties.nsw_loca_2 + '</p>';
	  tipSvg.html(tip)
	      .style('left', (d3.event.pageX) + 'px')
	      .style('top', (d3.event.pageY) + 'px');
	  tipSvg.transition()
	      .duration(500)
	      .style('opacity', 1);
	}

	function mapMouseOut(d) {
	  tipSvg.transition()
	        .duration(500)
	        .style('opacity', 0);
	}
}




function initialize() {
  loadmap();
}
