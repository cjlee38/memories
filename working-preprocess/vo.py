
from abc import *
from enums import Status
from config import Config

import pandas as pd

class ResultVO(ABC) :

    _status = None
    _data = None

    @abstractmethod
    def status(self) :
        pass

    @abstractmethod
    def get(self) :
        pass

    @abstractmethod
    def to_df(self) :
        pass

class ClassifiedVO(ResultVO) :

    def __init__(self, status, data) :
        self._status = status
        self._data = data
    
    def status(self) :
        return self._status
    
    def get(self) :
        return self._data

    def to_df(self) :
        if self._status != Status.OK :
            raise Exception("Status is {}, Check data".format(self._status))

        df = pd.DataFrame(self._data['success'], columns = Config.CLASSIFIED_COLUMNS)
        return df

    def success(self) :
        return self._data['success']

    def fail(self) :
        return self._data['fail']