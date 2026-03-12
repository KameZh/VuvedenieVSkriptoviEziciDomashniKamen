import { useState, useMemo } from 'react';
import MapContainer from './components/MapContainer';
import Sidebar from './components/Sidebar';
import { trails as allTrails } from './data/trails';
import { getUserLocation, getDistanceFromLatLonInKm } from './utils/geolocation';

function App() {
  const [userLocation, setUserLocation] = useState(null);
  const [activeTrailId, setActiveTrailId] = useState(null);
  const [trails, setTrails] = useState(allTrails);

  const activeTrail = trails.find(t => t.id === activeTrailId);

  const handleFindNearby = async () => {
    try {
      const position = await getUserLocation();
      const location = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
      setUserLocation(location);

      // Calculate distances and sort
      const trailsWithDist = allTrails.map(trail => ({
        ...trail,
        distance: getDistanceFromLatLonInKm(
          location.lat,
          location.lng,
          trail.location.lat,
          trail.location.lng
        )
      })).sort((a, b) => a.distance - b.distance);

      setTrails(trailsWithDist);
    } catch (error) {
      alert("Could not get your location. Please enable location permissions.");
      console.error(error);
    }
  };

  const handleTrailClick = (trail) => {
    setActiveTrailId(trail.id);
  };

  return (
    <div className="app-container">
      <Sidebar
        trails={trails}
        onFindNearby={handleFindNearby}
        userLocation={userLocation}
        activeTrailId={activeTrailId}
        onTrailClick={handleTrailClick}
      />
      <MapContainer
        trails={trails}
        userLocation={userLocation}
        activeTrail={activeTrail}
        onMarkerClick={handleTrailClick}
        onCloseInfoWindow={() => setActiveTrailId(null)}
      />
    </div>
  );
}

export default App;
