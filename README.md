# DGU Harvesters

This repository contains the code for individual harvesters for DGU.  These
are individual modules where each is able to harvest from a specific endpoint.

## Installation

Harvesters are intended for use within a worker process that obtains jobs
to execute from a message queue.

## Running tests


## Jobs

The jobs provided to the harvesting code should be serialised as JSON and contain the following fields in order to be processed.

The outer envelope should look like:

|Name|Use|
|----|----|
|id|A unique identifier for the message (UUID)|
|created|The iso8601 formatted time for when the job was created|
|user|See user object below |
|task|See task object below |

The user object:

|Name|Use|
|----|----|
|username|The username of the user this task should run as|
|token|An authz token for any API calls|
|email|The user's email address|
|notify|Boolean. Should we notify the user at the end of the run|

The task object:

|Name|Use|
|----|----|
|type|The type of the endpoint|
|url|The endpoint|
|organisation|The shortname of the target organisation where datasets will be created/updated|
|remote_organisations|A list of remote organisations to harvest from. The contents of the list will vary based on the type of the task. e.g. CKAN will be short-names, datajson will be publisher URLs|

An example job:

```json
{
    "id": "61457864-F8E4-41B9-A336-DAEADA9A7EFE",
    "created": "2017-09-03T20:56:35.450686Z",
    "user": {
        "username": "ross",
        "token": "a token",
        "email": "user@server",
        "notify": false
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
```

## Task types

The currently supported task types are:

* datajson - A data.json endpoint
* ckan - A standard CKAN.org instance

## Harvesting notes

In cases where the remote system does not support organisations it should be possible to re-use categories or a related field for remote_organisations.

Any datasets created MUST include a harvest_id field that will not change from run to run.  For instance, for a dataset created from a CKAN instance the harvest_id should be the source ID.  This can then be checked on each run to see if an update or create event should be actioned.

