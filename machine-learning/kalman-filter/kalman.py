import numpy as np

class KalmanFilter:
    def __init__(self, A, B, H, Q, R, P, x0):
        self.A = A  # State transition matrix
        self.B = B  # Control input matrix
        self.H = H  # Measurement matrix
        self.Q = Q  # Process noise covariance
        self.R = R  # Measurement noise covariance
        self.P = P  # Estimate error covariance
        self.x = x0  # Initial state estimate

    def predict(self, u=0):
        # Predict the state
        self.x = np.dot(self.A, self.x) + np.dot(self.B, u)
        # Predict the error covariance
        self.P = np.dot(np.dot(self.A, self.P), self.A.T) + self.Q

    def update(self, z):
        # Compute the Kalman Gain
        S = np.dot(self.H, np.dot(self.P, self.H.T)) + self.R
        K = np.dot(np.dot(self.P, self.H.T), np.linalg.inv(S))
        
        # Update the state estimate
        y = z - np.dot(self.H, self.x)
        self.x = self.x + np.dot(K, y)
        
        # Update the error covariance
        I = np.eye(self.H.shape[1])
        self.P = np.dot((I - np.dot(K, self.H)), self.P)

    def current_state(self):
        return self.x

# Example usage
if __name__ == "__main__":
    # Define matrices for a simple 1D motion model
    A = np.array([[1]])
    B = np.array([[0]])
    H = np.array([[1]])
    Q = np.array([[1e-5]])
    R = np.array([[1e-2]])
    P = np.array([[1]])
    x0 = np.array([[0]])

    # Create a Kalman Filter instance
    kf = KalmanFilter(A, B, H, Q, R, P, x0)

    # Simulate some measurements
    measurements = [1, 2, 3, 4, 5]

    for z in measurements:
        kf.predict()
        kf.update(np.array([[z]]))
        print(f"Updated state estimate: {kf.current_state().flatten()}")
