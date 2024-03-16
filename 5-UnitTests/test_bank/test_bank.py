import bank


def test_return_zero():
    assert bank("hello gi") == 0
    assert bank("Hello") == 0
    assert bank("HeLlo Gi") == 0


if __name__ == "__main__":
    main()
