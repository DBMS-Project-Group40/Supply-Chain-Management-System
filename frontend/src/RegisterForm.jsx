import React from "react";
import { useFormik } from "formik";
import * as Yup from "yup";
import "./RegisterForm.css";
import inventoryImage from "./inventory2.png";
import { Link } from "react-router-dom";
import { addCustomer, addUser, getUser } from "./api/InventoryAPI";

const RegisterSchema = Yup.object().shape({
  username: Yup.string().required("Please enter your username"),
  email: Yup.string()
    .email("Invalid email address format")
    .required("Please enter your email address"),
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
  const formik = useFormik({
    initialValues: {
      username: "",
      email: "",
      password: "",
      confirmPassword: "",
      role: "",
      address: "",
    },
    validationSchema: RegisterSchema,
    validateOnMount: true,
    onSubmit: async (values) => {
      try {
        var newUser = {
          name: values.username,
          email: values.email,
          role: values.role,
          password: values.password,
          address: values.address,
        };
        const response = await addUser(newUser);
        if (values.role === "customer") {
          try {
            const userID = await getUser().then((data) => data.id);
            const response_c = await addCustomer({
              points: 0,
              address: values.address,
              user_id: userID,
            });
          } catch (error) {
            console.error("Error occurred", error);
          }
        }

        console.log("User added successfully:", response);
        formik.resetForm();
      } catch (error) {
        console.error("Error adding the user:", error);
      }
    },
  });

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

              <div className="input-group">
                <label htmlFor="username">Username</label>
                <input
                  type="text"
                  id="username"
                  name="username"
                  onChange={formik.handleChange}
                  onBlur={formik.handleBlur}
                  value={formik.values.username}
                />
                {formik.touched.username && formik.errors.username && (
                  <div className="error">{formik.errors.username}</div>
                )}
              </div>

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
