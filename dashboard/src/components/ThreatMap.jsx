import React from 'react';
import { ComposableMap, Geographies, Geography, Markers } from 'react-simple-maps';

export const ThreatMap = ({ threats }) => (
  <ComposableMap>
    <Geographies geography={geoUrl}>
      {({ geographies }) =>
        geographies.map((geo) => (
          <Geography
            key={geo.rsmKey}
            geography={geo}
            fill="#DDD"
            stroke="#FFF"
          />
        ))
      }
    </Geographies>
    {threats.map((threat) => (
      <Marker key={threat.id} coordinates={[threat.longitude, threat.latitude]}>
        <circle r={4} fill="#F00" />
      </Marker>
    ))}
  </ComposableMap>
);