import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def adams_moulton_3(f, n, y0):
    # Интервал
    x0, x_end = 0, 1
    h = (x_end - x0) / n


    # Первый шаг (разгон) делаем методом рунге кутты третьего порядка
    k1 = f(x0, y0)
    k2 = f(x0 + h, y0 + h*k1)
    k3 = f(x0 + h/2, y0 + h*k1/4+h*k2/4)
    x1 = x0 + h
    y1 = y0 + (h/6) * (k1 + k2 + 4*k3)
    x_vals = [x0, x1]
    y_vals = [y0, y1]

    for i in range(1, n):
        x_prev, y_prev = x_vals[i], y_vals[i]
        x_prev1, y_prev1 = x_vals[i-1], y_vals[i-1]
        x_next = x_prev + h
        
        #вычисляем y_new по выведенной формуле
        b=-(y_prev+h*(8*np.pi*h*np.sin(2*np.pi*x_prev)/y_prev - np.pi*h*np.sin(2*np.pi*x_prev1)/y_prev1)/12)
        c=-5*(np.pi*h*np.sin(2*np.pi*x_next))/12
        y_new = (-b-np.sqrt(np.power(b, 2)-4*c))*0.5
        x_vals.append(x_next)
        y_vals.append(y_new)

    # Точное решение для сравнения
    sol = solve_ivp(lambda x, y: f(x, y), [x0, x_end], [y0], t_eval=np.linspace(x0, x_end, 1000))
    x_exact = sol.t
    y_exact = sol.y[0]

    # Сохраняем в Excel
    df = pd.DataFrame({'x': x_vals, 'y': y_vals})
    df.to_excel('table_adams_moulton3.xlsx', index=False)

    # График
    plt.figure(figsize=(10, 6))
    plt.plot(x_vals, y_vals, 'o-', label='Адамс-Мултон 3-й порядок', color='blue')
    plt.plot(x_exact, y_exact, '-', label='Точное решение', color='red')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.title('Неявный метод Адамса (3-й порядок)')
    plt.show()

# Задаём f(x, y)
def f(x, y):
    return (np.pi / y) * np.sin(2 * np.pi * x)

# Вызов (второй аргумент это как раз N из условия лабы)
adams_moulton_3(f, 200, -2)
