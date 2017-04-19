from dgu.harvesters.base import HarvesterBase

from tests.test_data import TASK

def test_configure_base():

    b = HarvesterBase()
    b.configure(TASK)

    assert b.get_url() == TASK.get('task', {}).get('url')
