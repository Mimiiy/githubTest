
import pytest
from esl import * 


#test that old firmware version is offline. 
#test that all 6 devices are updated.
@pytest.mark.parametrize("id, version, status", 
                         [("1", "1.0.0", "offline")])
def no_update(id, version, status):
    device = ESLDevice(id)
    assert device.status == status


@pytest.mark.parametrize("id", ["1", "2", "3","4", "5", "6"])
def test_update(id):

    version = "2.0.0"
    expected_status = "online"
    device = ESLDevice(id)
    device.update_firmware(version)
    assert device.status == expected_status 
    
@pytest.mark.parametrize("id, f_version, exp_version, state", 
                         [("1", "2.0.0", "2.0.0", True),
                         ("2", "1.0.0", "2.0.0", False),
                         ("3", "2.0.0", "1.0.0", False)])
def verify_update(id, f_version, exp_version, state):
    device = ESLDevice(id)
    device.update_firmware(f_version)
    verification = device.verify_update(exp_version)
    assert  verification == state


    




