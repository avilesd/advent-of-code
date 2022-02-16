import pandas as pd

# Given a table where the most-right column is numeric (default), it will return the table with a new column
# with 1 if the previous row number was lower (has increased) or else 0
def column_increase(input_data, show_sum=True):

    relevant_col_index = input_data.shape[1] - 1
    overwrite_col_index = input_data.shape[1]
    input_data["has_increased"] = None

    for i in range(0, input_data.shape[0]):
        if i == 0:
            input_data.iloc[i, overwrite_col_index] = 0
        else:
            if input_data.iloc[i - 1, relevant_col_index] < input_data.iloc[i, relevant_col_index]:
                input_data.iloc[i, overwrite_col_index] = 1
            else:
                input_data.iloc[i, overwrite_col_index] = 0

    if show_sum:
        print("The sum of the column 'has_increased' is:", sum(input_data.iloc[:, overwrite_col_index]))

    return input_data

def main():
    data = pd.read_csv("input-data.csv", header=None)
    column_increase(data, relevant_col_index=None, show_sum=True)


if __name__ == "__main__":
    main()