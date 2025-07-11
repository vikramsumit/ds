import matplotlib.pyplot as plt
# plt.plot([1,2,3],[4,5,6])
# plt.show()

# years = [1990, 1992, 1994, 1996, 1998, 2000, 2003, 2005, 2007, 2010]
# runs =  [500, 700, 1100, 1500, 1800, 1200, 1700, 1300, 900, 1500]
# plt.plot(years, runs)
# plt.xlabel("Year")
# plt.ylabel("Runs Scored")
# plt.title("Sachin Tendulkar's Yearly Runs")

# kohli = [0, 0, 500, 800, 1100, 1300, 1500, 1800, 1900, 2100]
# sehwag = [0, 300, 800, 1200, 1500, 1700, 1600, 1400, 1000, 0]


# with plt.xkcd():
#     plt.plot(years, kohli, color='orange', linestyle='--',linewidth = "4", label="Kohli")
#     plt.plot(years, sehwag, color='green', linestyle='-.', label="Sehwag")
#     plt.plot(years, runs, color='blue', label="Tendulkar", linestyle="-")
#     plt.tight_layout()
#     plt.legend()
#     plt.show()

import numpy as np

# for i in range(50):
plt.plot(np.random.rand(100), linewidth=1)

plt.title("Too Much Data Can Be Confusing!")
plt.grid(True)
plt.tight_layout()
plt.show()