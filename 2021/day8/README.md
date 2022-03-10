# References

## General information
For how I split the segments for part two, check the initial part of the code in `challenge16.py`.

The second part of this challenge was one of the most challenging tasks of aoc until now. Specially,
getting the decoding right with as minimum logic as possible.

We use two types of logical deductions. First, we count how much a segment, i.e. a letter appears in all ten segments
of the input. This allows for immediate identification of three out of seven segments: segment2, segment5 and segment6.
The segments 1 and 3 share a count of 8 and the segments 4 and 7 share a count of 7. After a small differentiation, the 
decoding is possible and deterministic.
    
## Input Data
Input data available at: https://adventofcode.com/2021/day/8