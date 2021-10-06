from hello import add


def test_add():
    assert add(1, 2) == 3


from change_app import change


def test_change():
    assert [{5: "quarters"}, {1: "nickels"}, {4: "pennies"}] == change(1.34)
