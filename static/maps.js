
    function initMap() {
        map = new google.maps.Map(document.getElementById("map"), {
          center: { lat: 51.509865, lng: -0.118092 },
          zoom: 9,
        });
      
      
          var labels = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
      
          var locations = [
              { lat: 51.509865, lng: -0.118092 },
          ];
      
          var markers = locations.map(function(location, i) {
              return new google.maps.Marker({
                  position: location,
                  label: labels[i % labels.length]
              });
          });
      
      var markerCluster = new MarkerClusterer(map, markers, { imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m' });
      }
      