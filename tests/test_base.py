import dgu.harvesters.base as b

def test_known():
    known_types = b.known_harvester_types()
    assert 'ckan' in known_types
    assert 'data_json' in known_types


