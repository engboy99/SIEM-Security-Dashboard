import React, { useEffect, useState } from 'react';
import { Line } from 'react-chartjs-2';
import { Chart as ChartJS, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';

ChartJS.register(CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);

const LogChart = () => {
  const [logs, setLogs] = useState([]);
  const [data, setData] = useState({ labels: [], datasets: [{ data: [], label: "Log Events" }] });

  useEffect(() => {
    const fetchLogs = async () => {
      const response = await fetch('http://127.0.0.1:5000/logs');
      const logData = await response.json();
      setLogs(logData);
    };

    const interval = setInterval(fetchLogs, 5000);
    return () => clearInterval(interval);
  }, []);

  useEffect(() => {
    if (logs.length > 0) {
      const labels = logs.map(log => log.timestamp);
      const logCounts = logs.map(log => log.event_count);
      setData({
        labels: labels,
        datasets: [{ data: logCounts, label: "Log Events" }],
      });
    }
  }, [logs]);

  return (
    <div>
      <h2>Log Events Over Time</h2>
      <Line data={data} />
    </div>
  );
};

export default LogChart;
