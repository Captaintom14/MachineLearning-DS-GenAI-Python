import numpy as np
import matplotlib.pyplot as plt

# Standard Deviation
incomes = np.random.normal(1000, 200, 10000)
print (np.std(incomes))
plt.hist(incomes, bins=50)
plt.title('Income Distribution with Standard Deviation')
plt.show()


#Variance
incomesV = np.random.normal(1000, 200, 10000)
print (np.var(incomesV))
plt.hist(incomesV, bins=50)
plt.title('Income Distribution with Variance')
plt.show()


