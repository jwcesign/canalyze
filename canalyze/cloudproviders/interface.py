import abc

class CloudProvider(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def __init__(self, region: str):
        pass

    @abc.abstractmethod
    def analyze(self):
        pass


def Analyzer(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def analyze(self):
        pass

    @abc.abstractmethod
    def recommendations(self):
        pass