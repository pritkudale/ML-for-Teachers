# prompt: publish it on stramlit

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import norm

st.title("Normal Distribution Plotter")

mu = st.slider("Mean (mu)", -5.0, 5.0, 0.0, 0.1)
sigma = st.slider("Standard Deviation (sigma)", 0.1, 5.0, 1.0, 0.1)
z_value1 = st.slider("z-value 1", -5.0, 5.0, -1.0, 0.1)
z_value2 = st.slider("z-value 2", -5.0, 5.0, 1.0, 0.1)
show_cdf = st.checkbox("Show CDF")


x = np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)
y = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

fig, ax = plt.subplots()
ax.plot(x, y, label='PDF')

if show_cdf:
    cdf = norm.cdf(x, loc=mu, scale=sigma)
    ax.plot(x, cdf, label='CDF')

x_fill = np.linspace(z_value1, z_value2, 100)
y_fill = (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x_fill - mu) / sigma) ** 2)
ax.fill_between(x_fill, y_fill, color='skyblue', alpha=0.5)

cdf_value1 = norm.cdf(z_value1, loc=mu, scale=sigma)
cdf_value2 = norm.cdf(z_value2, loc=mu, scale=sigma)
area = cdf_value2 - cdf_value1

ax.plot(z_value1, 0, marker='o', markersize=8, color='red', label=f'z1 = {z_value1:.2f}')
ax.plot(z_value2, 0, marker='o', markersize=8, color='green', label=f'z2 = {z_value2:.2f}')

ax.text(z_value1, 0.05, f'CDF({z_value1:.2f}) = {cdf_value1:.2f}', ha='center', va='bottom')
ax.text(z_value2, 0.05, f'CDF({z_value2:.2f}) = {cdf_value2:.2f}', ha='center', va='bottom')
ax.text((z_value1 + z_value2) / 2, 0.1, f'Area = {area:.2f}', ha='center', va='bottom')

ax.set_title('Normal Distribution')
ax.set_xlabel('x')
ax.set_ylabel('Probability Density/Cumulative Probability')
ax.grid(True)
ax.legend()

st.pyplot(fig)
