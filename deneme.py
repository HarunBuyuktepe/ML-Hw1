import numpy as np
import matplotlib.pyplot as plt



def plotDistribution(mean , cov):
    x1, x2 = np.random.multivariate_normal(mean, cov, 100).T
    area = np.pi * 3
    colors = (0, 0, 0)

    plt.scatter(x1, x2, s=area, c=colors, alpha=0.5)
    plt.title('plot')
    plt.xlabel('x-1')
    plt.ylabel('x-2')
    plt.show()




print("HW 1 Question 8")
mean1 = [0, 0]
mean2 = [1, -1]
cov1 = [[],[]]
cov2 = [[2, 0], [0, 2]]
cov3 = [[2, 0.2], [0.2, 2]]
cov4 = [[2, -0.2], [-0.2, 2]]


plotDistribution(mean1,cov1)
plotDistribution(mean2,cov1)
plotDistribution(mean1,cov2)
plotDistribution(mean1,cov3)
plotDistribution(mean1,cov4)




