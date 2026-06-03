import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [stats, setStats] = useState({
    apps: 0,
    deployments: 0,
    running_deployments: 0,
    repositories: 0,
  });

  useEffect(() => {
  axios
    .get("http://127.0.0.1:8000/dashboard")
    .then((res) => {
      console.log(res.data);
      setStats(res.data);
    })
    .catch((err) => {
      console.log(err);
    });
}, []);

  return (
    <div style={{ padding: "30px" }}>
      <h1>🚀 Mini PaaS Dashboard</h1>

      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(4, 1fr)",
          gap: "20px",
          marginTop: "30px",
        }}
      >
        <div style={cardStyle}>
          <h2>Apps</h2>
          <h1>{stats.apps}</h1>
        </div>

        <div style={cardStyle}>
          <h2>Deployments</h2>
          <h1>{stats.deployments}</h1>
        </div>

        <div style={cardStyle}>
          <h2>Running</h2>
          <h1>{stats.running_deployments}</h1>
        </div>

        <div style={cardStyle}>
          <h2>Repositories</h2>
          <h1>{stats.repositories}</h1>
        </div>
      </div>
    </div>
  );
}

const cardStyle = {
  border: "1px solid #ddd",
  borderRadius: "10px",
  padding: "20px",
  textAlign: "center",
  boxShadow: "0 2px 10px rgba(0,0,0,0.1)",
};

export default App;