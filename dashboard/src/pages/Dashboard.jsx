import React, { useState, useEffect } from 'react';
import { Card } from '@/components/ui/card';
import { ThreatMap, ThreatTimeline, AlertsTable } from '../components';
import { Shield, AlertTriangle, Activity } from 'lucide-react';

const Dashboard = () => {
  const [data, setData] = useState({
    threats: [],
    alerts: [],
    metrics: {}
  });

  useEffect(() => {
    fetchDashboardData();
  }, []);

  return (
    <div className="p-6 space-y-6 overflow-auto">
      {/* Metrics */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
        <Card>
          <div className="p-6 flex items-center">
            <Shield className="w-12 h-12 text-blue-500" />
            <div className="ml-4">
              <h3 className="text-lg font-medium">Active Threats</h3>
              <p className="text-3xl font-bold">{data.metrics.activeThreats}</p>
            </div>
          </div>
        </Card>
        
        <Card>
          <div className="p-6 flex items-center">
            <AlertTriangle className="w-12 h-12 text-red-500" />
            <div className="ml-4">
              <h3 className="text-lg font-medium">Critical Alerts</h3>
              <p className="text-3xl font-bold">{data.metrics.criticalAlerts}</p>
            </div>
          </div>
        </Card>
        
        <Card>
          <div className="p-6 flex items-center">
            <Activity className="w-12 h-12 text-green-500" />
            <div className="ml-4">
              <h3 className="text-lg font-medium">System Status</h3>
              <p className="text-3xl font-bold">Healthy</p>
            </div>
          </div>
        </Card>
      </div>

      {/* Map and Timeline */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        <Card className="p-6">
          <h2 className="text-xl font-bold mb-4">Threat Map</h2>
          <ThreatMap data={data.threats} />
        </Card>
        
        <Card className="p-6">
          <h2 className="text-xl font-bold mb-4">Activity Timeline</h2>
          <ThreatTimeline data={data.threats} />
        </Card>
      </div>

      {/* Alerts Table */}
      <Card className="p-6">
        <h2 className="text-xl font-bold mb-4">Recent Alerts</h2>
        <AlertsTable data={data.alerts} />
      </Card>
    </div>
  );
};

export default Dashboard;