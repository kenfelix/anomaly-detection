import random
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
from matplotlib.animation import FuncAnimation
from typing import Generator, Tuple


def data_stream() -> Generator[float, None, None]:
    """
    Generator function that simulates a continuous data stream with:
    - Seasonal patterns (sine wave)
    - Random noise (Gaussian)
    - Occasional anomalies (extreme values)

    Yields:
        float: A floating-point number representing the next data point in the stream.
    """
    t: int = 0
    while True:
        # Simulate a base sine wave pattern with added noise
        seasonal_component: float = 10 * np.sin(0.1 * t)  # Regular pattern
        noise: float = random.gauss(0, 2)  # Random Gaussian noise
        anomaly: float = random.choice(
            [0, 0, 0, 20]
        )  # Occasional anomalies (20 is a spike)
        yield seasonal_component + noise + anomaly
        t += 1


def detect_anomaly(window: deque[float], threshold: float = 3.0) -> Tuple[bool, float]:
    """
    Detects anomalies in a sliding window using Z-Score.

    Args:
        window (deque[float]): Sliding window of recent data points.
        threshold (float): Z-score threshold for detecting anomalies.

    Returns:
        Tuple[bool, float]: A tuple containing:
                            - Whether the latest value is an anomaly.
                            - The Z-score of the latest value.
    """
    if len(window) < 2:
        return False, 0.0  # Not enough data to detect anomalies

    mean: float = float(np.mean(window))
    std: float = float(np.std(window))

    if std == 0:
        return False, 0.0  # Avoid division by zero if no variation

    latest_value: float = window[-1]
    z_score: float = (latest_value - mean) / std

    # Return whether the Z-score exceeds the threshold
    return abs(z_score) > threshold, z_score


def update(
    frame: int,
    window: deque[float],
    anomalies: deque[float],
    data_gen: Generator[float, None, None],
    ax: plt.Axes,
    line: plt.Line2D,
    anomaly_line: plt.Line2D,
) -> Tuple[plt.Line2D, plt.Line2D]:
    """
    Update function for real-time plotting and anomaly detection.

    Args:
        frame (int): The frame number (for FuncAnimation).
        window (deque[float]): The sliding window storing the last N data points.
        anomalies (deque[float]): Queue for storing detected anomalies.
        data_gen (Generator[float, None, None]): The data stream generator function.
        ax (Axes): Matplotlib axes for plotting.
        line (Line2D): The line plot for the data stream.
        anomaly_line (Line2D): The line plot for marking anomalies.

    Returns:
        Tuple[Line2D, Line2D]: Updated line and anomaly_line to be redrawn in the animation.
    """
    # Get the next data point from the stream
    data: float = next(data_gen)

    # Add data to the sliding window
    window.append(data)

    # Check for anomalies
    is_anomaly, z_score = detect_anomaly(window)
    anomalies.append(data if is_anomaly else np.nan)  # Mark anomaly

    # Update the data in the plot
    line.set_ydata(window)
    anomaly_line.set_ydata(anomalies)

    ax.relim()
    ax.autoscale_view()

    return line, anomaly_line


def main() -> None:
    """
    Main function to set up and execute the real-time anomaly detection system.
    """
    # Parameters
    window_size: int = 100  # Size of the sliding window
    threshold: float = 3.0  # Z-score threshold for anomaly detection

    # Initialize deque (sliding window) and anomalies queue
    window: deque[float] = deque([0.0] * window_size, maxlen=window_size)
    anomalies: deque[float] = deque([np.nan] * window_size, maxlen=window_size)

    # Data stream generator
    data_gen: Generator[float, None, None] = data_stream()

    # Set up real-time plot
    fig, ax = plt.subplots()
    (line,) = ax.plot(list(window), label="Data Stream")
    (anomaly_line,) = ax.plot(list(anomalies), "ro", label="Anomalies")

    ax.set_ylim(-30, 30)  # Set y-limits for visualization

    # Real-time animation
    ani = FuncAnimation(
        fig,
        update,
        fargs=(window, anomalies, data_gen, ax, line, anomaly_line),
        interval=100,  # Update interval (ms)
    )

    plt.legend()
    plt.show()


if __name__ == "__main__":
    main()
