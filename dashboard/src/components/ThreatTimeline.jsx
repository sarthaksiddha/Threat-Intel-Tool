import React from 'react';
import { LineChart, Line, XAxis, YAxis, Tooltip, ResponsiveContainer } from 'recharts';

const ThreatTimeline = ({ data }) => {
  const processedData = data.map(threat => ({
    time: new Date(threat.timestamp).toLocaleTimeString(),
    severity: threat.severity
  }));

  return (
    <ResponsiveContainer width="100%" height={300}>
      <LineChart data={processedData}>
        <XAxis dataKey="time" />
        <YAxis domain={[0, 10]} />
        <Tooltip />
        <Line type="monotone" dataKey="severity" stroke="#8884d8" />
      </LineChart>
    </ResponsiveContainer>
  );
};

export default ThreatTimeline;