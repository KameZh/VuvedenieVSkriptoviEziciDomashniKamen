import { useState } from 'react';

/**
 * Sidebar displaying list of trails
 */
export default function Sidebar({ trails, onFindNearby, userLocation, activeTrailId, onTrailClick }) {
    const [isOpen, setIsOpen] = useState(true);

    return (
        <div className={`sidebar ${isOpen ? 'open' : 'closed'}`}>
            <div className="sidebar-header">
                <h1>Gorski BG Trails</h1>
                <button className="toggle-btn" onClick={() => setIsOpen(!isOpen)}>
                    {isOpen ? '◀' : '▶'}
                </button>
            </div>

            <div className="sidebar-content">
                <button
                    className="btn-primary"
                    onClick={onFindNearby}
                    title="Find trails near you"
                >
                    📍 Find Nearby Trails
                </button>

                {userLocation && <p className="status-text">✅ Location found</p>}

                <div className="trails-list">
                    {trails.map(trail => (
                        <div
                            key={trail.id}
                            className={`trail-card ${activeTrailId === trail.id ? 'active' : ''}`}
                            onClick={() => onTrailClick(trail)}
                        >
                            <h3>{trail.name}</h3>
                            <div className="trail-meta">
                                <span className={`difficulty ${trail.difficulty.toLowerCase()}`}>{trail.difficulty}</span>
                                <span>📏 {trail.length}</span>
                            </div>
                            <p className="trail-region">{trail.region}</p>
                            {trail.distance !== undefined && (
                                <p className="trail-dist">Run: {trail.distance.toFixed(1)} km away</p>
                            )}
                        </div>
                    ))}
                </div>
            </div>
        </div>
    );
}
