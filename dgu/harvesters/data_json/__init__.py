from typing import List, Any, Dict, Generator
import json

from dgu.harvesters.base import HarvesterBase, Dataset, get_request_session

from dotmap import DotMap

class DataJsonHarvester(HarvesterBase):

    def records(self) -> Generator:
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

    def convert(self, data: Any) -> None:
        """
        {
            "accessLevel": "public",
            "landingPage": "https://opendata.camden.gov.uk/d/tpym-hws7",
            "issued": "2017-04-13",
            "@type": "dcat:Dataset",
            "modified": "2017-04-13",
            "keyword": [
                "public health",
                "health",
                "jsna",
                "alcohol"
            ],
            "contactPoint": {
                "@type": "vcard:Contact",
                "fn": "<Nobody>",
                "hasEmail": "mailto:PublicHealth.Intelligence@islington.gov.uk"
            },
            "publisher": {
                "@type": "org:Organization",
                "name": "opendata.camden.gov.uk"
            },
            "identifier": "https://opendata.camden.gov.uk/api/views/tpym-hws7",
            "description": "This public health factsheet describes facts, assets, and strategies related to alcohol health impacts in Camden.",
            "title": "Alcohol",
            "distribution": [
                {
                    "@type": "dcat:Distribution",
                    "downloadURL": "https://opendata.camden.gov.uk/download/tpym-hws7/application/pdf",
                    "mediaType": "application/pdf"
                }
            ],
            "theme": [
                "Health"
            ]
        }
        """
