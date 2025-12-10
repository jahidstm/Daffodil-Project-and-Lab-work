def f(x):
    return x**2


def hill_climbing(f, x0, step_size=0.1, max_iterations=100):
    x = x0
    for i in range(max_iterations):
        print(f"Iteration {i+1}: x = {x:.2f}, f(x) = {f(x):.2f}")

        neighbor_left = x - step_size
        neighbor_right = x + step_size

        f_current = f(x)
        f_left = f(neighbor_left)
        f_right = f(neighbor_right)

        if f_left < f_current:
            x = neighbor_left
        elif f_right < f_current:
            x = neighbor_right
        else:
            break

    return x


# Run Hill Climbing
initial_solution = 3.0
best_solution = hill_climbing(f, initial_solution)
print(f"\nBest solution: x = {best_solution:.2f}, f(x) = {f(best_solution):.2f}")
