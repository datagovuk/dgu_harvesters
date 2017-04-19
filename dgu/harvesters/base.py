

"""
HarvesterBase provides a skeleton implementation that is overridable
by sub-classes that wish to act as a harvester for a specific type
of metadata.
"""
class HarvesterBase(object):

    """
    To be implemented by the sub-classes that implement actual
    harvesters.  The method MUST return a generator which when
    processed will provide an iterable of Dataset objects.
    """
    def records(self):
        pass

    """
    configure() will be called before any other function and the
    provided job data will passed as the sole parameter. There is
    no requirement for sub-classes to implement this method as it
    will retrieve all of the required information
    """
    def configure(self, config):
        self.id = config.get('id')
        self.user = config.get('user')

        task = config.get('task')
        self.organisation = task.get('organisation')
        self.remote_organisations = task.get('remote_organisations')
        self.url = task.get('url')

    """
    Returns the short-name of the target organisation
    """
    def get_organisation(self):
        return self.get_organisation

    """
    Returns the URL of the endpoint
    """
    def get_url(self):
        return self.url

    """
    Returns a list of remote organisations, used as a filter on
    the endpoint to limit the response
    """
    def get_remote_organisations(self):
        return self.remote_organisations

    """
    Returns the user details provided with the harvest job
    """
    def get_user(self):
        return self.user

"""
A class to hold fields that represent a dataset understood by DGU.
Subclasses of harvesters should also override this class to provide
the conversion from the endpoint format to our internal one.
"""
class Dataset(object):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    """
    Subclass implementations should implement this method to convert
    from the source format to a form understood by DGU. It should
    populate it's own fields with the appropriate values.
    """
    def convert(self, data):
        pass
