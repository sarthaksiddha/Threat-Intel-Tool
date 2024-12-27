import React from 'react';
import { ResponsiveTreeMap } from '@nivo/treemap';

const ImpactAnalysis = ({ data }) => (
  <div className="h-96">
    <ResponsiveTreeMap
      data={data}
      identity="name"
      value="impact"
      valueFormat=".0%"
      margin={{ top: 10, right: 10, bottom: 10, left: 10 }}
      labelSkipSize={12}
      labelTextColor={{ from: 'color', modifiers: [['darker', 1.2]] }}
      parentLabelPosition="left"
      parentLabelTextColor={{ from: 'color', modifiers: [['darker', 2]] }}
      borderColor={{ from: 'color', modifiers: [['darker', 0.1]] }}
    />
  </div>
);