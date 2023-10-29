import { useState } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./App.css";
import Home from "./Home";
import "./index.css";
import ProductTable from "./ProductTable";
import OrderForm from "./OrderForm";
import Login from "./LoginForm";
import Layout from "./Layout";
import RegisterForm from "./RegisterForm";

function App() {
  const [openSidebarToggle, setOpenSidebarToggle] = useState(false);

  const OpenSidebar = () => {
    setOpenSidebarToggle(!openSidebarToggle);
  };

  return (
    <BrowserRouter>
      <Layout OpenSidebar={OpenSidebar}>
        <Routes>
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<RegisterForm />} />
          <Route path="/" element={<Home />} />
          <Route path="/products" element={<ProductTable />} />
          <Route path="/orders" element={<OrderForm />} />
        </Routes>
      </Layout>
    </BrowserRouter>
  );
}

export default App;
