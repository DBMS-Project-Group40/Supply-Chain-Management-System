import React from "react";
import { useLocation } from "react-router-dom";
import Header from "./Header";
import Sidebar from "./SideBar";

function Layout({ children, OpenSidebar }) {
  const location = useLocation();
  const isLoginPage = location.pathname === "/login";
  const isRegisterPage = location.pathname === "/register";

  return (
    <div className={!(isLoginPage || isRegisterPage) ? `grid-container` : ``}>
      {!(isLoginPage || isRegisterPage) && <Header OpenSidebar={OpenSidebar} />}
      {!(isLoginPage || isRegisterPage) && (
        <Sidebar OpenSidebar={OpenSidebar} />
      )}
      {children}
    </div>
  );
}

export default Layout;
