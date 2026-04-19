def build_newton_interpolation(x_points, y_points):
    n = len(x_points)

    divided_diff = {}

    # Нулевой порядок — значения функции
    for i in range(n):
        divided_diff[(i, i)] = y_points[i]

    # Вычисляем разности более высоких порядков, начиная с 1 "табличным методом"
    for k in range(1, n):
        for i in range(n - k):
            j = i + k
            divided_diff[(i, j)] = (divided_diff[(i + 1), j] - divided_diff[(i, j - 1)]) / (x_points[j] - x_points[i])


build_newton_interpolation([2, 3, 4, 5], [7, 5, 8, 7])