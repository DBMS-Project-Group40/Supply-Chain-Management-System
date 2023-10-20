import { useState } from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import "./App.css";
import Header from "./Header";
import Sidebar from "./SideBar";
import Home from "./Home";
import "./index.css";
import ProductTable from "./ProductTable";

function App() {
  const [openSidebarToggle, setOpenSidebarToggle] = useState(false);

  const OpenSidebar = () => {
    setOpenSidebarToggle(!openSidebarToggle);
  };

  return (
    <div>
      <BrowserRouter>
        <div className="grid-container">
          <Header OpenSidebar={OpenSidebar} />
          <Sidebar
            openSidebarToggle={openSidebarToggle}
            OpenSidebar={OpenSidebar}
          />
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/products" element={<ProductTable />} />
          </Routes>
        </div>
      </BrowserRouter>
    </div>
  );
}

export default App;
