import json

from dgu.harvesters.base import HarvesterBase, Dataset, get_request_session

from dotmap import DotMap

class DataJsonHarvester(HarvesterBase):

    def records(self):
        text = get_request_session().get(self.get_url()).text
        data = DotMap(json.loads(text))
        remote_orgs = self.get_remote_organisations()

        for dataset_blob in data.dataset:
            dataset = DotMap(dataset_blob)
            d = DataJsonDataset()
            d.convert(dataset)

            # Check remote_organisations for a match unless remote
            # organisations is empty
            if remote_orgs:
                org = dataset.publisher.name
                if not org in remote_orgs:
                    continue

            yield d

""" Converts from a DataJson dataset into a DGU dataset """
class DataJsonDataset(Dataset):

    def convert(self, data):
        pass
