import bank


def test_return_zero():
    assert bank("hello gi") == 0
    assert bank("Hello") == 0
    assert bank("HeLlo Gi") == 0


def test_return_20():
    assert bank("Hi") == 20
    assert bank("Hey") == 20


def test_return_100():
    assert bank("What's up?") == 100
    assert bank("good morning") == 100


if __name__ == "__main__":
    main()
