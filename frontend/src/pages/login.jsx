import React, { useState } from 'react';
import { Container, Card, Form, Button, Alert } from 'react-bootstrap';
import axios from 'axios';
// import benchLogo from '../assets/bench_logo.svg';

const LoginForm = () => {
  const [formData, setFormData] = useState({ email: '', password: '' });
  const [errorMsg, setErrorMsg] = useState('');
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleLogin = async (e) => {
    e.preventDefault();
    setErrorMsg('');
    setLoading(true);

    try {
      const response = await axios.post('https://your-api-url.com/login', formData);
      console.log('Login success:', response.data);

      // Example: save token or redirect
      // localStorage.setItem('token', response.data.token);
      // navigate('/dashboard');

    } catch (error) {
      console.error('Login error:', error);
      setErrorMsg(error.response?.data?.message || 'Login failed. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <Container className="d-flex flex-column justify-content-center align-items-center min-vh-100">
      <Card className="shadow-sm p-4" style={{ maxWidth: '400px', width: '100%' }}>
        <div className="text-center mb-4">
          {/* <img src={benchLogo} alt="Logo" style={{ height: 50 }} /> */}
          <h5 className="mt-2 mb-0 fw-bold" style={{ color: '#004a99' }}>
            Bench Resources <span style={{ color: '#28a745' }}>Onboarding</span>
          </h5>
        </div>

        <h6 className="fw-bold mb-3" style={{position: 'left', color: '#004a99' }}>Login</h6>

        {errorMsg && <Alert variant="danger">{errorMsg}</Alert>}

        <Form onSubmit={handleLogin}>
          <Form.Group className="mb-3" controlId="formEmail">
            <Form.Label>Email</Form.Label>
            <Form.Control
              type="email"
              placeholder="Enter your Email"
              name="email"
              value={formData.email}
              onChange={handleChange}
              required
            />
          </Form.Group>

          <Form.Group className="mb-3" controlId="formPassword">
            <Form.Label>Password</Form.Label>
            <Form.Control
              type="password"
              placeholder="Enter Password"
              name="password"
              value={formData.password}
              onChange={handleChange}
              required
            />
          </Form.Group>

          <div className="mb-3 text-end">
            <a href="#" style={{ fontSize: '0.9rem', color: '#333' }}>Forgot Password?</a>
          </div>

          <Button variant="primary" type="submit" className="w-100" disabled={loading}>
            {loading ? 'Logging in...' : 'Login'}
          </Button>
        </Form>
      </Card>

      <p className="mt-3 text-center" style={{ fontSize: '0.9rem' }}>
        Don’t have an account? <a href="#" className="fw-bold text-primary">Sign Up</a>
      </p>
    </Container>
  );
};

export default LoginForm;
