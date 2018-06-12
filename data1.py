import pandas as pd
p = pd.read_csv('count_dongda.csv')
import matplotlib.pyplot as plt
plt.plot(p['count'])
plt.show()