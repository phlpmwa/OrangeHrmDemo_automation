import pytest


@pytest.mark.usefixtures("chrome_browser")
class BaseTest:
    pass
