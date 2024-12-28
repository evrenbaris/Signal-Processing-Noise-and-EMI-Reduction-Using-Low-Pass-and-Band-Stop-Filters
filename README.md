# Signal Processing: Noise and EMI Reduction Using Low-Pass and Band-Stop Filters

## Description
This project demonstrates how to process and clean noisy signals by reducing random noise and electromagnetic interference (EMI) using digital filters. The project employs Fourier Transform for frequency domain analysis and applies low-pass and band-stop filters to clean the signal.

## Features
- Generates a clean 50 Hz sine wave signal.
- Adds random noise and EMI (150 Hz) to simulate real-world conditions.
- Performs Fourier Transform for frequency spectrum analysis.
- Applies:
  - **Low-Pass Filter**: Reduces high-frequency noise.
  - **Band-Stop Filter**: Suppresses EMI at 150 Hz.
- Visualizes the original, noisy, and filtered signals in both time and frequency domains.

## Technologies Used
- **Python**
  - NumPy: Numerical computations.
  - Matplotlib: Visualization of signals and spectrums.
  - SciPy: Digital filter design and implementation.

## How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/signal-processing-emi-reduction.git
