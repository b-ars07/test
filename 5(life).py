
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
 
N = 100
ON = 255
OFF = 0
values = [ON, OFF]
 
# заполняем сетку случайными значениями, преимущественно OFF
grid = np.random.choice(values, N * N, p=[0.2, 0.8]).reshape(N, N)
 
 
def update(data):
    global grid
    # копируем сетку, т.к. нам надо 8 ближайших соседей на каждой итерации
    # и мы обходим сетку линия за линией
    new_grid = grid.copy()
    for i in range(N):
        for j in range(N):
            # вычисляем сумму 8 соседей
            # используя тороидальные граниччные соглашения - x и y обернуты вокруг
            # т.е. моделируется тороидальная поверхность.
            total = (grid[i, (j - 1) % N] + grid[i, (j + 1) % N] +
                     grid[(i - 1) % N, j] + grid[(i + 1) % N, j] +
                     grid[(i - 1) % N, (j - 1) % N] + grid[(i - 1) % N, (j + 1) % N] +
                     grid[(i + 1) % N, (j - 1) % N] + grid[(i + 1) % N, (j + 1) % N]) / 255
            # применяем правила Конвея
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = OFF
            else:
                if total == 3:
                    new_grid[i, j] = ON
    # обновление данных
    mat.set_data(new_grid)
    grid = new_grid
    return [mat]
 
 
# настраиваем анимацию
fig, ax = plt.subplots()
mat = ax.matshow(grid)
ani = animation.FuncAnimation(fig, update, interval=50, save_count=50)
plt.show()
print "Hello World"