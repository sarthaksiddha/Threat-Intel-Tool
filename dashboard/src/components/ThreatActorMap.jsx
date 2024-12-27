import React from 'react';
import { ComposableMap, Geographies, Geography, Line, Marker } from 'react-simple-maps';

const ThreatActorMap = ({ actors }) => (
  <div className="h-96">
    <ComposableMap projection="geoMercator">
      <Geographies geography="/world-110m.json">
        {({ geographies }) =>
          geographies.map(geo => (
            <Geography
              key={geo.rsmKey}
              geography={geo}
              fill="#DDD"
              stroke="#FFF"
              strokeWidth={0.5}
            />
          ))
        }
      </Geographies>
      {actors.map(actor => (
        <>
          <Marker coordinates={actor.origin}>
            <circle r={5} fill="#F00" />
            <text textAnchor="middle" y={-10}>{actor.name}</text>
          </Marker>
          {actor.targets.map(target => (
            <Line
              from={actor.origin}
              to={target.coordinates}
              stroke="#F00"
              strokeWidth={1}
              strokeDasharray="5,5"
            />
          ))}
        </>
      ))}
    </ComposableMap>
  </div>
);