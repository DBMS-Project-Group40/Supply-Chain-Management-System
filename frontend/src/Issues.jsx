import React from "react";
import "./Issues.css";

function Issues() {
  const dummyData = [
    {
      RouteID: 101,
      City: "New York",
      start_location: "Central Park",
      end_location: "Times Square",
      time_to_leave: "9:00 AM",
      Duration: "30 mins",
    },
  ];

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
          {dummyData.map((route, index) => (
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
