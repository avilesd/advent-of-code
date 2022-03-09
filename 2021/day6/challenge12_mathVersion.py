import pandas as pd

# Import and transform data
input_array = [int(str_num) for str_num in open('input_data', 'r').read().split(',')]

state_col = pd.DataFrame([0, 1, 2, 3, 4, 5, 6, 7, 8])\
    .rename(columns={0:'all_states'})

population_count = pd.DataFrame(input_array, columns=['state'])\
    .value_counts()\
    .rename_axis('state')\
    .reset_index(name='state_count')

initial_pop_state = pd.merge(state_col, population_count, how='left', left_on='all_states', right_on='state')\
    .drop(columns=['state'])\
    .fillna(0)\
    .astype({'state_count': 'int64'})


def new_population(initial_df):
    """
    Calculates the population of laternfish according to rules from Advent of Code 2021.6.2
    :param initial_df: the initial population dataframe containing two columns 'all_states' and 'state_count'
    :return: a new dataframe of the same structure with an updated 'state_count' column
    """
    new_df = initial_df.copy()

    for key, values in initial_df.iterrows():
        state = values[0]

        if state == 6:
            count_0 = initial_df.loc[new_df["all_states"] == 0]["state_count"]
            count_7 = initial_df.loc[new_df["all_states"] == (state + 1)]["state_count"]
            new_count = int(count_0) + int(count_7)
            new_df.loc[new_df["all_states"] == state, "state_count"] = new_count

        elif state == 8:
            count_0 = initial_df.loc[new_df["all_states"] == 0]["state_count"]
            new_count = int(count_0)
            new_df.loc[new_df["all_states"] == state, "state_count"] = new_count

        else:
            count_s_plus_1 = initial_df.loc[new_df["all_states"] == (state + 1)]["state_count"]
            new_count = int(count_s_plus_1)
            new_df.loc[new_df["all_states"] == state, "state_count"] = new_count

    return new_df


def recursive(previous_state, days):
    """
    A function that runs the function 'new_population' recursively by passing the previous_state param and the number of
    iterations to run (days param)
    :return: the final result after 'days' number of recursive iterations of 'new_population' function
    """
    if days == 1:
        result = new_population(previous_state)
    else:
        result = recursive(new_population(previous_state), days-1)

    return result


def main():
    final_state = recursive(initial_pop_state, 256)
    print(sum(final_state["state_count"]))
    pass


if __name__ == '__main__':
    main()

