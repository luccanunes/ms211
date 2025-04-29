def newton(x0, f, df, dados_iteracao=[], x=[], show=False, max_iter = 1000, eps=1e-7):
    ant = x0+1
    i = 0
    dados_iteracao.append(x0)
    x.append(i)
    while abs(x0 - ant) > eps and i < max_iter:
        if show:
            print(x0)
        ant = x0
        x0 = x0 - f(x0)/df(x0)
        i += 1
        dados_iteracao.append(x0)
        x.append(i)
    return x0