import pandas as pd

class ClassiAssister() :

    def __init__(self, df) :
        self._df = df

    def describe(self) :
        columns = Config.CLASSIFIED_COLUMNS[1:] # [현상 원인 조치 요망]
        
        entire_len = self.df.shape[0]
        
        allnotfound = self._df[(notfound('현상')) & (notfound('원인')) & (notfound('조치')) & (notfound('요망'))]
        allnotfound_len = allnotfound.shape[0]
        print("classifed / entire = {}".format((entire_len - allnotfound_len) / entire_len))

        suspicious = self._df[(found('현상')) & (notfound('원인')) & (notfound('조치')) & (notfound('요망'))]
        suspicious_len = suspicious.shape[0]
        print("ensured / entire = {}".format((entire_len - suspicious_len - allnotfound_len) / entire_len))
    
    def found(self, column) :
        return self._df[column] != 'notfound'
    def notfound(self, column) :
        return self._df[column] == 'notfound'
