import numpy as np
import matplotlib.pyplot as plt
X = np.linspace(-np.pi, np.pi, 256)
C, S = np.cos(X), np.sin(X) 
plt.plot(X, C, ls="--", label="cosine") 
plt.plot(X, S, ls=":", label="sine") 
plt.legend(loc=2)
plt.show()