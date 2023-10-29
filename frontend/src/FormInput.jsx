import React, { useState } from "react";
import "./FormInput.css";

const FormInput = (props) => {
  const [focused, setFocused] = useState(false);
  const { label, errorMessage, onChange, ...inputProps } = props;

  return (
    <div className="formInput">
      <label>{label}</label>
      <input
        {...inputProps}
        onChange={onChange}
        onBlur={() => setFocused(false)}
        onFocus={() => setFocused(true)}
        focused={focused.toString()}
      />
      <span
        className={
          focused &&
          inputProps.value &&
          inputProps.type !== "date" &&
          !inputProps.validity.valid
            ? "visible"
            : ""
        }
      >
        {errorMessage}
      </span>
    </div>
  );
};

export default FormInput;
