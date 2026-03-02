# Project 01: Approximating y = x² with PyTorch 

## Objective
Build a neural network to approximate the function y = x² with some added noise.

## Description
- Generate 50 points x evenly spaced between -1 and 1.
- Compute y = x² + random noise.
- Neural network architecture:
  - Input layer: 1 neuron
  - Hidden layer: 8 neurons + ReLU activation
  - Output layer: 1 neuron
- Loss function: Mean Squared Error (MSELoss)
- Optimizer: Adam (or SGD)

## Results
- A plot comparing the real data points and the network predictions: `results.png`
- The network learns to approximate the non-linear function y = x².


