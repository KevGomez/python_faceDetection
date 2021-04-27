import matplotlib.pyplot as plt

import numpy as np

img = np.array([0,0,0,0,7,7,7,7,0,7,7,7,7])
ken = np.array([1,-2,1])

res1 = np.correlate(img,ken)

plt.subplot(121),plt.plot(res1)