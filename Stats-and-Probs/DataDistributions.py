import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from scipy.stats import binom
from scipy.stats import poisson


# Uniform Distribution
valuesUniform = np.random.uniform(0, 1, 10000)
plt.hist(valuesUniform, bins=50)
plt.title('Uniform Distribution')
plt.show()


# Normal Distribution
valuesNormal = np.arange(-3, 3, 0.1)
normalDist = norm.pdf(valuesNormal, 0, 1)
plt.plot(valuesNormal, normalDist)
plt.title('Normal Distribution')
plt.show()


# Compute MU (desired mean) and Sigma (Standard Deviation)
MU = 5
sigma = 2
values = np.random.normal(MU, sigma, 10000)
plt.hist(values, bins=50)
plt.title('Normal Distribution with MU (Desired Mean of 5) and Sigma (Standard Deviation of 2)')
plt.show()

#Exponential Distribution "Power Law"
valuesExponential = np.arange(0, 10, 0.01)
exponential =  norm.pdf(valuesExponential)
plt.plot(valuesExponential, exponential)
plt.title('Exponential Distribution')
plt.show()

# Binomial Distribution
n , p = 10, 0.5
valuesBinomial = np.arange(0, 10, 0.01)
binomial =  binom.pmf(valuesBinomial, n, p)
plt.plot(valuesBinomial, binomial)
plt.title('Binomial Distribution')
plt.show()

# Poisson Distribution
MU2 = 500
valuesPoisson = np.arange(400, 600, 0.5)
poisson = poisson.pmf(valuesPoisson, MU2)
plt.plot(valuesPoisson, poisson)
plt.title('Poisson Distribution')
plt.show()








