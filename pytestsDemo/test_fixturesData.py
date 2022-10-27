import pytest

from pytestsDemo.BaseClass import BaseClass


@pytest.mark.usefixtures("dataLoad")
class TestExample2(BaseClass):

    def test_editProfile(self, dataLoad):
        log = self.get_logger()
        log.info(dataLoad[0])
        log.info(dataLoad[1])
        log.info(dataLoad[2])
        print(dataLoad)
