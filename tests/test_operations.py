import math
import pytest

from calculator.operations import (
    addition,
    subtraction,
    multiplication,
    division,
    exponential,
    square_root,
)


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),
    (-2, 3, 1),
    (0, 5, 5),
])
def test_addition(a, b, expected):
    assert addition(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, -1),
    (-2, 3, -5),
    (0, 5, -5),
])
def test_subtraction(a, b, expected):
    assert subtraction(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 2),
    (-2, 3, -6),
    (0, 5, 0),
])
def test_multiplication(a, b, expected):
    assert multiplication(a, b) == expected


@pytest.mark.parametrize("a, b, expected", [
    (6, 3, 2),
    (1, 2, 0.5),
    (-8, 2, -4),
])
def test_division(a, b, expected):
    assert division(a, b) == expected


def test_division_by_zero():
    with pytest.raises(ValueError, match="Divisão por zero não é permitida"):
        division(1, 0)


@pytest.mark.parametrize("a, b, expected", [
    (2, 3, 8),
    (-2, 3, -8),
    (0, 5, 0),
])
def test_exponential(a, b, expected):
    assert exponential(a, b) == expected


def test_square_root():
    assert square_root(4) == 2


def test_square_root_irrational():
    assert square_root(2) == pytest.approx(math.sqrt(2))


def test_square_root_of_negative_number():
    with pytest.raises(ValueError, match="Raiz quadrada de números negativos não é permitida"):
        square_root(-4)