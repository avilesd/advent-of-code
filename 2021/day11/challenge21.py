import pandas as pd
import numpy as np

from functools import wraps
from time import time


def timeit(f):
    @wraps(f)
    def wrap(*args, **kw):
        ts = time()
        result = f(*args, **kw)
        tf = time()
        print(f'func:{f.__name__} took: {tf-ts} seconds')
        return result
    return wrap


def df_convert_9_to_99(df):
    res_df = df.applymap(lambda x: 99 if x == 9 else x)
    return res_df


def df_convert_larger9_to_99(df):
    res_df = df.applymap(lambda x: 99 if x > 9 else x)
    return res_df


def if_num_larger_n_then_1(x, n):
    if x != 'x':
        bool1 = x >= n
        bool2 = x < 18
        bool_res = bool1 & bool2
        if bool_res:
            return 1
        else:
            return 0
    else:
        return 0


def get_neighbor_value(df, some_coord):
    non_negative_out_of_bound = some_coord >= 0
    non_out_of_bound_row = some_coord[0] <= (df.shape[0] - 1)
    non_out_of_bound_col = some_coord[1] <= (df.shape[1] - 1)

    all_bool = non_negative_out_of_bound.all() & non_out_of_bound_row & non_out_of_bound_col

    if all_bool:
        return df.iloc[some_coord[0], some_coord[1]]
    else:
        return 'x' # 'x' for neighbor out of bound, no particular meaning it just cannot be 0


def count_n_neighbors(df, i, j, n):
    nw_value = get_neighbor_value(df, np.array([i-1, j-1]))
    nn_value = get_neighbor_value(df, np.array([i-1, j]))
    ne_value = get_neighbor_value(df, np.array([i-1, j+1]))
    ee_value = get_neighbor_value(df, np.array([i, j+1]))
    se_value = get_neighbor_value(df, np.array([i+1, j+1]))
    ss_value = get_neighbor_value(df, np.array([i+1, j]))
    sw_value = get_neighbor_value(df, np.array([i+1, j-1]))
    ww_value = get_neighbor_value(df, np.array([i, j-1]))

    neighbor_value = [nw_value, nn_value, ne_value, ee_value, se_value, ss_value, sw_value, ww_value]
    res_count = [if_num_larger_n_then_1(xx, n)
                 for xx in neighbor_value]
    return sum(res_count)


def add_matrix_based_on_neighbor(df, n_special, n_special_new_value, n):
    n_rows = df.shape[0]
    n_cols = df.shape[1]

    res_df = pd.DataFrame(np.zeros((n_rows, n_cols)).astype(int))

    for i in range(n_rows):
        for j in range(n_cols):
            if df.iloc[i, j] >= n_special:
                res_df.iloc[i, j] = n_special_new_value
            else:
                res_df.iloc[i, j] = count_n_neighbors(df, i, j, n)

    return res_df


def any_largerEqualN_in_df(df, n):
    bool_vec = df >= n
    bool_vec_2 = df < 50
    bool_all = bool_vec & bool_vec_2
    return bool_all.any().any()


def add_1_if_not_99(df):
    res_df = df.applymap(lambda x: x+1 if x != 99 else x)
    return res_df


def marker_to_0(df):
    res_df = df.applymap(lambda x: 0 if x > 98 else x)
    return res_df


def count_flashes(df):
    return sum(sum(df.values == 0))


@timeit
def main():
    input_data = [[int(i) for i in line]
                  for line in open('input_data', 'r').read().split('\n')]

    grid0 = pd.DataFrame(input_data)

    flash_counter = 0
    for i in range(100):
        if i != 0:
            grid0 = grid_final

        matrix_to_add = add_matrix_based_on_neighbor(grid0, 9, 0, 9)
        grid00 = df_convert_9_to_99(grid0)
        grid_i = grid00 + matrix_to_add

        while any_largerEqualN_in_df(grid_i, 10):
            i_to_add_on_10 = add_matrix_based_on_neighbor(grid_i, 99, 99, 10)
            grid_i = df_convert_larger9_to_99(grid_i)
            grid_i = grid_i + i_to_add_on_10

        grid_i = add_1_if_not_99(grid_i)

        while any_largerEqualN_in_df(grid_i, 10):
            i_to_add_on_10 = add_matrix_based_on_neighbor(grid_i, 99, 99, 10)
            grid_i = df_convert_larger9_to_99(grid_i)
            grid_i = grid_i + i_to_add_on_10

        final_add_matrix = add_matrix_based_on_neighbor(grid_i, 99, 99, 10)
        grid_i = df_convert_larger9_to_99(grid_i + final_add_matrix)
        grid_final = marker_to_0(grid_i)
        flashes_per_iteration = count_flashes(grid_final)
        flash_counter += flashes_per_iteration

    print(grid_final)
    print(flash_counter)


if __name__ == "__main__":
    main()
