# dispoints
An easy to use, versatile and lightweight python library to choose dispersed points in a scatterplot.

# How to use

Import the dispoints.py file to your project.

To use it simply call the `choose_dispersed_points(points, amount, distance_function)` function. 
- `points` is the iterable object representating the elements in your scatter plot.
- `amount` is the number of dispersed elements from `points` that you need to retrieve.
- `distance_function` is the function that calculates the distance between two elements.

The function returns the dispersed points as a list.

# Principle

The dispersed points are the m points that maximises the distances between them in a set of n points. The dispersion is the sum of all the distances between selected points.

To choose them *dispoints* uses an original greedy algorithm for performance and satisfying results, especially in large datasets. Note that greedy algorithms do not always return the optimal solution.

The goal is to iterate each point and choose it if it augments the dispersion by comparing the result with the nearest previously selected.

1) Select m elements from points
2) Iterate through all the points
3) If a point augments the dispersion compared to the nearest selected point choose it instead
4) Return the selected points
