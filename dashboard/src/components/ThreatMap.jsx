import React from 'react';
import { ComposableMap, Geographies, Geography, Marker } from 'react-simple-maps';

const ThreatMap = ({ data }) => {
  const geoUrl = "https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json";

  return (
    <div className="w-full h-96">
      <ComposableMap>
        <Geographies geography={geoUrl}>
          {({ geographies }) =>
            geographies.map((geo) => (
              <Geography
                key={geo.rsmKey}
                geography={geo}
                fill="#EAEAEC"
                stroke="#D6D6DA"
              />
            ))
          }
        </Geographies>
        {data.map((threat, index) => (
          <Marker key={index} coordinates={[threat.longitude, threat.latitude]}>
            <circle r={5} fill="#FF5533" stroke="#fff" strokeWidth={2} />
          </Marker>
        ))}
      </ComposableMap>
    </div>
  );
};

export default ThreatMap;