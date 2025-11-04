import random
import seaborn as sb
import matplotlib.pyplot as plt

data1: list[int] = [i % 10 for i in range(100)]
data2: list[float] = [(i + random.random() * 0.5) * max(random.random(), 0.5) for i in data1]

sb.set_theme()

sb.boxplot(x=data1, y=data2)

plt.show()