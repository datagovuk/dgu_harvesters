from typing import List, Dict

from .base import HarvesterBase
from .ckan import CKANHarvester
from .data_json import DataJsonHarvester

import logging
log = logging.getLogger(__name__)

HARVESTERS = {
    'data_json': DataJsonHarvester,
    'ckan': CKANHarvester
}

def known_harvester_types() -> List[str]:
    return HARVESTERS.keys()

def get_harvester(name: str) -> HarvesterBase:
    return HARVESTERS.get(name,{})

def get_configured_harvester_from_task(task: Dict) -> HarvesterBase:
    task_type = task.get('task', '').get('type')
    harvester_class = get_harvester(task_type)
    if not harvester_class:
        log.error('Invalid task_type "{}" supplied'.format(task_type))
        return None

    harvester = harvester_class()
    harvester.configure(task)

    return harvester
