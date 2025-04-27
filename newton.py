def newton(x0, f, df, show=False, max_iter = 1000, eps = 1e-10):
    ant = 0
    i = 0
    while abs(x0 - ant) > eps and i < max_iter:
        if show:
            print(x0)
        ant = x0
        x0 = x0 - f(x0)/df(x0)
        i += 1
    return x0