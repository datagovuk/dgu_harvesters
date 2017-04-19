from dgu.harvesters.base import HarvesterBase, Dataset


class CKANHarvester(HarvesterBase):

    def records(self):
        yield


class CKANDataset(Dataset):

    """ Converts from a CKAN dataset into a DGU dataset """
    def convert(self, data):
        pass
