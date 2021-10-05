import sys
import pandas as pd

from abc import *
import config

class AbstractClassifier(ABC) :

    @abstractmethod
    def classify(self) :
        pass

    @abstractmethod
    def get(self) :
        pass

class LangClassifier(AbstractClassifier) :

    def __init__(self, patterns) :
        self.classes = {}
        self.validate_patterns(patterns)
        self._patterns = patterns
    
    def validate_patterns(self, patterns) :
        if 'kor' not in patterns.keys() :
            raise "korean must exists"
        if 'etc' not in patterns.keys() :
            raise "etc must exists"
        
    def classify(self, descriptions, threshold = -1) :
        if threshold == -1:
            threshold = (2 ** 31) - 1
        if isinstance(descriptions, str) :
            return self._classify(descriptions, threshold)
        for desc in descriptions :
            class_ = self.classify(desc, threshold)
            if not self._classes.get(class_) :
                self._classes[class_] = []
            self._classes[class_].append(desc)
        return self._classes

    def _classify(self, desc, threshold) :
        if len(desc) < threshold :
            return 'useless'
        if self._patterns['kor'].search(desc) :
            return 'kor'
        if self._patterns['etc'].search(desc) : # be careful on odering
            return 'etc'
        return 'eng'
    
    def get(self) :
        return self._classes

class FrameClassifier(AbstractClassifier) :

    @abstractmethod
    def to_df(self) :
        pass

class SplitClassifier(FrameClassifier) :

    def __init__(self, pattern) :
        self._pattern = pattern
        self._success = []
        self._fails = []

    def classify(self, descriptions) :
        if isinstance(descriptions, str) :
            return self._classify(descriptions)
        for desc in descriptions :
            flag, splt = self._classify(desc)
            to_save = self._success if flag else self._fails
            to_save.append([desc, *splt])
        return self.get()
    
    def _classify(self, desc) :
        splt = [i for i in self._pattern.split(desc) if i != '']
        return (is_success(splt), splt)

    def is_success(splt) :
        if len(s) == 5 :
            return True
        return False

    def get(self) :
        return {
            'success' : self._success,
            'fail' : self._fails
        }

    def to_df(self) :
        df = pd.DataFrame(self._success) \
            .drop([1], axis = 1) # drop '[C]' columns
        df.columns = Config.CLASSIFIED_COLUMNS
        return df

class SearchClassifier(FrameClassifier) :

    def __init__(self, rgroup) :
        self._rgroup = rgroup
        self._successes = []
        self._fails = []
    
    def classify(self, descriptions) :
        if isinstance(descriptions, str) :
            return self._classify(descriptions)
        for desc in descriptions :
            try :
                splt = self._classify(desc)
                self._successes.append(splt)
            except Exception as e :
                print(e) # todo : to logger except for printing
                self._fails.append(desc)
        return self.get()

    def _classify(self, desc) :
        x = [desc]
        candidates = []
        for regex in self._rgroup :
             # ex) {'A' : <pattern>, 'B' : <pattern>}
            splt = [parse(p, desc) for n, p in regex.items()]
            if isOK(desc, temp) :
                x.extend(temp)
                return x
            candidates.append(splt)
        return find_best(x, candidates)
            
    def parse(p, desc) :
        r = p.search(desc)
        text = None
        if r :
            buf = r.group('text')
            text = buf if buf else 'empty'
        else :
            text = 'notfound'
        return text.strip()
    
    def isOK(desc, splt) :
        # '현상' 이 없는 경우
        if splt[0] == 'notfound' and '현상' in msg :
            return False
        # all not found
        if splt[0] == 'notfound' and splt[1] == 'notfound' and splt[2] == 'notfound' and splt[3] == 'notfound' :
            return False
        # 현상에 다 몰린 경우
        if splt[0] != 'notfound' and splt[1] == 'notfound' and splt[2] == 'notfound' and splt[3] == 'notfound' :
            return False
        return True
    
    def find_best(x, candidates) :
        def countExists(splt) :
            count = 0
            for s in splt :
                if s == 'notfound' or s == 'empty' :
                    continue
                count += 1
            return count
        
        count = 0
        best = None
        for cand in candidates[::-1] : # should be reversed
            cut_cnt = countExists(cand)
            if count <= cut_cnt :
                count = cur_cnt
                best = cand
        x.extend(best)
        return x

    def get(self) :
        return {
            'success' : self._successes,
            'fail' : self._fails
        }

    def to_df(self) :
        df = pd.DataFrame(self._successes, columns = Config.CLASSIFIED_COLUMNS)
        return df

    