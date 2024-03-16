from plates import is_valid


def main():
    test_min_max_char()


def test_min_max_char():
    assert is_valid("AA") == True
    assert is_valid("AABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFGH") == False


if __name__ == "__main__":
    main()
