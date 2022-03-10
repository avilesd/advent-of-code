import numpy as np

input_data = np.array([int(str_num) for str_num in open('input_data', 'r').read().split(',')])
min_x = np.min(input_data)
max_x = np.max(input_data)


def fuel_consumption(x_pos, x_goal):
    steps_to_goal = abs(x_pos - x_goal)
    consumed_fuel = sum(range(1, steps_to_goal+1, 1))
    return consumed_fuel


vec_fuel_consumption = np.vectorize(fuel_consumption)

for goal in range(min_x, max_x+1, 1):
    sum_of_consumption = np.sum(vec_fuel_consumption(input_data, goal))

    if goal == min_x:
        min_sum = sum_of_consumption
        optimal_x = goal
    else:
        if sum_of_consumption < min_sum:
            min_sum = sum_of_consumption
            optimal_x = goal


def main():
    print(f"The optimal horizontal position is:{optimal_x}. This results in the minimized sum of differences:{min_sum}")
    print(f"The optimal horizontal position should be near the {np.mean(input_data)}")
    pass


if __name__ == "__main__":
    main()
