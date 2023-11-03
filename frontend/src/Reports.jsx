import React, { useState, useEffect } from "react";
import { getTopProducts, getSalesByCityAndRoute } from "./api/InventoryAPI"; // Adjust the import to your actual path
import "./Report.css";

const Report = () => {
  const [products, setProducts] = useState([]);
  const [salesData, setSalesData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    Promise.all([getTopProducts(), getSalesByCityAndRoute()])
      .then(([productData, salesData]) => {
        setProducts(productData);
        setSalesData(salesData);
        setLoading(false);
      })
      .catch(() => {
        setLoading(false);
      });
  }, []);

  if (loading) {
    return <div>Loading...</div>;
  }

  return (
    <div className="report-container">
      <section>
        <h1>Top Products</h1>
        <table>
          <thead>
            <tr>
              <th>Product Name</th>
              <th>Order Count</th>
            </tr>
          </thead>
          <tbody>
            {products.map((product) => (
              <tr key={product.ProductID}>
                <td>{product.product_name}</td>
                <td>{product.OrderCount}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>

      <section>
        <h1>Sales Report by City and Route</h1>
        <table>
          <thead>
            <tr>
              <th>City</th>
              <th>Route</th>
              <th>Sales Count</th>
            </tr>
          </thead>
          <tbody>
            {salesData.map((sale, index) => (
              <tr key={index}>
                <td>{sale.City}</td>
                <td>{sale.Route}</td>
                <td>{sale.SalesCount}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </section>
    </div>
  );
};

export default Report;
