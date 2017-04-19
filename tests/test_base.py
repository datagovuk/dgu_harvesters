from dgu.harvesters.base import HarvesterBase


def test_configure_base():
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
            "type": "CKAN",
            "url": "http://demo.ckan.org/",
            "organisation": "cabinet-office",
            "remote_organisations": [
                "organisation-a",
                "organisation-b"
            ]
        }
    }

    b = HarvesterBase()
    b.configure(task)

    assert b.get_url() == task.get('task', {}).get('url')
