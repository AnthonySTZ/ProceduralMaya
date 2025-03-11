def evenly_distribute_point_on_line(line_length, pt_nb):
    dt = line_length / pt_nb
    return [0.5 * dt + i * dt for i in range(pt_nb)]


def fit_value(value, r_min, r_max, t_min, t_max):
    return (value - r_min) / (r_max - r_min) * (t_max - t_min) + t_min
