def gradient_descent_quadratic(a, b, c, x0, lr, steps):
    """
    Return final x after 'steps' iterations.
    """
    x_new = x0
    for i in range(0, steps):
        derivative = 2*a*x_new + b
        x_new = x_new - lr*derivative

    return x_new