def config_axes(ax):
    # Настройка граничных значений осей
    ax.set_xlim(-4, 4)
    ax.set_ylim(-4, 4)

    # Настройка соотношения сторон графика
    ax.set_aspect('equal', adjustable='box')

    # Настройка spines для перемещения осей к центру
    ax.spines['left'].set_position('zero')
    ax.spines['left'].set_color('black')
    ax.spines['left'].set_linewidth(0.5)
    ax.spines['bottom'].set_position('zero')
    ax.spines['bottom'].set_color('black')
    ax.spines['bottom'].set_linewidth(0.5)

    # Убираем верхнюю и правую границы
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')

    # Настройка меток осей
    ax.tick_params(axis='x', labelsize=8)
    ax.tick_params(axis='y', labelsize=8)

    # Настройка подписи осей
    ax.annotate('x', xy=(4, 0), xytext=(4.1, 0.1), fontsize=10)
    ax.annotate('y', xy=(0, 4), xytext=(0.1, 4.1), fontsize=10)
