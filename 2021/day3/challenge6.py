import pandas as pd


def bit_criteria(some_column, how) -> int:
    """
    Returns either 0 or 1 depending on the criteria, as described by the Advent of Code day 3.2
    If no correct input_data is entered in how, then it just returns -1
    :param some_column: a column of a data frame
    :param how: "most_common" or "least_common"
    :return: an integer
    """

    average_of_col = some_column.mean()

    if how == "most_common":
        if average_of_col == 0.5:
            return 1
        elif average_of_col < 0.5:
            return 0
        elif average_of_col > 0.5:
            return 1
    elif how == "least_common":
        if average_of_col == 0.5:
            return 0
        elif average_of_col < 0.5:
            return 1
        elif average_of_col > 0.5:
            return 0
    else:
        return -1


def filter_bit_criteria(df, gas) -> pd.DataFrame:
    """
    A recursive function
    """
    col_to_evaluate = df.columns[1]
    if gas == "oxygen":
        common_bit = bit_criteria(df[col_to_evaluate], "most_common")
    else: # else we assume gas == "co2":
        common_bit = bit_criteria(df[col_to_evaluate], "least_common")

    df = df[df[col_to_evaluate] == common_bit]

    if df.shape[0] == 1:
        result = df
    else:
        result = filter_bit_criteria(pd.concat([df.iloc[:, 0], df.iloc[:, 2:]], axis=1), gas)
    return result


def main():
    input_data = pd.read_csv("input_data", dtype="str", header=None)
    input_data.rename(columns={0: "binary_input_data"}, inplace=True)

    for i in range(0, len(input_data.iloc[0, 0])):
        col_index = i + 1
        col_name = "bit_" + str(col_index)
        input_data[col_name] = input_data["binary_input_data"].apply(lambda some_str: int(some_str[i]))

    result_oxygen_df = filter_bit_criteria(input_data, "oxygen")
    result_oxygen_bin = result_oxygen_df.iloc[0, 0]
    result_oxygen_dec = int(result_oxygen_bin, 2)
    print("oxygen value in binary is: {}, in decimal: {}".format(result_oxygen_bin, result_oxygen_dec))

    result_co2_df = filter_bit_criteria(input_data, "co2")
    result_co2_bin = result_co2_df.iloc[0, 0]
    result_co2_dec = int(result_co2_bin, 2)
    print("co2 value in binary is: {}, in decimal: {}".format(result_co2_bin, result_co2_dec))

    print("final result", result_oxygen_dec * result_co2_dec)


if __name__ == "__main__":
    main()