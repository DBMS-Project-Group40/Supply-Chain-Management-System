import { useEffect, useState } from "react";
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
import Bill from "./Bill";
import TrainScheduleOrder from "./TrainScheduleOrder";
import TrainSchedules from "./TrainSchedules";
import Issues from "./Issues";
import Report from "./Reports";
import Managers from "./Managers";

function App() {
  const [openSidebarToggle, setOpenSidebarToggle] = useState(false);
  const [userEmail, setUserEmail] = useState("");

  useEffect(() => {
    const storedEmail = localStorage.getItem("userEmail");
    if (storedEmail) {
      setUserEmail(storedEmail);
    }
  }, []);

  console.log(userEmail);

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
            <Route path="/bills" element={<Bill />} />
            <Route path="/train-schedule" element={<TrainSchedules />} />
            <Route path="/driver-issues" element={<Issues />} />
            <Route path="/reports" element={<Report />} />
            <Route path="/managers" element={<Managers />} />
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
