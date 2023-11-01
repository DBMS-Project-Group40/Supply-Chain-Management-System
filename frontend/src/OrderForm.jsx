import React, { useState, useEffect } from "react";
import { getProducts, getRoutes, getRoutesByCity } from "./api/InventoryAPI";
import "./OrderForm.css";

const OrderForm = ({ onOrderSubmit }) => {
  const [customerID, setCustomerID] = useState("");
  const [selectedProduct, setSelectedProduct] = useState("");
  const [quantity, setQuantity] = useState("");
  const [route, setRoute] = useState("");
  const [routes, setRoutes] = useState([]);
  const [products, setProducts] = useState([]);
  const [cityRoutes, setCityRoutes] = useState([]);
  const [selectedCity, setSelectedCity] = useState("");

  useEffect(() => {
    if (selectedCity) {
      getRoutesByCity(selectedCity).then((data) => {
        setCityRoutes(data);
      });
    }
  }, [selectedCity]);

  useEffect(() => {
    getRoutes().then((r) => setRoutes(r));

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

      <label className="form-label">City:</label>
      <select
        value={selectedCity}
        onChange={(e) => setSelectedCity(e.target.value)}
        required
        className="form-select"
      >
        <option value="">Select a City</option>
        {routes.map((route) => (
          <option key={route.RouteID} value={route.City}>
            {route.City}
          </option>
        ))}
      </select>

      {selectedCity && (
        <div className="form-group">
          <label className="form-label">Route:</label>
          <p>
            {cityRoutes[0].start_location} to {cityRoutes[0].end_location}
          </p>
        </div>
      )}

      <button type="submit" className="submit-button">
        Place Order
      </button>
    </form>
  );
};

export default OrderForm;
