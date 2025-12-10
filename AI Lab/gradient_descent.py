def f(x):
    return x**2 + 4*x + 4
def df(x):
    return 2*x + 4
def gradient_descent(starting_point, learning_rate, iterations):
    x = starting_point
    for i in range(iterations):
        x = x - learning_rate * df(x)  # update step
        print(f"Iteration {i+1}: x = {x:.4f}, f(x) = {f(x):.4f}")
    return x

starting_point = 0
learning_rate = 0.1
iterations = 10

minimum = gradient_descent(starting_point, learning_rate, iterations)
print(f"\nLocal minimum occurs at x = {minimum:.4f}, f(x) = {f(minimum):.4f}")