import React from "react";
import { Link } from "react-router-dom";
import {
  BsCart3,
  BsGrid1X2Fill,
  BsFillArchiveFill,
  BsFillGrid3X3GapFill,
  BsPeopleFill,
  BsListCheck,
  BsMenuButtonWideFill,
  BsExclamationCircleFill,
  BsCardChecklist,
  BsFillGearFill,
  BsPeople,
  BsFileEarmarkText,
  BsCalendar,
} from "react-icons/bs";
import { FiLogOut } from "react-icons/fi";
import { useNavigate } from "react-router-dom";

function Sidebar({ openSidebarToggle, OpenSidebar }) {
  const navigation = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem("isUserLoggedIn");
    navigation("/login");
  };

  return (
    <aside
      id="sidebar"
      className={openSidebarToggle ? "sidebar-responsive" : ""}
    >
      <div className="sidebar-title">
        <div className="sidebar-brand">
          <BsCart3 className="icon_header" /> SHOP
        </div>
        <span className="icon close_icon" onClick={OpenSidebar}>
          X
        </span>
      </div>

      <ul className="sidebar-list">
        <li className="sidebar-list-item">
          <Link to="/">
            <BsGrid1X2Fill className="icon" /> Dashboard
          </Link>
        </li>
        <li className="sidebar-list-item">
          <Link to="/products">
            <BsFillArchiveFill className="icon" /> Products
          </Link>
        </li>
        <li className="sidebar-list-item">
          <Link to="/categories">
            <BsFillGrid3X3GapFill className="icon" /> Categories
          </Link>
        </li>
        <li className="sidebar-list-item">
          <Link to="/customers">
            <BsPeopleFill className="icon" /> Customers
          </Link>
        </li>
        <li className="sidebar-list-item">
          <Link to="/managers">
            <BsPeople className="icon" /> Managers
          </Link>
        </li>
        <li className="sidebar-list-item">
          <Link to="/orders">
            <BsCart3 className="icon" /> Orders
          </Link>
        </li>
        <li className="sidebar-list-item">
          <Link to="/bills">
            <BsFileEarmarkText className="icon" /> Bills
          </Link>
        </li>
        <li className="sidebar-list-item">
          <Link to="/reports">
            <BsMenuButtonWideFill className="icon" /> Reports
          </Link>
        </li>
        <li className="sidebar-list-item">
          <Link to="/driver-issues">
            <BsCardChecklist className="icon" /> Issues
          </Link>
        </li>
        <li className="sidebar-list-item">
          <Link to="/train-schedule">
            <BsCalendar className="icon" /> Train Schedule
          </Link>
        </li>
        <li className="sidebar-list-item logout-button" onClick={handleLogout}>
          <span>
            <FiLogOut className="icon" /> Logout
          </span>
        </li>
      </ul>
    </aside>
  );
}

export default Sidebar;
