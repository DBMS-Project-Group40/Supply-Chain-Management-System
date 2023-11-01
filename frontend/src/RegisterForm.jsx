import React, { useEffect, useState } from "react";
import { useFormik } from "formik";
import * as Yup from "yup";
import "./RegisterForm.css";
import inventoryImage from "./assets/inventory4.png";
import { Link } from "react-router-dom";
import { addCustomer, addUser, getRoutes, getUser } from "./api/InventoryAPI";
import { customAlphabet } from "nanoid";
import { v4 as uuidv4 } from "uuid";

const RegisterSchema = Yup.object().shape({
  firstName: Yup.string().required("Please enter your first name"),
  middleName: Yup.string(), // middle name can be optional
  lastName: Yup.string().required("Please enter your last name"),
  email: Yup.string()
    .email("Invalid email address format")
    .required("Please enter your email address"),
  city: Yup.string().required("Please select a city"),
  password: Yup.string()
    .required("Please enter your password")
    .min(6, "Password must be at least 6 characters"),
  confirmPassword: Yup.string()
    .required("Please confirm your password")
    .oneOf([Yup.ref("password"), null], "Passwords must match"),
  role: Yup.string().required("Please select a role"),
  address: Yup.string().test(
    "required-for-customer",
    "Please enter your address",
    function (value) {
      if (this.parent.role === "customer") {
        return !!value;
      }
      return true;
    }
  ),
});

function RegisterForm() {
  const [cities, setCities] = useState([]);

  const formik = useFormik({
    initialValues: {
      firstName: "",
      middleName: "",
      lastName: "",
      email: "",
      city: "",
      password: "",
      confirmPassword: "",
      role: "",
      address: "",
    },
    validationSchema: RegisterSchema,
    validateOnMount: true,
    onSubmit: async (values) => {
      console.log("Submit");
      try {
        console.log(values.firstName);
        const newUser = {
          first_name: values.firstName,
          middle_name: values.middleName,
          last_name: values.lastName,
          email: values.email,
          role: values.role,
          password: values.password,
        };
        const response = await addUser(newUser);
        console.log("User added successfully:", response);

        if (values.role === "customer") {
          const uid = await getUser(values.email).then((d) => d.ID);
          try {
            const response_c = await addCustomer({
              CustomerID: uid,
              points: 0,
              City: values.city,
              address: values.address,
            });
            console.log("Customer added successfully:", response_c);
          } catch (error) {
            console.error("Error adding the customer:", error);
          }
        }

        formik.resetForm();
      } catch (error) {
        console.error("Error adding the user:", error);
      }
    },
  });

  useEffect(() => {
    const fetchCities = async () => {
      const routes = await getRoutes();
      console.log(routes);
      const uniqueCities = [...new Set(routes.map((route) => route.City))];
      setCities(uniqueCities);
    };
    fetchCities();
    console.log(cities);
  }, []);

  return (
    <div className="register-page">
      <div className="main-con">
        <h1 className="wellcome">JOIN US!</h1>
        <div className="container">
          <div className="img-container">
            <img src={inventoryImage} alt="Inventory Management" />
          </div>
          <form onSubmit={formik.handleSubmit} className="login-form">
            <div className="inside">
              <h1 className="login-text">Create an Account</h1>

              {/* First Name */}
              <div className="input-group">
                <label htmlFor="firstName">First Name</label>
                <input
                  type="text"
                  id="firstName"
                  name="firstName"
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  value={formik.values.firstName}
                />
                {formik.touched.firstName && formik.errors.firstName && (
                  <div className="error">{formik.errors.firstName}</div>
                )}
              </div>

              {/* Middle Name */}
              <div className="input-group">
                <label htmlFor="middleName">Middle Name</label>
                <input
                  type="text"
                  id="middleName"
                  name="middleName"
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  value={formik.values.middleName}
                />
                {formik.touched.middleName && formik.errors.middleName && (
                  <div className="error">{formik.errors.middleName}</div>
                )}
              </div>

              {/* Last Name */}
              <div className="input-group">
                <label htmlFor="lastName">Last Name</label>
                <input
                  type="text"
                  id="lastName"
                  name="lastName"
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  value={formik.values.lastName}
                />
                {formik.touched.lastName && formik.errors.lastName && (
                  <div className="error">{formik.errors.lastName}</div>
                )}
              </div>

              {/* Email */}
              <div className="input-group">
                <label htmlFor="email">Email</label>
                <input
                  type="email"
                  id="email"
                  name="email"
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  value={formik.values.email}
                />
                {formik.touched.email && formik.errors.email && (
                  <div className="error">{formik.errors.email}</div>
                )}
              </div>

              {/* Role */}
              <div className="input-group">
                <label htmlFor="role">Select a Role</label>
                <select
                  id="role"
                  name="role"
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  value={formik.values.role}
                >
                  <option value="" disabled>
                    Select a role
                  </option>
                  <option value="customer">Customer</option>
                  <option value="admin">Admin</option>
                  <option value="product_manager">Product Manager</option>
                  <option value="inventory_manager">Inventory Manager</option>
                  <option value="driver">Driver</option>
                </select>
                {formik.touched.role && formik.errors.role && (
                  <div className="error">{formik.errors.role}</div>
                )}
              </div>

              {/* Address (if role is customer) */}
              {formik.values.role === "customer" && (
                <div className="input-group">
                  <label htmlFor="address">Address</label>
                  <input
                    type="text"
                    id="address"
                    name="address"
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                    value={formik.values.address}
                  />
                  {formik.touched.address && formik.errors.address && (
                    <div className="error">{formik.errors.address}</div>
                  )}
                </div>
              )}
              {formik.values.role === "customer" && (
                <div className="input-group">
                  <label htmlFor="city">City</label>
                  <select
                    id="city"
                    name="city"
                    onChange={formik.handleChange}
                    onBlur={formik.handleBlur}
                    value={formik.values.city}
                  >
                    <option value="" disabled>
                      Select a city
                    </option>
                    {cities.map((city, index) => (
                      <option key={index} value={city}>
                        {city}
                      </option>
                    ))}
                  </select>

                  {formik.touched.city && formik.errors.city && (
                    <div className="error">{formik.errors.city}</div>
                  )}
                </div>
              )}

              {/* Password */}
              <div className="input-group">
                <label htmlFor="password">Password</label>
                <input
                  type="password"
                  id="password"
                  name="password"
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  value={formik.values.password}
                />
                {formik.touched.password && formik.errors.password && (
                  <div className="error">{formik.errors.password}</div>
                )}
              </div>

              {/* Confirm Password */}
              <div className="input-group">
                <label htmlFor="confirmPassword">Confirm Password</label>
                <input
                  type="password"
                  id="confirmPassword"
                  name="confirmPassword"
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  value={formik.values.confirmPassword}
                />
                {formik.touched.confirmPassword &&
                  formik.errors.confirmPassword && (
                    <div className="error">{formik.errors.confirmPassword}</div>
                  )}
              </div>

              <button type="submit" className="login-btn">
                Register
              </button>
              <Link to="/login" className="register-button">
                <p className="btn-reg">Already have an account? Login</p>
              </Link>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default RegisterForm;
