

"""
HarvesterBase provides a skeleton implementation that is overridable
by sub-classes that wish to act as a harvester for a specific type
of metadata.
"""
class HarvesterBase(object):

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
