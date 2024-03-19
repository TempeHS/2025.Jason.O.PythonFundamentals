from plates import is_valid


def main():
    test_min_max_char()
    test_start_two_letters()
    test_middle_numbers()
    test_zero_first()
    test_punctuation()


def test_min_max_char():
    assert is_valid("AA") == True
    assert is_valid("AABCDEF") == True
    assert is_valid("A") == False
    assert is_valid("ABCDEFGH") == False


def test_start_two_letters():
    assert is_valid("AA") == True
    assert is_valid("A2") == False
    assert is_valid("1A") == False
    assert is_valid("07") == False


def test_middle_numbers():
    assert is_valid("ABC123") == True
    assert is_valid("ABC12D") == False


def test_zero_first():
    assert is_valid("ABC120") == True
    assert is_valid("ABC012") == False


def test_punctuation():
    assert is_valid("ABC.12") == False
    assert is_valid("ABC!12") == False
    assert is_valid("ABC 12") == False


if __name__ == "__main__":
    main()
