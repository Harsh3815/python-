import pylab as plt

y = [35, 25, 25, 15]
mylabels = ["Apples", "bananas", "cherries", "Dates"]
myexplode = [0.1, 0.1, 0.1, 0.1]
plt.pie(y, labels=mylabels, startangle=180,explode = myexplode)
plt.show()
