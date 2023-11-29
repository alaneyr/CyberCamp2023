#!/bin/bash
# Given three integers (, , and ) representing the three sides of a triangle, identify whether the triangle is scalene, isosceles, or equilateral.
# If all three sides are equal, output EQUILATERAL.
# Otherwise, if any two sides are equal, output ISOSCELES.
# Otherwise, output SCALENE.
# Input Format
# Three integers, each on a new line.
# Constraints
# The sum of any two sides will be greater than the third.
# Output Format
# One word: either "SCALENE" or "EQUILATERAL" or "ISOSCELES" (quotation marks excluded).

#!/bin/bash

# Read three integers representing the sides of a triangle
read side1
read side2
read side3

# Check if it's an equilateral triangle
if [ $side1 -eq $side2 ] && [ $side2 -eq $side3 ]; then
    echo "EQUILATERAL"
# Check if it's an isosceles triangle
elif [ $side1 -eq $side2 ] || [ $side1 -eq $side3 ] || [ $side2 -eq $side3 ]; then
    echo "ISOSCELES"
# If none of the above conditions are met, it's a scalene triangle
else
    echo "SCALENE"
fi