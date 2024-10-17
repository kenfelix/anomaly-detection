# Efficient Data Stream Anomaly Detection

This project implements an efficient Python-based system for detecting anomalies in a continuous data stream. The data stream simulates real-time sequences of floating-point numbers, which could represent various metrics like financial transactions or system performance metrics. The system employs a sliding window and Z-Score based anomaly detection algorithm to detect unusual patterns in real-time.

## Features

1. **Data Stream Simulation**: 
   - The data stream generator simulates real-time data with seasonal patterns, random noise, and occasional anomalies (spikes).
   
2. **Anomaly Detection**: 
   - A Z-Score based algorithm is used to flag anomalies in the data stream. It adapts dynamically to the changing nature of the stream.

3. **Real-Time Visualization**: 
   - A real-time plot visualizes the data stream and highlights detected anomalies.

4. **Efficiency**: 
   - The algorithm processes data in real-time using a sliding window, ensuring optimized memory usage and fast anomaly detection.

5. **Python 3.x Compatibility**: 
   - Type annotations, error handling, and documentation make the code clear, robust, and easy to maintain.

## Algorithm Explanation

### Sliding Window and Z-Score
The algorithm uses a sliding window (a deque structure) to keep track of recent data points. For each new data point, the algorithm computes the Z-Score, which measures how far the current value deviates from the mean of the recent data. If the Z-Score exceeds a pre-defined threshold (3.0 by default), the point is flagged as an anomaly.

#### Why Z-Score?
- **Simplicity**: Z-Score is a simple and well-understood statistical method for measuring how many standard deviations a value is from the mean.
- **Effectiveness**: It effectively handles both large spikes and gradual drifts in data, making it suitable for anomaly detection in continuous streams.

### Seasonal Component and Random Noise
The data stream simulates real-world scenarios by including:
- **Seasonal Component**: A sine wave pattern simulates regular fluctuations in the data.
- **Random Noise**: Gaussian noise is added to represent natural variations.
- **Anomalies**: Occasional extreme values (spikes) are introduced to test the anomaly detection mechanism.

## Requirements

- Python 3.10 or later.
- Standard Python libraries like `collections`, `random`, and `deque` are used for memory efficiency and simplicity.
- External libraries: `numpy`, `matplotlib` for numerical calculations and real-time plotting.

## Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/kenfelix/anomaly-detection.git
    cd anomaly-detection
    ```

2. **Create a virtual environment** (optional but recommended):

    ```bash
    python3 -m venv env
    source env/bin/activate  # On Windows: env\Scripts\activate
    ```

3. **Install dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

## Running the Program

To run the program, simply execute the `main` Python script:

```bash
python main.py
