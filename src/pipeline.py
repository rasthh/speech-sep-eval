from abc import ABCMeta, abstractmethod


class Pipeline(metaclass=ABCMeta):
    """A Pipeline is the main interface with a user. The user sets up
    a Pipeline specifying choices of the individual blocks, and the pipeline
    then is the overarching class that execute the final evaluation."""

    def __init__(
        self, datasets, preprocessings, models, postprocessings, metrics, reports
    ):
        self._datasets = datasets
        self._preprocessings = preprocessings
        self._models = models
        self._postprocessings = postprocessings
        self._metrics = metrics
        self._reports = reports

    @property
    @abstractmethod
    def datasets(self):
        pass

    @datasets.setter
    @abstractmethod
    def datasets(self, value):
        pass

    @property
    @abstractmethod
    def preprocessings(self):
        pass

    @preprocessings.setter
    @abstractmethod
    def preprocessings(self, value):
        pass

    @property
    @abstractmethod
    def models(self):
        pass

    @models.setter
    @abstractmethod
    def models(self, value):
        pass

    @property
    @abstractmethod
    def postprocessings(self):
        pass

    @postprocessings.setter
    @abstractmethod
    def postprocessings(self, value):
        pass

    @property
    @abstractmethod
    def metrics(self):
        pass

    @metrics.setter
    @abstractmethod
    def metrics(self, value):
        pass

    @property
    @abstractmethod
    def reports(self):
        pass

    @reports.setter
    @abstractmethod
    def reports(self, value):
        pass

    @abstractmethod
    def run(self):
        pass


class BasePipeline(Pipeline):
    """This class displays the summary of the tabular data contained
    in a CSV file"""

    @property
    def datasets(self):
        """ ... """
        pass

    @datasets.setter
    def datasets(self, value):
        pass

    @property
    def preprocessings(self):
        """ ... """
        pass

    @preprocessings.setter
    def preprocessings(self, value):
        pass

    @property
    def models(self):
        """ ... """
        pass

    @models.setter
    def models(self, value):
        pass

    @property
    def postprocessings(self):
        """ ... """
        pass

    @postprocessings.setter
    def postprocessings(self, value):
        pass

    @property
    def metrics(self):
        """ ... """
        pass

    @metrics.setter
    def metrics(self, value):
        pass

    @property
    def reports(self):
        """ ... """
        pass

    @reports.setter
    def reports(self, value):
        pass

    def run(self):
        raise NotImplementedError
