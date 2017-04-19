import os
import requests_mock

def setup():
    os.environ['TESTING'] = "1"

def test_uris():
    return [
        ('open.camden.gov.uk/data.json',
          open('tests/data/camden.data.json', 'r').read())
    ]

