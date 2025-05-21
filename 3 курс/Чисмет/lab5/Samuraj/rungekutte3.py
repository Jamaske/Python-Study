import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def runge_kutta_3(f, N, y0):
    # Интервал решения
    x0, x_end = 0, 1
    h = (x_end - x0) / N
    x_vals = [x0]
    y_vals = [y0]
    
    # Метод Рунге-Кутты 3-го порядка
    x = x0
    y = y0
    for _ in range(N):
        k1 = f(x, y)
        k2 = f(x + h, y + h*k1)
        k3 = f(x + h/2, y + h*k1/4+h*k2/4)
        y += (h/6) * (k1 + k2 + 4*k3)
        x += h
        x_vals.append(x)
        y_vals.append(y)

    # Вычисляем точное решение для сравнения
    sol = solve_ivp(lambda x, y: f(x, y), [x0, x_end], [y0], t_eval=np.linspace(x0, x_end, 1000))
    x_exact = sol.t
    y_exact = sol.y[0]

    # Сохраняем данные в Excel
    df = pd.DataFrame({'x': x_vals, 'y': y_vals})
    df.to_excel('table_explicit_rungekutta3.xlsx', index=False)

    # Строим график
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, 'o-', label='RK3 (приближённое)', color='blue')
    plt.plot(x_exact, y_exact, '-', label='Точное решение', color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.title('Метод Рунге-Кутты 3-го порядка')
    plt.show()

# Определение функции f(x, y)
def f(x, y):
    return (np.pi / y) * np.sin(2 * np.pi * x)

# Вызов функции (второй аргумент это как раз N из условия лабы) 
runge_kutta_3(f, 50, -2)
