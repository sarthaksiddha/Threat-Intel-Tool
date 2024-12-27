import React from 'react';
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow
} from "@/components/ui/table";

const AlertsTable = ({ data }) => {
  return (
    <Table>
      <TableHeader>
        <TableRow>
          <TableHead>Timestamp</TableHead>
          <TableHead>Type</TableHead>
          <TableHead>Severity</TableHead>
          <TableHead>Source</TableHead>
        </TableRow>
      </TableHeader>
      <TableBody>
        {data.map((alert, index) => (
          <TableRow key={index}>
            <TableCell>{new Date(alert.timestamp).toLocaleString()}</TableCell>
            <TableCell>{alert.type}</TableCell>
            <TableCell>
              <span className={`
                px-2 py-1 rounded text-xs
                ${alert.severity === 'High' ? 'bg-red-200 text-red-800' : 
                  alert.severity === 'Medium' ? 'bg-yellow-200 text-yellow-800' : 
                  'bg-green-200 text-green-800'}
              `}>
                {alert.severity}
              </span>
            </TableCell>
            <TableCell>{alert.source}</TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
};

export default AlertsTable;