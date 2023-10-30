import React, { useEffect, useState } from "react";
import "./ProductTable.css";
import { getProducts } from "./api/InventoryAPI";

const ProductTable = () => {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    getProducts().then((products) => setProducts(products));
  }, []);

  console.log(products);

  return (
    <div className="table-container">
      {" "}
      <table className="product-table">
        <thead>
          <tr>
            <th className="table-header">Product Name</th>
            <th className="table-header">Price</th>
            <th className="table-header">Stock Count</th>
          </tr>
        </thead>
        <tbody>
          {products.map((product, index) => (
            <tr key={index} className="table-row">
              <td>{product.product_name}</td>
              <td>{product.price}</td>
              <td>{product.stock_count}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
};

export default ProductTable;
