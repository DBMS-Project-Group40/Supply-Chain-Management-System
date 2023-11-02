import React, { useState, useEffect } from "react";
import { useFormik } from "formik";
import * as Yup from "yup";
import "./OrderForm.css";
import { getStoreAndEndLocation } from "./api/InventoryAPI";

const TrainScheduleOrder = ({ order, onClose }) => {
  const [storeLocations, setStoreLocations] = useState([]);

  useEffect(() => {
    console.log("Effect is running");

    async function fetchData() {
      try {
        const response = await getStoreAndEndLocation();
        setStoreLocations(response);
        console.log("Raw response:", response);

        if (response && Array.isArray(response.data)) {
          setStoreLocations(response.data);
        }
      } catch (error) {
        console.error("Error fetching store locations", error);
      }
    }
    fetchData();
  }, []);

  const formik = useFormik({
    initialValues: {
      train: "",
      sendingQuantity: "",
      endLocation: "",
    },
    validationSchema: Yup.object({
      train: Yup.string().required("Train is required"),
      sendingQuantity: Yup.number()
        .required("Sending Quantity is required")
        .positive("Quantity must be positive")
        .integer("Quantity must be an integer"),
      endLocation: Yup.string().required("End Location is required"),
    }),
    onSubmit: (values) => {
      console.log(values);
      onClose();
    },
  });

  return (
    <div>
      <h2>Schedule Train for Order: {order?.product}</h2>
      <form onSubmit={formik.handleSubmit}>
        <div>
          <label htmlFor="train">Train: </label>
          <select
            id="train"
            name="train"
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
            value={formik.values.train}
          >
            <option value="" label="Select a train" />
            {storeLocations.map((store) => (
              <option key={store.StoreID} value={`train${store.StoreID}`}>
                Train to store with ID of {store.StoreID} to{" "}
                {store.end_location}
              </option>
            ))}
          </select>
          {formik.touched.train && formik.errors.train && (
            <div className="error">{formik.errors.train}</div>
          )}
        </div>
        <div>
          <label htmlFor="sendingQuantity">Sending Quantity: </label>
          <input
            id="sendingQuantity"
            name="sendingQuantity"
            type="number"
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
            value={formik.values.sendingQuantity}
          />
          {formik.touched.sendingQuantity && formik.errors.sendingQuantity && (
            <div className="error">{formik.errors.sendingQuantity}</div>
          )}
        </div>
        <div>
          <label htmlFor="endLocation">End Location: </label>
          <select
            id="endLocation"
            name="endLocation"
            onChange={formik.handleChange}
            onBlur={formik.handleBlur}
            value={formik.values.endLocation}
          >
            <option value="" label="Select an end location" />
            {storeLocations.map((store) => (
              <option key={store.StoreID} value={store.end_location}>
                {store.end_location}
              </option>
            ))}
          </select>
          {formik.touched.endLocation && formik.errors.endLocation && (
            <div className="error">{formik.errors.endLocation}</div>
          )}
        </div>
        <button class="btn btn-submit" type="submit">
          Submit
        </button>
        <button class="btn btn-close" type="button" onClick={onClose}>
          Close
        </button>
      </form>
    </div>
  );
};

export default TrainScheduleOrder;
