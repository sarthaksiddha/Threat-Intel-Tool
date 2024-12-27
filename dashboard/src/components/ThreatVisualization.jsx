import React from 'react';
import { ForceGraph2D } from 'react-force-graph';

const ThreatVisualization = ({ data }) => {
  const graphData = {
    nodes: data.nodes.map(node => ({
      id: node.id,
      name: node.name,
      val: node.severity,
      color: getSeverityColor(node.severity)
    })),
    links: data.relationships.map(rel => ({
      source: rel.source,
      target: rel.target,
      value: rel.strength
    }))
  };

  return (
    <ForceGraph2D
      graphData={graphData}
      nodeLabel="name"
      nodeColor="color"
      linkWidth={1}
      nodeRelSize={6}
      onNodeClick={handleNodeClick}
    />
  );
};

export default ThreatVisualization;