import pandas as pd
import numpy as np

df_random_nums = pd.read_csv("input_data_firstRow", nrows=1, header=None).values[0]

matrix_list = [[[int(num_str)
                 for num_str in line.split()]
                for line in one_matrix.split('\n')]
               for one_matrix in open('input_data', 'r').read().split('\n\n')]

for i in range(0, len(matrix_list)):
    matrix_list[i] = np.array(matrix_list[i])


def is_board_bingo(bingo_matrix, bingo_numbers):
    row_bingo = False
    col_bingo = False
    
    row_matrix = bingo_matrix
    col_matrix = bingo_matrix.T

    for i in range(bingo_matrix.shape[0]):
        row_bool = np.isin(row_matrix[i], bingo_numbers)
        row_bingo = row_bool.all()

        col_bool = np.isin(col_matrix[i], bingo_numbers)
        col_bingo = col_bool.all()

        if row_bingo or col_bingo:
            return True

    return row_bingo or col_bingo


def main():
    bingo_list = df_random_nums
    play_bingo = True

    while play_bingo:
        bingo_list = bingo_list[0:len(bingo_list)-1]

        for mat in matrix_list:
            bingo_reached = is_board_bingo(mat, bingo_list)

            if not bingo_reached:
                last_win_num = df_random_nums[np.isin(df_random_nums, bingo_list, invert=True)][0]
                last_win_bingo_list = np.append(bingo_list, last_win_num)

                non_picked_nums_bool = np.isin(mat, last_win_bingo_list, invert=True)
                non_picked_nums = mat[non_picked_nums_bool]
                non_picked_nums_sum = sum(non_picked_nums)

                play_bingo = False
                break

    print("The last pulled bingo number was: {}".format(last_win_num))
    print("The sum of the non-picked numbers of the winning bingo board is: {}".format(non_picked_nums_sum))
    print("Both last numbers multiplied result in: {}".format(non_picked_nums_sum*last_win_num))


if __name__ == '__main__':
    main()
