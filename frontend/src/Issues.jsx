import React, { useState, useEffect } from "react";
import "./Issues.css";
import axios from "axios";
import { getUser, get_assigned_route_for_driver } from "./api/InventoryAPI";

function Issues() {
  console.log("HI HI");
  const [driverRouteData, setDriverRouteData] = useState([]);

  useEffect(() => {
    // Step 1: Get userEmail from local storage
    const userEmail = localStorage.getItem("userEmail");

    // Step 2: Fetch the driver's ID using the userEmail
    getUser(userEmail)
      .then((userData) => {
        const driverID = userData.ID;

        // Step 3: Get the route data using the driver's ID
        return get_assigned_route_for_driver(driverID);
      })
      .then((routeData) => {
        setDriverRouteData(routeData);
      })
      .catch((error) => {
        console.error("Error fetching data", error);
      });
  }, []); // Empty dependency array ensures this effect runs only once when the component mounts

  return (
    <div className="table-container">
      <table>
        <thead>
          <tr>
            <th>Route ID</th>
            <th>City</th>
            <th>Start Location</th>
            <th>End Location</th>
            <th>Time to Leave</th>
            <th>Duration</th>
          </tr>
        </thead>
        <tbody>
          {driverRouteData.map((route, index) => (
            <tr key={index}>
              <td>{route.RouteID}</td>
              <td>{route.City}</td>
              <td>{route.start_location}</td>
              <td>{route.end_location}</td>
              <td>{route.time_to_leave}</td>
              <td>{route.Duration}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Issues;
