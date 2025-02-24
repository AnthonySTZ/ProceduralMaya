def evenly_distribute_point_on_line(line_length, pt_nb):
    dt = line_length / pt_nb
    return [0.5 * dt + i * dt for i in range(pt_nb)]
