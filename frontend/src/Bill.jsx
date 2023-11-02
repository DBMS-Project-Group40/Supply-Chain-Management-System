import React, { useEffect, useState } from "react";
import "./Bill.css";
import {
  getBillById,
  getBills,
  getOrdersByCustomer,
  getUser,
} from "./api/InventoryAPI";

function Bill() {
  const [billDate, setBillDate] = useState(null);
  const [totalListPrice, setTotalListPrice] = useState(0.0);
  const [discountPercent, setDiscountPercent] = useState(null);
  const [totalDiscountedPrice, setTotalDiscountedPrice] = useState(0.0);
  const [customerID, setCustomerId] = useState(null);
  const [billID, setBillID] = useState(null);
  const [billData, setBillData] = useState(null);
  const [email, setEmail] = useState(null);

  // Load the userEmail from localStorage when the component mounts

  var savedEmail = "";
  useEffect(() => {
    savedEmail = localStorage.getItem("userEmail");
    if (savedEmail) {
      setEmail(savedEmail);
    }
  }, []);

  const dummyData = {
    billDate: billDate,
    totalListPrice: totalListPrice,
    discountPercent: discountPercent,
    totalDiscountedPrice: totalDiscountedPrice,
  };

  useEffect(() => {
    async function fetchCustomerId() {
      try {
        const customer = await getUser(savedEmail);
        setCustomerId(customer.ID);
        console.log("customer id ", customer.ID);
      } catch (error) {
        console.error("Error fetching customer ID:", error);
      }
    }

    fetchCustomerId();
  }, [savedEmail]);

  useEffect(() => {
    getOrdersByCustomer(customerID)
      .then((orders) => {
        const extractedBillID = orders.length > 0 ? orders[0].BillID : null;
        setBillID(extractedBillID);
      })
      .catch((error) => {
        console.error("Error fetching orders:", error);
      });
  }, [customerID]);

  useEffect(() => {
    getBillById(billID)
      .then((bill) => {
        setBillData(bill);
        setBillDate(bill.BillDate);
        setDiscountPercent(bill.discount_percent);
        setTotalListPrice(bill.total_list_price);
        setTotalDiscountedPrice(bill.total_discounted_price);
      })
      .catch((error) => {
        console.error("Error: in bill fetching ", error);
      });
  }, [billID]);

  return (
    <div className="bill-container">
      <h1>User Bill</h1>
      <div className="bill-input">
        <label>Bill Date:</label>
        <input
          type="date"
          value={billDate}
          onChange={(e) => setBillDate(e.target.value)}
          readOnly
        />
      </div>
      <div className="bill-input">
        <label>Total List Price:</label>
        <input
          type="number"
          value={totalListPrice}
          onChange={(e) => setTotalListPrice(parseFloat(e.target.value))}
          readOnly
        />
      </div>
      <div className="bill-input">
        <label>Discount Percent:</label>
        <input
          type="number"
          value={discountPercent}
          onChange={(e) => setDiscountPercent(parseInt(e.target.value, 10))}
          readOnly
        />
      </div>
      <div className="bill-input">
        <label>Total Discounted Price:</label>
        <input
          type="number"
          value={totalDiscountedPrice}
          onChange={(e) => setTotalDiscountedPrice(parseFloat(e.target.value))}
          readOnly
        />
      </div>
    </div>
  );
}

export default Bill;
