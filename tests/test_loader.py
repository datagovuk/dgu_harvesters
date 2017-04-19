import dgu.harvesters.loader as l
from tests.test_data import TASK

def test_known():
    known_types = l.known_harvester_types()
    assert 'ckan' in known_types
    assert 'data_json' in known_types

def test_load_ckan():
    h = l.get_harvester('ckan')
    assert h.__name__ == 'CKANHarvester'

def test_load_datajson():
    h = l.get_harvester('data_json')
    assert h.__name__ == 'DataJsonHarvester'

def test_load_from_task():
    h = l.get_configured_harvester_from_task(TASK)
    assert h.__class__.__name__ == 'CKANHarvester'
    assert h.get_url() == TASK.get('task', {}).get('url')
