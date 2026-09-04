import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3, 5, 9, 1])

plt.plot(ypoints, '*:c', ms=15, mec = 'm', mfc = 'm')
plt.show()