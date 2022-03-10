# References
## Regarding challenge 7.1
The median has the nice characteristic of minimizing the sum of differences, so for this challenge, that 
ought to be the optimal horizontal position, i.e. the position that minimizes the sum of positional differences to all
the submarine crabs.

## Regarding challenge 7.2:
First approach: brute force trying all possible sums of fuel consumptions and getting the minimum of that

Another,perhaps more efficient idea, which we did not implement here would be to get the mean and check the distribution 
of the data. In this way you can approximately determine a small interval where the optimal horizontal point would be 
that minimizes the sum of fuel consumption. With some more thought, you could mathematically minimize the interval or 
interval width, such that the optimal horizontal point you are looking for would be within the interval,
with 100 % certainty.

First thoughts are interval within [mean - 1*stddev, mean + 1*stddev, but even that may bet too wide an interval.

For comparison's sake, we also print the mean, which is only 0.509 away from the optimal horizontal position. 

Input data available at: https://adventofcode.com/2021/day/7