import React, { useState } from 'react';
import { TextField, Button, Container, Typography, Alert } from '@mui/material';

function App() {
  const [numberString, setNumberString] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError(null);  // Clear previous errors
    setResult(null);  // Clear previous result

    try {
      const response = await fetch('http://localhost:8000/calculate_sum', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ number_string: numberString }), // Send input string as JSON
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.detail);
      }

      const data = await response.json();
      setResult(data.sum);
    } catch (err) {
      setError(err.message || "An unexpected error occurred");
    }
  };

  return (
    <Container maxWidth="sm" sx={{ marginTop: 4 }}>
      <Typography variant="h4" align="center">String Calculator</Typography>
      <form onSubmit={handleSubmit} 
        style={{ display: 'flex', flexDirection: 'column', gap: '16px', marginTop: '16px' }}>
        <TextField
          label="Enter numbers"
          variant="outlined"
          value={numberString}
          onChange={(e) => setNumberString(e.target.value)}
          fullWidth
        />
        <Button variant="contained" color="primary" type="submit">Calculate Sum</Button>
      </form>

      {result !== null && (
        <Typography variant="h5" align="center" sx={{ marginTop: 2 }}>
          Sum: {result}
        </Typography>
      )}
      {error && (
        <Alert severity="error" sx={{ marginTop: 2 }}>
          {error}
        </Alert>
      )}
    </Container>
  );
}

export default App;
