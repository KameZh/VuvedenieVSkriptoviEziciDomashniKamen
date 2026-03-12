import { useEffect, useRef, useState } from 'react';
import tt from '@tomtom-international/web-sdk-maps';
import '@tomtom-international/web-sdk-maps/dist/maps.css';

const API_KEY = import.meta.env.VITE_TOMTOM_API_KEY;

export default function MapContainer({ trails, userLocation, activeTrail, onMarkerClick, onCloseInfoWindow }) {
    const mapElement = useRef(null);
    const [map, setMap] = useState(null);
    const markersRef = useRef([]);
    const popupRef = useRef(null);

    // Initialize Map
    useEffect(() => {
        if (!mapElement.current || map) return;

        if (!API_KEY) {
            console.error("TomTom API Key is missing. Please add VITE_TOMTOM_API_KEY to your .env file.");
            return;
        }

        const mapInstance = tt.map({
            key: API_KEY,
            container: mapElement.current,
            center: userLocation ? [userLocation.lng, userLocation.lat] : [25.4858, 42.7339], // [lng, lat]
            zoom: userLocation ? 9 : 7,
            style: `https://api.tomtom.com/map/1/style/20.0.0-8/basic_main.json?key=${API_KEY}`,
        });

        mapInstance.addControl(new tt.NavigationControl(), 'top-right');
        setMap(mapInstance);

        return () => {
            mapInstance.remove();
        };
    }, [mapElement]);

    // Update Center when userLocation changes (only once or on explicit demand to avoid fighting user pan)
    useEffect(() => {
        if (map && userLocation) {
            map.flyTo({
                center: [userLocation.lng, userLocation.lat],
                zoom: 9
            });

            // Add User Location Marker
            const element = document.createElement('div');
            element.className = 'marker-user';
            element.style.backgroundImage = 'url("https://cdn-icons-png.flaticon.com/512/149/149071.png")'; // Simple user icon
            element.style.width = '30px';
            element.style.height = '30px';
            element.style.backgroundSize = 'cover';
            element.style.borderRadius = '50%';
            element.style.border = '2px solid white';
            element.style.boxShadow = '0 0 10px rgba(0,0,0,0.5)';

            new tt.Marker({ element })
                .setLngLat([userLocation.lng, userLocation.lat])
                .addTo(map);
        }
    }, [map, userLocation]);

    // sync Markers with Trails
    useEffect(() => {
        if (!map) return;

        // Clear existing markers
        markersRef.current.forEach(marker => marker.remove());
        markersRef.current = [];

        // Add new markers
        trails.forEach(trail => {
            const element = document.createElement('div');
            element.className = 'marker-trail';

            // Color coding based on difficulty
            let color = '#6366f1';
            switch (trail.difficulty) {
                case 'Easy': color = '#22c55e'; break;
                case 'Moderate': color = '#f59e0b'; break;
                case 'Hard': color = '#ef4444'; break;
                case 'Extreme': color = '#000000'; break;
            }

            element.style.backgroundColor = color;
            element.style.width = '24px';
            element.style.height = '24px';
            element.style.borderRadius = '50% 50% 50% 0';
            element.style.transform = 'rotate(-45deg)';
            element.style.border = '2px solid white';
            element.style.cursor = 'pointer';
            element.style.boxShadow = '0 2px 4px rgba(0,0,0,0.3)';

            const marker = new tt.Marker({ element })
                .setLngLat([trail.location.lng, trail.location.lat])
                .addTo(map);

            marker.getElement().addEventListener('click', () => {
                onMarkerClick(trail);
            });

            markersRef.current.push(marker);
        });

    }, [map, trails, onMarkerClick]);

    // Handle Active Trail Popup
    useEffect(() => {
        if (!map || !activeTrail) {
            if (popupRef.current) {
                popupRef.current.remove();
                popupRef.current = null;
            }
            return;
        }

        if (popupRef.current) {
            popupRef.current.remove();
        }

        const popupContent = `
      <div style="padding: 10px; color: #0f172a; max-width: 200px;">
        <h3 style="margin: 0 0 5px 0; font-size: 16px;">${activeTrail.name}</h3>
        <p style="margin: 0 0 5px 0; font-size: 12px;">${activeTrail.difficulty} • ${activeTrail.length}</p>
        <p style="margin: 0; font-size: 12px; color: #334155;">${activeTrail.description.substring(0, 100)}...</p>
      </div>
    `;

        const popup = new tt.Popup({ offset: 30 })
            .setLngLat([activeTrail.location.lng, activeTrail.location.lat])
            .setHTML(popupContent)
            .addTo(map);

        // Close handler
        popup.on('close', () => {
            onCloseInfoWindow();
        });

        popupRef.current = popup;

        // Center map on active trail
        map.flyTo({
            center: [activeTrail.location.lng, activeTrail.location.lat],
            zoom: 10
        });

    }, [map, activeTrail, onCloseInfoWindow]);

    return (
        <div ref={mapElement} style={{ width: '100%', height: '100%', zIndex: 0 }} />
    );
}
