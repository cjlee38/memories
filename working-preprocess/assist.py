import pandas as pd
from config import Config
from vo import ClassifiedVO

class ClassDescriber() :

    def __init__(self, result) :
        self._result = result
        self._df = result.to_df()

    def describe(self) :
        columns = Config.CLASSIFIED_COLUMNS[1:] # [현상 원인 조치 요망]
        passed_len = self._df.shape[0]
        
        print("checking passed ...")
        print("passed({}) / entire({}) = {}%".format(*self.ratio(len(self._result.success()), len(self._result.success()) + len(self._result.fail()))))
        
        print("checking passed and found at least one ...")
        allnotfound = self._df[(self.notfound('현상')) & (self.notfound('원인')) & (self.notfound('조치')) & (self.notfound('요망'))]
        allnotfound_len = allnotfound.shape[0]
        print("classified({}) / passed({}) = {}%".format(*self.ratio(passed_len - allnotfound_len, passed_len)))

        
        print("checking passed and ensured ...")
        suspicious = self._df[(self.found('현상')) & (self.notfound('원인')) & (self.notfound('조치')) & (self.notfound('요망'))]
        suspicious_len = suspicious.shape[0]
        print("ensured({}) / passed({}) = {}%".format(*self.ratio(passed_len - suspicious_len - allnotfound_len, passed_len)))

    def ratio(self, numerator, denominator) :
        return numerator, denominator, numerator / denominator * 100    
    def found(self, column) :
        return self._df[column] != 'notfound'
    def notfound(self, column) :
        return self._df[column] == 'notfound'
