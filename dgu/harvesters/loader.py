from .ckan import CKANHarvester
from .data_json import DataJsonHarvester

HARVESTERS = {
    'data_json': DataJsonHarvester,
    'ckan': CKANHarvester
}

def known_harvester_types():
    return HARVESTERS.keys()

def get_harvester(name):
    return HARVESTERS.get(name,{})
