import React, { useState, useEffect } from "react";
import { getProducts, getRoutes } from "./api/InventoryAPI";
import "./OrderForm.css";

const OrderForm = ({ onOrderSubmit }) => {
  const [customerID, setCustomerID] = useState("");
  const [selectedProduct, setSelectedProduct] = useState("");
  const [quantity, setQuantity] = useState("");
  const [route, setRoute] = useState("");
  const [routes, setRoutes] = useState([]);
  const [products, setProducts] = useState([]);

  useEffect(() => {
    // Fetch predefined routes from the backend.
    getRoutes().then((r) => setRoutes(r));

    // Fetch distinct products from the backend.
    getProducts().then((pro) => setProducts(pro));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();

    const orderData = {
      customerID,
      productID: selectedProduct,
      quantity,
      route,
    };

    onOrderSubmit(orderData);
  };

  return (
    <form onSubmit={handleSubmit} className="order-form">
      <div className="form-group">
        <label className="form-label">Customer email:</label>
        <input
          type="text"
          value={customerID}
          onChange={(e) => setCustomerID(e.target.value)}
          required
          className="form-input"
        />
      </div>

      <div className="form-group">
        <label className="form-label">Product:</label>
        <select
          value={selectedProduct}
          onChange={(e) => setSelectedProduct(e.target.value)}
          required
          className="form-select"
        >
          <option value="">Select a Product</option>
          {products.map((product) => (
            <option key={product.ProductID} value={product.ProductID}>
              {product.product_name}
            </option>
          ))}
        </select>
      </div>

      <div className="form-group">
        <label className="form-label">Quantity:</label>
        <input
          type="number"
          value={quantity}
          onChange={(e) => setQuantity(e.target.value)}
          required
          className="form-input"
        />
      </div>

      <div className="form-group">
        <label className="form-label">Route:</label>
        <select
          value={route}
          onChange={(e) => setRoute(e.target.value)}
          required
          className="form-select"
        >
          <option value="">Select a Route</option>
          {routes.map((r) => (
            <option key={r.RouteID} value={r.RouteID}>
              {r.start_location + " to " + r.end_location}
            </option>
          ))}
        </select>
      </div>

      <button type="submit" className="submit-button">
        Place Order
      </button>
    </form>
  );
};

export default OrderForm;
