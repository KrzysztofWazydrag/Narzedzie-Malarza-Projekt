import matplotlib.pyplot as plt

fig, ax = plt.subplots()

cities = ['Gdańsk', 'Gdynia', 'Sopot']
population = [100, 200, 300]

ax.bar(cities, population)
plt.show()