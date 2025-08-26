import math
import pytest
from cnyt_complejos import (suma, resta, producto, division, modulo, 
                        conjugado, fase, polares, cartesianas)

#suma
def t_suma():
    assert suma((3, 2), (1, 4)) == (4, 6)
    assert suma((-1, -1), (1, 1)) == (0, 0)

#resta
def t_resta():
    assert resta((5, 3), (2, 1)) == (3, 2)
    assert resta((0, 0), (2, 3)) == (-2, -3)

#producto
def t_producto():
    assert producto((2, 3), (1, -1)) == (5, 1)
    assert producto((0, 1), (0, 1)) == (-1, 0)   # i*i = -1

#división
def _division():
    assert division((1, 2), (3, -1)) == (0.1, 0.7)
    assert division((2, 2), (1, 1)) == (2.0, 0.0)

#módulo
def t_modulo():
    assert modulo((3, 4)) == 5
    assert math.isclose(modulo((1, 1)), math.sqrt(2))

#conjugado
def t_conjugado():
    assert conjugado((3, -5)) == (3, 5)
    assert conjugado((0, 7)) == (0, -7)

def t_fase():
    assert math.isclose(fase((1, 0)), 0.0)
    assert math.isclose(fase((0, 1)), math.pi/2)

#polares
def t_polares():
    r, ang = polares((3, 4))
    assert math.isclose(r, 5.0)
    assert math.isclose(ang, math.atan2(4, 3))
    
    r, ang = polares((1, 1))
    assert math.isclose(r, math.sqrt(2))
    assert math.isclose(ang, math.pi/4)

#cartesianos
def t_cartesianas():
    real, imag = cartesianas((5, math.atan2(4, 3)))
    assert math.isclose(real, 3.0, rel_tol=1e-9)
    assert math.isclose(imag, 4.0, rel_tol=1e-9)

    real, imag = cartesianas((math.sqrt(2), math.pi/4))
    assert math.isclose(real, 1.0, rel_tol=1e-9)
    assert math.isclose(imag, 1.0, rel_tol=1e-9)
