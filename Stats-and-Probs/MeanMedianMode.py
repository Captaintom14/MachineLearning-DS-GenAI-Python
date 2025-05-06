import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Mean, Median, Mode
# Mean
incomes = np.random.normal(1000, 200, 10000)
print (np.mean(incomes))
#show the distribution
plt.hist(incomes, bins=50)
plt.title('Income Distribution')
plt.show()

# Add a median
incomes2 = np.append(incomes, [1000000000])
print (np.median(incomes2))
#show the distribution
plt.hist(incomes2, bins=50)
plt.title('Income Distribution with Outlier')
plt.show()

# Add a mode
ages = np.random.randint(18, high= 180, size=500)
print ("ages", np.mean(ages))
stats.mode(ages)
print ("mode", stats.mode(ages))


