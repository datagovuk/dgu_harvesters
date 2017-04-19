import dgu.harvesters.loader as l

def test_harvest_camden():
    task = {
        "id": "61457864-F8E4-41B9-A336-DAEADA9A7EFE",
        "created": "2017-09-03T20:56:35.450686Z",
        "user": {
            "username": "ross",
            "token": "a token",
            "email": "user@server",
            "notify": False
        },
        "task": {
            "type": "data_json",
            "url": "mock://open.camden.gov.uk/data.json",
            "organisation": "cabinet-office",
            "remote_organisations": ["opendata.camden.gov.uk"]
        }
    }

    harvester = l.get_configured_harvester_from_task(task)
    records = list(harvester.records())
    assert len(records) == 266, len(records)

