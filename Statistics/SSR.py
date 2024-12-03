# -*- coding: utf-8 -*-
"""untitled18.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/gist/pritkudale/9a66029d28e231db597ef894d0c1f320/untitled18.ipynb
"""

# Understand Gradient Decent

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Define the points
p1 = (2, 6)
p2 = (4, 8)
p3 = (6, 7)

# Extract x and y coordinates
x_coords = [p1[0], p2[0], p3[0]]
y_coords = [p1[1], p2[1], p3[1]]

# Streamlit app
st.title("Interactive Plot of Points, Fitted Line, and Residuals")

# Interactive sliders for w0, w1, and w2
w0 = st.slider("w0", -5.0, 5.0, 0.0, step=0.1)
w1 = st.slider("w1", -5.0, 5.0, -1.0, step=0.1)
w2 = st.slider("w2", 0.1, 5.0, 1.0, step=0.1)


def plot_data_line_residuals_and_ssr(w0, w1, w2):
    # Generate x values for the line
    x_line = np.linspace(0, 10, 100)
    y_line = (-w0 - w1 * x_line) / w2

    # Calculate residuals
    residuals = []
    for i in range(len(x_coords)):
        y_predicted = (-w0 - w1 * x_coords[i]) / w2
        residuals.append(y_coords[i] - y_predicted)

    # Calculate sum of squared residuals
    sum_squared_residuals = sum(r**2 for r in residuals)

    # Create subplots in a single row
    fig, axes = plt.subplots(1, 4, figsize=(20, 5))  # Adjust figure size as needed

    # Plot 1: Data, line, and residuals
    axes[0].scatter(x_coords, y_coords, marker='o', label='Data Points')
    axes[0].plot(x_line, y_line, color='red', label='Fitted Line')
    for i in range(len(x_coords)):
        axes[0].plot([x_coords[i], x_coords[i]], [y_coords[i], y_line[np.argmin(np.abs(x_line - x_coords[i]))]], color='blue', linestyle='--', linewidth=1, label='Residuals' if i == 0 else "")
    axes[0].set_xlabel('X-axis')
    axes[0].set_ylabel('Y-axis')
    axes[0].set_title(f'Data, Line, Residuals (SSR = {sum_squared_residuals:.2f})')
    axes[0].set_xlim(0, 8)
    axes[0].set_ylim(0, 10)
    axes[0].legend()

    # Plot 2: SSR vs w0
    w0_values = np.linspace(-5, 5, 100)
    ssr_values = [sum((y_coords[i] - (-w0_val - w1 * x_coords[i]) / w2)**2 for i in range(len(x_coords))) for w0_val in w0_values]
    axes[1].plot(w0_values, ssr_values)
    axes[1].scatter(w0, sum_squared_residuals, color='red', marker='o', s=50, label=f'Current w0 ({w0:.2f})')
    axes[1].set_xlabel("w0")
    axes[1].set_ylabel("SSR")
    axes[1].set_title("SSR vs w0")
    axes[1].grid(True)
    axes[1].legend()

    # Plot 3: SSR vs w1
    w1_values = np.linspace(-5, 5, 100)
    ssr1_values = [sum((y_coords[i] - (-w0 - w1_val * x_coords[i]) / w2)**2 for i in range(len(x_coords))) for w1_val in w1_values]
    axes[2].plot(w1_values, ssr1_values)
    axes[2].scatter(w1, sum_squared_residuals, color='red', marker='o', s=50, label=f'Current w1 ({w1:.2f})')
    axes[2].set_xlabel("w1")
    axes[2].set_ylabel("SSR")
    axes[2].set_title("SSR vs w1")
    axes[2].grid(True)
    axes[2].legend()

    # Plot 4: SSR vs w2
    w2_values = np.linspace(0.1, 5, 100)
    ssr2_values = [sum((y_coords[i] - (-w0 - w1 * x_coords[i]) / w2_val)**2 for i in range(len(x_coords))) for w2_val in w2_values]
    axes[3].plot(w2_values, ssr2_values)
    axes[3].scatter(w2, sum_squared_residuals, color='red', marker='o', s=50, label=f'Current w2 ({w2:.2f})')
    axes[3].set_xlabel("w2")
    axes[3].set_ylabel("SSR")
    axes[3].set_title("SSR vs w2")
    axes[3].grid(True)
    axes[3].legend()

    plt.tight_layout()
    st.pyplot(plt) # Use st.pyplot to display the plot in Streamlit



plot_data_line_residuals_and_ssr(w0, w1, w2)
