from dgu.harvesters.base import HarvesterBase, Dataset


class DataJsonHarvester(HarvesterBase):
    pass

""" Converts from a DataJson dataset into a DGU dataset """
class DataJsonDataset(Dataset):

    def convert(self, data):
        pass
