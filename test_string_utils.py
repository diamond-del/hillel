from utils import string_utils


def test_string_utils1():
    actual_result = string_utils.deleting_blank("qweqweqweqdsaasdqe")
    expected_result = "qweqweqweqdsaasdqe"
    assert actual_result == expected_result


def test_string_utils2():
    actual_result = string_utils.deleting_blank("qweqwe qwe qdsa asd q")
    expected_result = "qweqweqweqdsaasdq"
    assert actual_result == expected_result


def test_string_utils3():
    actual_result = string_utils.deleting_blank("12312124324324")
    expected_result = "qweqweqweqdsaasdq"
    assert not actual_result == expected_result
