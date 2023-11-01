import { useState } from "react";
import {
  BrowserRouter,
  Route,
  Routes,
  Outlet,
  Navigate,
} from "react-router-dom";
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
  const [userEmail, setUserEmail] = useState("");

  const OpenSidebar = () => {
    setOpenSidebarToggle(!openSidebarToggle);
  };

  return (
    <BrowserRouter>
      <Layout OpenSidebar={OpenSidebar}>
        <Routes>
          <Route
            path="/login"
            element={<Login setUserEmail={setUserEmail} />}
          />
          <Route path="/register" element={<RegisterForm />} />
          <Route path="/" element={<ProtectedRoutes />}>
            <Route index element={<Home />} />
            <Route path="/products" element={<ProductTable />} />
            <Route path="/orders" element={<OrderForm />} />
          </Route>
        </Routes>
      </Layout>
    </BrowserRouter>
  );
}

function ProtectedRoutes() {
  const isUserLoggedIn = localStorage.getItem("isUserLoggedIn");

  if (isUserLoggedIn !== "true") {
    return <Navigate to="/login" />;
  }

  return <Outlet />;
}

export default App;
