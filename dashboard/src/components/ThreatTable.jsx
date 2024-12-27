import React from 'react';
import { Table, Badge } from '@/components/ui';

export const ThreatTable = ({ threats }) => (
  <Table>
    <Table.Header>
      <Table.Row>
        <Table.Head>Type</Table.Head>
        <Table.Head>Indicator</Table.Head>
        <Table.Head>Severity</Table.Head>
        <Table.Head>Source</Table.Head>
        <Table.Head>Confidence</Table.Head>
      </Table.Row>
    </Table.Header>
    <Table.Body>
      {threats.map((threat) => (
        <Table.Row key={threat.id}>
          <Table.Cell>{threat.type}</Table.Cell>
          <Table.Cell>{threat.value}</Table.Cell>
          <Table.Cell>
            <Badge variant={getSeverityColor(threat.severity)}>
              {threat.severity}
            </Badge>
          </Table.Cell>
          <Table.Cell>{threat.source}</Table.Cell>
          <Table.Cell>{threat.confidence}%</Table.Cell>
        </Table.Row>
      ))}
    </Table.Body>
  </Table>
);