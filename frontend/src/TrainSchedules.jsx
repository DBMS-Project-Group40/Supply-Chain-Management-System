import React, { useEffect, useState } from "react";
import Modal from "react-modal";
import TrainScheduleOrder from "./TrainScheduleOrder";
import "./TrainSchedules.css";
import { getUser, getOrdersByCustomer } from "./api/InventoryAPI";

Modal.setAppElement("#root");

function TrainSchedules() {
  const [selectedOrder, setSelectedOrder] = useState(null);
  const [orders, setOrders] = useState([]);
  const [userEmail, setUserEmail] = useState("");

  useEffect(() => {
    const storedEmail = localStorage.getItem("userEmail");
    if (storedEmail) {
      setUserEmail(storedEmail);
      getUser(storedEmail)
        .then((userData) => {
          getOrdersByCustomer(userData.ID)
            .then((orderData) => {
              setOrders(orderData);
            })
            .catch((error) => {
              console.error("Error fetching orders:", error);
            });
        })
        .catch((error) => {
          console.error("Error fetching user:", error);
        });
    }
  }, []);

  return (
    <div className="orders-list">
      <h1>Orders for Trains</h1>
      <p>User Email: {userEmail}</p>
      <ul>
        {orders?.length > 0 ? (
          orders.map((order) => (
            <li key={order.OrderID} onClick={() => setSelectedOrder(order)}>
              OrderID: {order.OrderID}, BillID: {order.BillID}, CustomerID:{" "}
              {order.CustomerID}, RouteID: {order.RouteID}
            </li>
          ))
        ) : (
          <li>No orders available.</li>
        )}
      </ul>
      {selectedOrder && (
        <Modal isOpen={true} onRequestClose={() => setSelectedOrder(null)}>
          <TrainScheduleOrder
            order={selectedOrder}
            onClose={() => setSelectedOrder(null)}
          />
        </Modal>
      )}
    </div>
  );
}

export default TrainSchedules;
