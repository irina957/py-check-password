import pytest
from app.main import check_password


@pytest.mark.parametrize("passwords, expected",
                         [("Pass@word1", True),
                          ("pass!WOrd1", True),
                          ("pass@WOrdd", False),
                          ("Pass@", False),
                          ("pass@word1", False),
                          ("passsWOrd1", False),
                          ("pass@WOrddpass@WOrddd", False),
                          ("pass@WOrd1.", False),
                          ("пар@WOrd1.", False),
                          ("Pass@w1r", True),
                          ("Pass@word1111111", True),
                          ("", False),
                          ("Pard1$@#&!-_", True)
                          ])
def test_check_passwords_with_different_data(
        passwords: str, expected: bool) -> None:
    assert check_password(passwords) == expected
