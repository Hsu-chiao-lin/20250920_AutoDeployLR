import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.title("Simple Linear Regression Demo with Top 5 Outliers")
st.write("Adjust the parameters below to see the effect on the regression line and outliers.")

# Sidebar inputsimport streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.title("Simple Linear Regression Demo with Top 5 Outliers")
st.write("Adjust the parameters below to see the effect on the regression line and outliers.")

# Sidebar inputs
st.sidebar.header("Parameters")
a = st.sidebar.slider("Slope (a)", min_value=-10.0, max_value=10.0, value=2.0)
b = st.sidebar.slider("Intercept (b)", min_value=-10.0, max_value=10.0, value=1.0)
noise_std = st.sidebar.slider("Noise standard deviation", min_value=0.0, max_value=5.0, value=1.0)
n_points = st.sidebar.slider("Number of points", min_value=10, max_value=100, value=50)

# Generate data
np.random.seed(42)
x = np.linspace(0, 10, n_points)
y = a * x + b + np.random.normal(0, noise_std, size=n_points)

# Fit linear regression
model = LinearRegression()
model.fit(x.reshape(-1, 1), y)
y_pred = model.predict(x.reshape(-1, 1))

# Calculate residuals
residuals = np.abs(y - y_pred)
outlier_indices = np.argsort(residuals)[-5:]  # Top 5 largest residuals

# Plot
fig, ax = plt.subplots()
ax.scatter(x, y, label="Data points")
ax.plot(x, y_pred, color="red", label="Regression line")

# Highlight top 5 outliers
ax.scatter(x[outlier_indices], y[outlier_indices], color="orange", edgecolors="black", s=100, label="Top 5 Outliers")
ax.set_title("Linear Regression Plot with Top 5 Outliers")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend()
st.pyplot(fig)

# Display regression coefficients
st.write(f"Estimated slope: {model.coef_[0]:.2f}")
st.write(f"Estimated intercept: {model.intercept_:.2f}")

# Display Top 5 Outliers
st.write("Top 5 Outliers (X, Y, Residual):")
top_outliers = [(x[i], y[i], residuals[i]) for i in outlier_indices[::-1]]  # largest first
st.write(top_outliers)

st.sidebar.header("Parameters")
a = st.sidebar.slider("Slope (a)", min_value=-10.0, max_value=10.0, value=2.0)
b = st.sidebar.slider("Intercept (b)", min_value=-10.0, max_value=10.0, value=1.0)
noise_std = st.sidebar.slider("Noise standard deviation", min_value=0.0, max_value=5.0, value=1.0)
n_points = st.sidebar.slider("Number of points", min_value=10, max_value=100, value=50)

# Generate data
np.random.seed(42)
x = np.linspace(0, 10, n_points)
y = a * x + b + np.random.normal(0, noise_std, size=n_points)

# Fit linear regression
model = LinearRegression()
model.fit(x.reshape(-1, 1), y)
y_pred = model.predict(x.reshape(-1, 1))

# Calculate residuals
residuals = np.abs(y - y_pred)
outlier_indices = np.argsort(residuals)[-5:]  # Top 5 largest residuals

# Plot
fig, ax = plt.subplots()
ax.scatter(x, y, label="Data points")
ax.plot(x, y_pred, color="red", label="Regression line")

# Highlight top 5 outliers
ax.scatter(x[outlier_indices], y[outlier_indices], color="orange", edgecolors="black", s=100, label="Top 5 Outliers")
ax.set_title("Linear Regression Plot with Top 5 Outliers")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend()
st.pyplot(fig)

# Display regression coefficients
st.write(f"Estimated slope: {model.coef_[0]:.2f}")
st.write(f"Estimated intercept: {model.intercept_:.2f}")

# Display Top 5 Outliers
st.write("Top 5 Outliers (X, Y, Residual):")
top_outliers = [(x[i], y[i], residuals[i]) for i in outlier_indices[::-1]]  # largest first
st.write(top_outliers)
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

st.title("Simple Linear Regression Demo with Top 5 Outliers")
st.write("Adjust the parameters below to see the effect on the regression line and outliers.")

# Sidebar inputs
st.sidebar.header("Parameters")
a = st.sidebar.slider("Slope (a)", min_value=-10.0, max_value=10.0, value=2.0)
b = st.sidebar.slider("Intercept (b)", min_value=-10.0, max_value=10.0, value=1.0)
noise_std = st.sidebar.slider("Noise standard deviation", min_value=0.0, max_value=5.0, value=1.0)
n_points = st.sidebar.slider("Number of points", min_value=10, max_value=100, value=50)

# Generate data
np.random.seed(42)
x = np.linspace(0, 10, n_points)
y = a * x + b + np.random.normal(0, noise_std, size=n_points)

# Fit linear regression
model = LinearRegression()
model.fit(x.reshape(-1, 1), y)
y_pred = model.predict(x.reshape(-1, 1))

# Calculate residuals
residuals = np.abs(y - y_pred)
outlier_indices = np.argsort(residuals)[-5:]  # Top 5 largest residuals

# Plot
fig, ax = plt.subplots()
ax.scatter(x, y, label="Data points")
ax.plot(x, y_pred, color="red", label="Regression line")

# Highlight top 5 outliers
ax.scatter(x[outlier_indices], y[outlier_indices], color="orange", edgecolors="black", s=100, label="Top 5 Outliers")
ax.set_title("Linear Regression Plot with Top 5 Outliers")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.legend()
st.pyplot(fig)

# Display regression coefficients
st.write(f"Estimated slope: {model.coef_[0]:.2f}")
st.write(f"Estimated intercept: {model.intercept_:.2f}")

# Display Top 5 Outliers
st.write("Top 5 Outliers (X, Y, Residual):")
top_outliers = [(x[i], y[i], residuals[i]) for i in outlier_indices[::-1]]  # largest first
st.write(top_outliers)
