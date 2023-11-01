import React, { useState, useEffect } from "react";
import { useFormik } from "formik";
import * as yup from "yup";
import {
  getProducts,
  getRoutes,
  getRoutesByCity,
  getUser,
  addOrder,
  addBill,
  addBillEntry,
  getProductById,
  getRouteIDByCity,
} from "./api/InventoryAPI";
import "./OrderForm.css";

const validationSchema = yup.object({
  userEmail: yup.string().required("User email is required"),
  selectedProduct: yup.string().required("Product is required"),
  quantity: yup
    .number()
    .required("Quantity is required")
    .positive("Quantity must be a positive number"),
  selectedCity: yup.string().required("City is required"),
});

const OrderForm = ({ onOrderSubmit }) => {
  const [routes, setRoutes] = useState([]);
  const [products, setProducts] = useState([]);
  const [cityRoutes, setCityRoutes] = useState([]);
  const [routeID, setRouteID] = useState(null);

  const handlePlaceOrder = async (orderData) => {
    try {
      console.log("email ", formik.values.userId);
      console.log(products);

      const product = await getProductById(orderData.productID);
      console.log(product);

      // // Find the product in the products array
      // const filteredProducts = products.filter(
      //   (p) => p.ProductID === orderData.productID
      // );
      // console.log("f products ", filteredProducts);

      // const product =
      //   filteredProducts.length > 0 ? filteredProducts[0] : undefined;
      // console.log("product ", product);

      // Throw an error if the product is not found
      if (!product) {
        throw new Error(`Product with ID ${orderData.productID} not found`);
      }

      // Create the Bill data using the found product's price
      const billData = {
        BillDate: new Date().toISOString().split("T")[0],
        total_list_price: orderData.quantity * product.price,
        discount_percent: 0,
        total_discounted_price: 0,
      };
      billData.total_discounted_price =
        billData.total_list_price * (1 - billData.discount_percent / 100);
      console.log("bill data ", billData);
      const createdBill = await addBill(billData);

      // Then create the BillEntry using the BillID from the created Bill
      console.log("createdBill ", createdBill);
      console.log("createdBill.BillID ", createdBill.BillID);
      console.log("orderData.productID ", orderData.productID);
      console.log("orderData.quantity ", orderData.quantity);
      const billEntryData = {
        BillID: createdBill.BillID,
        ProductID: orderData.productID,
        quantity: orderData.quantity,
      };

      const createdBillEntry = await addBillEntry(billEntryData);

      // Finally, create the Order using the BillID and other required data
      console.log("createdBill.BillID ", createdBill.BillID);
      console.log("orderData.customerID ", orderData.customerID);
      console.log("orderData.route_id ", orderData.route_id);
      console.log("routeID ", routeID);

      const finalOrderData = {
        BillID: createdBill.BillID,
        CustomerID: orderData.customerID,
        RouteID: routeID,
      };
      const createdOrder = await addOrder(finalOrderData);

      onOrderSubmit(createdOrder);
    } catch (error) {
      console.error("Error while placing the order:", error);
      // Handle error appropriately, e.g., show an error message to the user
    }
  };

  const formik = useFormik({
    initialValues: {
      customerID: "",
      selectedProduct: "",
      quantity: "",
      route: "",
      userEmail: "",
      userId: "",
      selectedCity: "",
    },
    validationSchema: validationSchema,
    onSubmit: (values) => {
      const orderData = {
        customerID: values.customerID,
        productID: values.selectedProduct,
        quantity: values.quantity,
        route: values.route,
      };

      handlePlaceOrder(orderData);
      formik.resetForm();
    },
  });

  useEffect(() => {
    if (formik.values.selectedCity) {
      getRouteIDByCity(formik.values.selectedCity)
        .then((id) => {
          setRouteID(id);
        })
        .catch((error) => {
          console.error(error.message);
          setRouteID(null);
        });
    }
  }, [formik.values.selectedCity]);

  useEffect(() => {
    const fetchCustomerId = async () => {
      try {
        const customerData = await getUser(formik.values.userEmail);
        if (customerData && customerData.ID) {
          formik.values.customerID = customerData.ID;
        }
      } catch (error) {
        console.error("Error fetching customer ID:", error);
      }
    };

    if (formik.values.userEmail) {
      fetchCustomerId();
    }
  }, [formik.values.userEmail, formik.values.customerID]);

  useEffect(() => {
    const fetchUserId = async () => {
      try {
        const userData = await getUser(formik.values.userEmail);
        if (userData && userData.ID) {
          formik.setFieldValue("userId", userData.ID);
        }
      } catch (error) {
        console.error("Error fetching user ID:", error);
      }
    };

    if (formik.values.userEmail) {
      fetchUserId();
    }
  }, [formik.values.userEmail, formik.values.userId]);

  useEffect(() => {
    if (formik.values.selectedCity) {
      getRoutesByCity(formik.values.selectedCity).then((data) => {
        setCityRoutes(data);
      });
    }
  }, [formik.values.selectedCity]);

  useEffect(() => {
    getRoutes().then((r) => setRoutes(r));
    getProducts().then((pro) => setProducts(pro));
  }, []);

  return (
    <form onSubmit={formik.handleSubmit} className="order-form">
      <div className="form-group">
        <label className="form-label">Customer email:</label>
        <input
          type="text"
          name="userEmail"
          value={formik.values.userEmail}
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
          required
          className="form-input"
        />
        {formik.touched.userEmail && formik.errors.userEmail ? (
          <div className="error">{formik.errors.userEmail}</div>
        ) : null}
      </div>
      <div className="form-group">
        <label className="form-label">Product:</label>
        <select
          name="selectedProduct"
          value={formik.values.selectedProduct}
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
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
        {formik.touched.selectedProduct && formik.errors.selectedProduct ? (
          <div className="error">{formik.errors.selectedProduct}</div>
        ) : null}
      </div>

      <div className="form-group">
        <label className="form-label">Quantity:</label>
        <input
          type="number"
          name="quantity"
          value={formik.values.quantity}
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
          required
          className="form-input"
        />
        {formik.touched.quantity && formik.errors.quantity ? (
          <div className="error">{formik.errors.quantity}</div>
        ) : null}
      </div>

      <div className="form-group">
        <label className="form-label">City:</label>
        <select
          name="selectedCity"
          value={formik.values.selectedCity}
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
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
        {formik.touched.selectedCity && formik.errors.selectedCity ? (
          <div className="error">{formik.errors.selectedCity}</div>
        ) : null}
      </div>

      {formik.values.selectedCity && cityRoutes.length > 0 && (
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
