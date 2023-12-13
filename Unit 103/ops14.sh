echo "Enter two numbers:"
read num1
read num2

sum=$((num1 + num2))
difference=$((num1 - num2))
product=$((num1 * num2))
if [ "$num2" -ne 0 ]; then
    quotient=$(awk "BEGIN {printf \"%.2f\", $num1/$num2}")
    echo "Sum: $sum"
    echo "Difference: $difference"
    echo "Product: $product"
    echo "Quotient: $quotient"
else
    echo "Cannot divide by zero"
fi
