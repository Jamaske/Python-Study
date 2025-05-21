import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def euler_improved(f, n, y0):
    # Интервал решения
    x0, x_end = 0, 1
    h = (x_end - x0) / n
    x_vals = [x0]
    y_vals = [y0]
    
    x = x0
    y = y0
    for i in range(n):
        ep = f(x, y)
        y_predict = y + h * ep
        x_new = x + h
        y += (h / 2) * (ep + f(x_new, y_predict))  # пересчёт
        x = x_new
        x_vals.append(x)
        y_vals.append(y)

    # Точное решение для сравнения
    sol = solve_ivp(lambda x, y: f(x, y), [x0, x_end], [y0], t_eval=np.linspace(x0, x_end, 1000))
    x_exact = sol.t
    y_exact = sol.y[0]

    # Сохраняем данные в Excel
    df = pd.DataFrame({'x': x_vals, 'y': y_vals})
    df.to_excel('table_eulerrecalc.xlsx', index=False)

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, 'o-', label='Эйлер с пересчётом', color='blue')
    plt.plot(x_exact, y_exact, '-', label='Точное решение', color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.title('Метод Эйлера с пересчётом')
    plt.show()

# Определение функции f(x, y)
def f(x, y):
    return (np.pi / y) * np.sin(2 * np.pi * x)

# Вызов функции
euler_improved(f, 10, -2)
