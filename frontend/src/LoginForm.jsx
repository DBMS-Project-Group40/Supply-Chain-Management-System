import React from "react";
import { useFormik } from "formik";
import * as Yup from "yup";
import "./LoginForm.css";
import inventoryImage from "./inventory2.png";

const LoginSchema = Yup.object().shape({
  email: Yup.string()
    .email("Invalid email address format")
    .required("Please enter your email address"),
  password: Yup.string().required("Please enter your password"),
});

function LoginForm() {
  const formik = useFormik({
    initialValues: {
      email: "",
      password: "",
    },
    validationSchema: LoginSchema,
    validateOnMount: true,
    onSubmit: (values) => {
      console.log(values);
    },
  });

  return (
    <div className="login-page">
      <div>
        <h1 className="wellcome">WELLCOME BACK!</h1>
        <div className="container">
          <div className="img-container">
            <img src={inventoryImage} alt="Inventory Management" />
          </div>
          <form onSubmit={formik.handleSubmit} className="login-form">
            <div className="inside">
              <h1 className="login-text">Login to your Account</h1>

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
              <button type="submit" className="login-btn">
                Login
              </button>
              <button type="button" className="register-button">
                <p className="btn-reg">Don't have an account? Register</p>
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default LoginForm;
