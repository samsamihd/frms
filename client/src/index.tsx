import React from "react";
import ReactDOM from "react-dom";
import { BrowserRouter as Router } from "react-router-dom";
import 'leaflet/dist/leaflet.css'
import "./assets/css/style.css";
import "bootstrap/dist/css/bootstrap.min.css";
import AppRouter from "./routes";

const App = () => {
  return (
    <Router>
      <AppRouter />
    </Router>
  );
};

ReactDOM.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>,
  document.getElementById("root")
);
