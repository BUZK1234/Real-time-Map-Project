var map = L.map('map').setView([0, 0], 2);  // Initialize the map

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png').addTo(map);

var data = [];  // Store the CSV data

var route = L.polyline([], { color: 'blue' }).addTo(map);  // Create an empty polyline
var marker = L.marker([0, 0]).addTo(map);  // Create a marker

var dataIndex = 0;  // Index to track the data point

function updateMap() {
    if (dataIndex < data.length) {
        var point = data[dataIndex];
        marker.setLatLng([point.lat, point.lon]);  // Update the marker

        var latLngs = data.slice(0, dataIndex + 1).map(function (point) {
            return [point.lat, point.lon];
        });

        route.setLatLngs(latLngs);  // Update the route

        dataIndex++;
    }
}

function fetchData() {
    fetch('/get_data')
        .then(response => response.json())
        .then(newData => {
            data = newData;
        });
}

fetchData();  // Initial data load
updateMap();  // Initial update
setInterval(updateMap, 500);  // Update every 1 second
setInterval(fetchData, 500);  // Fetch new data every 5 seconds
