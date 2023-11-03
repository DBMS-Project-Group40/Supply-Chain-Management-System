import React, { useState, useEffect } from "react";
import { getTransportManagers } from "./api/InventoryAPI"; // Adjust the import path as necessary
import "./Managers.css";

const Managers = () => {
  const [managers, setManagers] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    getTransportManagers()
      .then((data) => {
        setManagers(data);
        setLoading(false);
      })
      .catch((error) => {
        setError(error);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading...</p>;
  if (error) return <p>Error loading managers!</p>;

  return (
    <div className="managers-container">
      <h1 className="manager-topic">Managers</h1>
      <table className="managers-table">
        <thead>
          <tr>
            <th>Name</th>
            <th>Salary</th>
          </tr>
        </thead>
        <tbody>
          {managers.map((manager, index) => (
            <tr key={index}>
              <td>{manager.name}</td>
              <td>${parseFloat(manager.salary).toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default Managers;
