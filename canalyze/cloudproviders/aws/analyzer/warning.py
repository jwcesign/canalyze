class Warning:
    def __init__(self, resource_name: str, region: str):
        self._resource_name = resource_name
        self._region = region

    @property
    def resource_name(self):
        return self._resource_name

    @resource_name.setter
    def resource_name(self, value):
        self._resource_name = value

    @property
    def region(self):
        return self._region

    @region.setter
    def region(self, value):
        self._region = value