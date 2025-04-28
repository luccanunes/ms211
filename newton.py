def newton(x0, f, f_linha, dados_iteracao=[], x=[], show=False, max_iter = 1000):
    ant = x0+1
    i = 0
    dados_iteracao.append(x0)
    x.append(i)
    while abs(x0-ant)>0.0000001 and i < max_iter:
        if show:
            print(x0)
        ant = x0
        x0 = x0 - f(x0)/f_linha(x0)
        i += 1
        dados_iteracao.append(x0)
        x.append(i)

def newton_lucca(x0, f, df, show=False, max_iter = 1000, eps = 1e-10):
    ant = 0
    i = 0
    while abs(x0 - ant) > eps and i < max_iter:
        if show:
            print(x0)
        ant = x0
        x0 = x0 - f(x0)/df(x0)
        i += 1
    return x0
