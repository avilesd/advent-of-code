import pandas as pd

input = pd.read_csv("input_data", dtype="str", header=None)
input.rename(columns={0:"binary_input"}, inplace=True)


def main():
    for i in range(0, len(input.iloc[0,0])):
        col_index = i + 1
        col_name = "bit_" + str(col_index)
        input[col_name] = input["binary_input"].apply(lambda some_str: int(some_str[i]))

    binary_gamma = input.mean().round()[1:]
    gamma_bi_str = ""
    epsilon_bi_str = ""

    for i in binary_gamma:
        gamma_bi_str += str(int(i))
        abs_neg_i = abs(i-1)
        epsilon_bi_str += str(int(abs_neg_i))

    print("gamma_rate as binary: {}".format(gamma_bi_str))
    print("epsil_rate as binary: {}".format(epsilon_bi_str))

    # results / convert to decimal
    gamma_rate = int(gamma_bi_str, 2)
    epsilon_rate = int(epsilon_bi_str, 2)
    print("gamma_rate as binary: {}".format(gamma_rate))
    print("epsilon_rate as binary: {}".format(epsilon_rate))
    print("final result: {}".format(gamma_rate*epsilon_rate))




if __name__ == "__main__":
    main()


