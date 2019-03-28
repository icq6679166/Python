import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sequence = pd.DataFrame(np.random.normal(1.0, 0.08, (100, 8)))
print sequence.shape
accumulates = sequence.cumprod()
print accumulates.shape
accumulates.plot()
plt.title('behaviors')
plt.xlabel('Time')
plt.ylabel('Value')
plt.show()
