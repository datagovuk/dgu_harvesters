import dgu.harvesters.loader as l

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

