import pandas as pd
from challenge_one import column_increase


def main():
    # print(input_data.shape)
    input_data = pd.read_csv("input-data.csv", header=None)
    input_data.rename(columns= {0:'data'}, inplace=True)
    length_of_data = input_data.shape[0]
    input_data["sum_3_column"] = 0

    stop_iteration = length_of_data - 2

    for i in range(0, length_of_data):
        if i == 0:
            input_data.iloc[i, 1] = sum(input_data.iloc[i:i + 3, 0])
        else:
            if i+1 <= stop_iteration:
                input_data.iloc[i, 1] = sum(input_data.iloc[i:i+3, 0])
            else:
                input_data.iloc[i, 1] = 0

    print(input_data.head(5))
    print(input_data.tail(5))

    debugres = column_increase(input_data, show_sum=True)

    print(debugres.head(5))
    print(debugres.tail(5))


if __name__ == "__main__":
    main()