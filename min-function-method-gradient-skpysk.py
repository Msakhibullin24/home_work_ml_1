import numpy as np

# Определение функции
def f(x1, x2):
    return 3 * x1**2 + 2 * x2**2 + 4 * x1 * x2 - 5 * x1 + 6 * x2   #сначала мы ищем тут этот функцию по x1 и x2

# Определение градиента функции
def gradient(x1, x2):
    df_dx1 = 6 * x1 + 4 * x2 - 5 #это вобщем то что у нас уже мы вычисилили после диффиринцирвоания
    df_dx2 = 4 * x1 + 4 * x2 + 6 #это вобщем то что у нас уже мы вычисилили после диффиринцирвоания
    return np.array([df_dx1, df_dx2])

# Градиентный спуск
def gradient_descent(starting_point, learning_rate, num_iterations):
    x = np.array(starting_point)
    for _ in range(num_iterations):
        grad = gradient(x[0], x[1])
        x = x - learning_rate * grad
    return x

# Параметры алгоритма
starting_point = [0, 0]  # Начальная точка
learning_rate = 0.01     # Шаг обучения
num_iterations = 1000    # Количество итераций

# ищем минимум
minimum = gradient_descent(starting_point, learning_rate, num_iterations)
print("Точка минимума:", minimum)
print("Минимальное значение функции:", f(minimum[0], minimum[1]))
