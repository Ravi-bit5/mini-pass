import { useEffect, useState } from "react";
import axios from "axios";

function App() {
  const [stats, setStats] = useState({
    apps: 0,
    deployments: 0,
    running_deployments: 0,
    repositories: 0,
  });

  const [apps, setApps] = useState([]);
  const [deployments, setDeployments] = useState([]);
  const [repositories, setRepositories] = useState([]);

  const [logs, setLogs] = useState([]);
  const [selectedDeployment, setSelectedDeployment] = useState(null);

  const [search, setSearch] = useState("");
  const [darkMode, setDarkMode] = useState(true);

  useEffect(() => {
    // Dashboard
    axios
      .get("http://127.0.0.1:8000/dashboard")
      .then((res) => setStats(res.data))
      .catch(console.error);

    // Apps
    axios
      .get("http://127.0.0.1:8000/apps")
      .then((res) => setApps(res.data))
      .catch(console.error);

    // Deployments
    axios
      .get("http://127.0.0.1:8000/deployments")
      .then((res) => setDeployments(res.data))
      .catch(console.error);

    // Repositories
    axios
      .get("http://127.0.0.1:8000/repositories")
      .then((res) => setRepositories(res.data))
      .catch(console.error);
  }, []);

  const loadLogs = (deploymentId) => {
    axios
      .get(`http://127.0.0.1:8000/deployments/${deploymentId}/logs`)
      .then((res) => {
        setLogs(res.data);
        setSelectedDeployment(deploymentId);
      })
      .catch(console.error);
  };

 const cardStyle = {
  background: "#1e293b",
  color: "white",
  borderRadius: "16px",
  padding: "25px",
  textAlign: "center",
  border: "1px solid #334155",
  boxShadow: "0 8px 25px rgba(0,0,0,0.25)",
};

const sectionCard = {
  background: "#111827",
  color: "white",
  padding: "20px",
  marginTop: "15px",
  borderRadius: "16px",
  border: "1px solid #334155",
  boxShadow: "0 8px 20px rgba(0,0,0,0.25)",
}; return (
  <div
    style={{
      display: "flex",
      minHeight: "100vh",
      background: darkMode ? "#0f172a" : "#f8fafc",
      color: darkMode ? "white" : "#111827",
      fontFamily: "Segoe UI, sans-serif",
    }}
  >
    {/* Sidebar */}
    <div
      style={{
        width: "250px",
        background: darkMode ? "#111827" : "#ffffff",
        padding: "25px",
        borderRight: "1px solid #374151",
      }}
    >
      <h2>🚀 Mini PaaS</h2>

      <div style={{ marginTop: "30px", lineHeight: "2.5" }}>
        <p>📊 Dashboard</p>
        <p>📦 Applications</p>
        <p>🚀 Deployments</p>
        <p>📜 Logs</p>
        <p>📚 Repositories</p>
        <p>⚙️ Settings</p>
      </div>
    </div>

    {/* Main Content */}
    <div
      style={{
        flex: 1,
        padding: "30px",
      }}
    >
      {/* Header */}
      <div
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <h1>🚀 Mini PaaS Dashboard</h1>

        <button
          onClick={() => setDarkMode(!darkMode)}
          style={{
            padding: "10px 15px",
            borderRadius: "10px",
            cursor: "pointer",
            border: "none",
          }}
        >
          {darkMode ? "☀️ Light" : "🌙 Dark"}
        </button>
      </div>

      {/* Welcome Banner */}
      <div
        style={{
          background: "#2563eb",
          padding: "20px",
          borderRadius: "16px",
          marginTop: "20px",
          marginBottom: "25px",
        }}
      >
        <h2>Welcome to Mini PaaS</h2>

        <p>
          Manage applications, deployments, repositories and logs from one place.
        </p>
      </div>

      {/* Stats Cards */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(4,1fr)",
          gap: "20px",
        }}
      >
        <div style={cardStyle}>
          <h3>📦 Apps</h3>
          <h1>{stats.apps}</h1>
        </div>

        <div style={cardStyle}>
          <h3>🚀 Deployments</h3>
          <h1>{stats.deployments}</h1>
        </div>

        <div style={cardStyle}>
          <h3>🟢 Running</h3>
          <h1>{stats.running_deployments}</h1>
        </div>

        <div style={cardStyle}>
          <h3>📚 Repositories</h3>
          <h1>{stats.repositories}</h1>
        </div>
      </div>

      {/* Search */}
      <h2 style={{ marginTop: "40px" }}>📦 Applications</h2>

      <input
        type="text"
        placeholder="Search applications..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
        style={{
          width: "100%",
          padding: "12px",
          marginTop: "15px",
          borderRadius: "10px",
          border: "1px solid #334155",
          marginBottom: "20px",
        }}
      />

      {apps
        .filter((app) =>
          app.name.toLowerCase().includes(search.toLowerCase())
        )
        .map((app) => (
          <div key={app.id} style={sectionCard}>
            <h3>{app.name}</h3>

            <p>
              <strong>Owner:</strong> {app.owner_email}
            </p>

            <p>
              <strong>Image:</strong> {app.image_name}
            </p>
          </div>
        ))}

      {/* Deployments */}
      <h2 style={{ marginTop: "40px" }}>🚀 Deployments</h2>

      {deployments.map((deployment) => (
        <div key={deployment.id} style={sectionCard}>
          <h3>Deployment #{deployment.id}</h3>

          <p>
            <strong>Status:</strong> {deployment.status}
          </p>

          <p>
            <strong>GitHub URL:</strong> {deployment.github_url}
          </p>

          <button
            onClick={() => loadLogs(deployment.id)}
            style={{
              padding: "10px 15px",
              borderRadius: "8px",
              cursor: "pointer",
            }}
          >
            View Logs
          </button>
        </div>
      ))}

      {/* Logs */}
      {selectedDeployment && (
        <>
          <h2 style={{ marginTop: "40px" }}>
            📜 Logs for Deployment #{selectedDeployment}
          </h2>

          <div
            style={{
              background: "#000",
              color: "#00ff00",
              padding: "20px",
              borderRadius: "10px",
              marginTop: "15px",
              fontFamily: "monospace",
            }}
          >
            {logs.map((log) => (
              <p key={log.id}>{log.message}</p>
            ))}
          </div>
        </>
      )}

      {/* Repositories */}
      <h2 style={{ marginTop: "40px" }}>📚 Repositories</h2>

      {repositories.map((repo) => (
        <div key={repo.name} style={sectionCard}>
          <h3>{repo.name}</h3>

          <p>
            <strong>Repository:</strong>{" "}
            <a
              href={repo.url}
              target="_blank"
              rel="noreferrer"
            >
              {repo.url}
            </a>
          </p>

          <p>
            ⭐ Stars: {repo.stars || 0}
          </p>

          <p>
            🍴 Forks: {repo.forks || 0}
          </p>
        </div>
      ))}
    </div>
  </div>
);
}

export default App;