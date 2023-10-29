import React from "react";
import { useLocation } from "react-router-dom";
import Header from "./Header";
import Sidebar from "./SideBar";

function Layout({ children, OpenSidebar }) {
  const location = useLocation();
  const isLoginPage = location.pathname === "/login";

  return (
    <div className={!isLoginPage ? `grid-container` : ``}>
      {!isLoginPage && <Header OpenSidebar={OpenSidebar} />}
      {!isLoginPage && <Sidebar OpenSidebar={OpenSidebar} />}
      {children}
    </div>
  );
}

export default Layout;
