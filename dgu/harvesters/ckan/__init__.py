from typing import List, Any, Dict, Generator

from dgu.harvesters.base import HarvesterBase, Dataset, get_request_session


class CKANHarvester(HarvesterBase):

    def records(self) -> Generator:
        yield


class CKANDataset(Dataset):

    """ Converts from a CKAN dataset into a DGU dataset """
    def convert(self, data: Any) -> None:
        pass
