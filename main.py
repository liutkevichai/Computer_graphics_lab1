import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import numpy as np
import tkinter as tk

from axes_config import config_axes
import transformations as tfm


def plot_polygon(func, axes, patches_list):
    """
    Функция для построения полигона на графике.
    :param func: функция для преобразования координат вершин
    :param axes: объект системы координат для построения графика
    :param patches_list: список объектов Polygon, добавленных на график
    :return: внутренняя функция преобразования с сохранённым контекстом
    """
    # Внутренняя функция-замыкание
    def inner_func(*args, **kwargs):
        # Очищение списка фигур и удаление их с графика
        if patches_list:
            for patch in patches_list:
                patch.remove()
            patches_list.clear()
        # Вызов коллбэк функции для получения преобразованного массива координат вершин
        vertices_to_plot = func(*args, **kwargs)
        # Создание полигона на основе преобразованного массива
        pol = Polygon(vertices_to_plot, closed=True, edgecolor='black', fill=True, alpha=0.6)
        # Добавление полигона на график и в список фигур
        patches_list.append(axes.add_patch(pol))
        # Внутренняя функция возвращает объект Polygon
        return pol
    # Внешняя функция возвращает вызываемую внутреннюю функцию с сохранённым контекстом
    return inner_func


# Функции-обработчики для кнопок
def on_rotate():
    # Создание объекта plotter с помощью функции plot_polygon.
    # В качестве аргументов передается функция для преобразования вершин, система координат и список фигур.
    plotter = plot_polygon(tfm.rotate_polygon, ax, patches)
    # Вызов внутренней функции plotter.
    plotter(np.pi / 4, vertices_homogeneous)
    # Обновление холста для отрисовки изменений.
    canvas.draw()


def on_scale_up():
    plotter = plot_polygon(tfm.scale_polygon, ax, patches)
    plotter(1.5, 1.5, vertices_homogeneous)
    canvas.draw()


def on_scale_down():
    plotter = plot_polygon(tfm.scale_polygon, ax, patches)
    plotter(0.5, 0.5, vertices_homogeneous)
    canvas.draw()


def on_reflect():
    plotter = plot_polygon(tfm.reflect_polygon, ax, patches)
    plotter(vertices_homogeneous)
    canvas.draw()


def on_translate():
    plotter = plot_polygon(tfm.translate_polygon, ax, patches)
    plotter(2, 1, vertices_homogeneous)
    canvas.draw()


# Функция-обработчик для повторной отрисовки исходного полигона
def on_original():
    plotter = plot_polygon(lambda: vertices, ax, patches)
    plotter()
    canvas.draw()


def destroy_window():
    root.quit()
    root.destroy()


# Создание и настройка окна программы
root = tk.Tk()
root.title("Двумерные аффинные преобразования")
root.config(bg='white')
root.resizable(width=False, height=False)
# Завершение процесса при закрытии окна приложения
root.protocol("WM_DELETE_WINDOW", destroy_window)

# Создание фрейма для верхних кнопок
button_frame = tk.Frame(root)
button_frame.pack(side=tk.TOP, pady=(25, 0))

# Создание верхних кнопок
tk.Button(button_frame, text="Поворот", width=10, command=on_rotate).pack(side=tk.LEFT)
tk.Button(button_frame, text="Увеличение", width=10, command=on_scale_up).pack(side=tk.LEFT)
tk.Button(button_frame, text="Уменьшение", width=10, command=on_scale_down).pack(side=tk.LEFT)
tk.Button(button_frame, text="Отражение", width=10, command=on_reflect).pack(side=tk.LEFT)
tk.Button(button_frame, text="Перенос", width=10, command=on_translate).pack(side=tk.LEFT)

# Создание рисунка и осей координат
fig, ax = plt.subplots()
# Вызов функции для настройки осей
config_axes(ax)

# Создание списка фигур, добавленных на график
patches = []

# Создание объекта FigureCanvasTkAgg
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().config(width=600, height=500)
canvas.draw()

# Размещение canvas в окне Tkinter
canvas.get_tk_widget().pack()

# Создание и размещение нижней кнопки
(tk.Button(root, text="Оригинал", background='darkblue', fg='white', width=20, command=on_original)
 .pack(side=tk.BOTTOM, pady=(0, 25)))

# Определение координат вершин исходного многоугольника
vertices = np.array([
    (-2, 2.5),
    (2, 1.7),
    (0, 0),
    (2, -1.7),
    (-2, -2.5),
    (-2, 2.5)
])

# Создание массива однородных координат вершин полигона на основе исходного массива вершин.
# np.hstack() здесь выполняет горизонтальную конкатенацию массива вершин с вектором, состоящим из единиц,
# который содержит такое же количество строк, как и vertices
vertices_homogeneous = np.hstack((vertices, np.ones((vertices.shape[0], 1))))

# Добавление многоугольника на график
on_original()

# Запуск основного цикла обработки событий
root.mainloop()
