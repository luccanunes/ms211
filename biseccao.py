def biseccao(f, a, b, n = 100):
    x = (a + b) // 2
    for _ in range(n):
        if f(a) * f(x) <= 0:
            b = x
        else:
            a = x
    return (x, a , b)


