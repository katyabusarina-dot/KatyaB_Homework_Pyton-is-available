import pytest
from string_utils import StringUtils


string_utils = StringUtils()

# тесты для функции capitalize


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("хочу в отпуск", "Хочу в отпуск"),
    ("27 августа 2028", "27 августа 2028"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


# тесты для функции trim


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("   skypro", "skypro"),
    (" терминал работает", "терминал работает"),
    ("  6739", "6739"),
    ("   ", ""),
    ("", ""),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    (None, TypeError),
    ([], TypeError),
    (1, TypeError),
])
def test_trim_negative(input_str, expected):
    with pytest.raises(expected):
        StringUtils.trim(input_str)

# тесты для функции contains


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "Pro", True),
    ("", "A", False),
    ("Test", "", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("sky pro", " ", True),
    ("abc", "", True),
    ("", "1", False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected

# тесты для функции delete_symbol


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("SkyPro", "x", "SkyPro"),
    ("aaaa", "a", ""),
])
def test_delete_symbol_positive(input_str, symbol, expected):
    assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    (None, 's', TypeError),
    ("SkyPro", None, TypeError),
    ([], 's', TypeError),
    ("SkyPro", 1, TypeError),
])
def test_delete_symbol_negative(input_str, symbol, expected):
    with pytest.raises(expected):
        StringUtils.delete_symbol(input_str, symbol)
