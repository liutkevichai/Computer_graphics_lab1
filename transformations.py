import numpy as np


def rotate_polygon(angle_rad, vertices_hg):
    """
    Преобразование поворота фигуры.
    :param angle_rad: угол поворота в радианах
    :param vertices_hg: однородные координаты вершин
    :return: двумерные координаты вершин
    """
    # Матрица поворота
    rotation_matrix = np.array([
        [np.cos(angle_rad), np.sin(angle_rad), 0],
        [-np.sin(angle_rad), np.cos(angle_rad), 0],
        [0, 0, 1]
    ])
    # Матрица вершин умножается на транспонированную матрицу поворота
    rotated_vertices_homogeneous = np.dot(vertices_hg, rotation_matrix.T)
    # Преобразование обратно в 2D координаты
    return rotated_vertices_homogeneous[:, :2]


def scale_polygon(scale_x, scale_y, vertices_hg):
    """
    Преобразование масштабирования фигуры.
    :param scale_x: коэффициент масштабирования по оси x
    :param scale_y: коэффициент масштабирования по оси y
    :param vertices_hg: однородные координаты вершин
    :return: двумерные координаты вершин
    """
    # Матрица масштабирования
    scaling_matrix = np.array([
        [scale_x, 0, 0],
        [0, scale_y, 0],
        [0, 0, 1]
    ])
    scaled_vertices_homogeneous = np.dot(vertices_hg, scaling_matrix.T)
    return scaled_vertices_homogeneous[:, :2]


def reflect_polygon(vertices_hg):
    """
    Преобразование отражения фигуры.
    :param vertices_hg: однородные координаты вершин
    :return: двумерные координаты вершин
    """
    # Матрица отражения относительно оси y
    reflection_matrix = np.array([
        [-1, 0, 0],
        [0, 1, 0],
        [0, 0, 1]
    ])
    reflected_vertices_homogeneous = np.dot(vertices_hg, reflection_matrix.T)
    return reflected_vertices_homogeneous[:, :2]


def translate_polygon(translate_x, translate_y, vertices_hg):
    """
    Преобразование переноса фигуры.
    :param translate_x: коэффициент смещения по оси x
    :param translate_y: коэффициент смещения по оси y
    :param vertices_hg: однородные координаты вершин
    :return: двумерные координаты вершин
    """
    # Матрица переноса
    translation_matrix = np.array([
        [1, 0, translate_x],
        [0, 1, translate_y],
        [0, 0, 1]
    ])
    translated_vertices_homogeneous = np.dot(vertices_hg, translation_matrix.T)
    return translated_vertices_homogeneous[:, :2]
