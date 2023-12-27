import React, { useState } from 'react';

const HookFormWithValidation = () => {
  const [formData, setFormData] = useState({
    firstName: '',
    lastName: '',
    email: '',
    password: '',
    confirmPassword: '',
  });

  const [errors, setErrors] = useState({
    firstName: '',
    lastName: '',
    email: '',
    password: '',
    confirmPassword: '',
  });

  const validateInput = (name, value) => {
    switch (name) {
      case 'firstName':
      case 'lastName':
        if (value.length < 2) {
          return `${name} must be at least 2 characters`;
        }
        break;
      case 'email':
        if (value.length < 5) {
          return 'Email must be at least 5 characters';
        }
        break;
      case 'password':
        if (value.length < 8) {
          return 'Password must be at least 8 characters';
        }
        break;
      case 'confirmPassword':
        if (value.length < 8 || value !== formData.password) {
          return 'Passwords must match and be at least 8 characters';
        }
        break;
      default:
        break;
    }
    return '';
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
    setErrors({
      ...errors,
      [name]: formData[name] ? validateInput(name, value) : '',
    });
  };

  return (
    <div>
      <div>
        <label>First Name:</label>
        <input
          type="text"
          name="firstName"
          value={formData.firstName}
          onChange={handleChange}
        />
        {formData.firstName && <div>{errors.firstName}</div>}
      </div>

      <div>
        <label>Last Name:</label>
        <input
          type="text"
          name="lastName"
          value={formData.lastName}
          onChange={handleChange}
        />
        {formData.lastName && <div>{errors.lastName}</div>}
      </div>

      <div>
        <label>Email:</label>
        <input
          type="text"
          name="email"
          value={formData.email}
          onChange={handleChange}
        />
        {formData.email && <div>{errors.email}</div>}
      </div>

      <div>
        <label>Password:</label>
        <input
          type="password"
          name="password"
          value={formData.password}
          onChange={handleChange}
        />
        {formData.password && <div>{errors.password}</div>}
      </div>

      <div>
        <label>Confirm Password:</label>
        <input
          type="password"
          name="confirmPassword"
          value={formData.confirmPassword}
          onChange={handleChange}
        />
        {formData.confirmPassword && <div>{errors.confirmPassword}</div>}
      </div>
    </div>
  );
};

export default HookFormWithValidation;