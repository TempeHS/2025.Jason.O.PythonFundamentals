import fuel


def main():
    test_input()
    test_zero_division()
    test_value_error()


def test_input():
    assert fuel("1/4") == 25 and fuel("25") == "25%"
    assert fuel("1/100") == 1 and fuel("1") == "E"
    assert fuel("99/100") == 99 and fuel("99") == "F"


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        fuel("1/0")


def test_value_error():
    with putest.raises(ValueError):
        fuel("abc/123")


if __name__ == "__main__":
    main()
