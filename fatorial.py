def fatorial(n):
    if n<=1: #base da recursão: casos triviais n=0 ou n=1
        return 1
    else:
        return n * fatorial(n-1) #chamada recursiva


import pytest
@pytest.mark.parametrize("entrada, esperado", [
    (0, 1),
    (1, 1),
    (2, 2),
    (3, 6),
    (4, 24),
    (5, 120),
    (6, 720),
    (7, 5040)
    ])

def testa_fatorial(entrada, esperado):
    assert fatorial(entrada) == esperado
    
