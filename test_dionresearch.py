from dionresearch.stats import hotelling_t2, control_interval
import pandas as pd
import matplotlib.pyplot as plt


x = pd.DataFrame(
    {
        "id": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14],
        "impurities": [
            14.92,
            16.90,
            17.38,
            16.90,
            16.92,
            16.71,
            17.07,
            16.93,
            16.71,
            16.88,
            16.73,
            17.07,
            17.60,
            16.90,
        ],
        "temp": [
            85.77,
            83.77,
            84.46,
            86.27,
            85.23,
            83.81,
            86.08,
            85.85,
            85.73,
            86.27,
            83.46,
            85.81,
            85.92,
            84.23,
        ],
        "concentration": [
            42.26,
            43.44,
            42.74,
            43.60,
            43.18,
            43.72,
            43.33,
            43.41,
            43.28,
            42.59,
            44.00,
            42.78,
            43.11,
            43.48,
        ],
    }
)
x.set_index("id", inplace=True)
print (x)
n, f = x.shape
m = n

# computing each individual values to the mean and covariance of the whole dataset
x_bar, s = x.mean(0), x.cov()
qi = [hotelling_t2(x[i: i + 1], x_bar, S=s) for i in range(n)]
df = pd.DataFrame({"qi": qi})
lcl, cl, ucl = control_interval(m, n, f, phase=1, alpha=0.001)

plt.figure()
plt.plot([i for i in range(len(qi))], qi, c='blue', alpha=0.5)
plt.show()
