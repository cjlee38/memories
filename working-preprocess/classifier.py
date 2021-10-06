import sys
import pandas as pd

from abc import *
from config import Config
from vo import ClassifiedVO
from enums import Status

class AbstractClassifier(ABC) :

    @abstractmethod
    def classify(self) :
        pass

class LangClassifier(AbstractClassifier) :

    def __init__(self, patterns) :
        self.classes = {}
        self.validate_patterns(patterns)
        self._patterns = patterns
    
    def validate_patterns(self, patterns) :
        if 'kor' not in patterns.keys() :
            raise Exception("korean must exists")
        if 'etc' not in patterns.keys() :
            raise Exception("etc must exists")
        
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

class FrameClassifier(AbstractClassifier) :
    pass

class SplitClassifier(FrameClassifier) :

    def __init__(self, pattern) :
        self._pattern = pattern

    def classify(self, descriptions) :
        if isinstance(descriptions, str) :
            return self._classify(descriptions)

        successes = []
        fails = []
        for desc in descriptions :
            flag, splt = self._classify(desc)
            to_save = successes if flag else fails
            to_save.append([desc, *splt])
        return ClassifiedVO(Status.OK, {"success", successes, 'fail' : fails})
    
    def _classify(self, desc) :
        splt = [i for i in self._pattern.split(desc) if i != '']
        splt = splt[:1] + splt[2:] # drop '[C]' column
        return (self.is_success(splt), splt)

    def is_success(self, splt) :
        if len(splt) == 4 :
            return True
        return False

class SearchClassifier(FrameClassifier) :

    def __init__(self, rgroup) :
        self._rgroup = rgroup
    
    def classify(self, descriptions) :
        if isinstance(descriptions, str) :
            return self._classify(descriptions)
        
        successes = []
        fails = []
        for desc in descriptions :
            try :
                splt = self._classify(desc)
                successes.append(splt)
            except Exception as e :
                print(e) # todo : to logger except for printing
                fails.append(desc)
        return ClassifiedVO(Status.OK, {"success" : successes, "fail " fails})

    def _classify(self, desc) :
        x = [desc]
        candidates = []
        for regex in self._rgroup.get() :
             # ex) {'A' : <pattern>, 'B' : <pattern>}
            splt = [self.parse(p, desc) for n, p in regex.items()]
            if self.isOK(desc, splt) :
                x.extend(splt)
                return x
            candidates.append(splt)
        return self.find_best(x, candidates)
            
    def parse(self, p, desc) :
        r = p.search(desc)
        text = None
        if r :
            buf = r.group('text')
            text = buf if buf else 'empty'
        else :
            text = 'notfound'
        return text.strip()
    
    def isOK(self, desc, splt) :
        # '현상' 이 없는 경우
        if splt[0] == 'notfound' and '현상' in desc :
            return False
        # all not found
        if splt[0] == 'notfound' and splt[1] == 'notfound' and splt[2] == 'notfound' and splt[3] == 'notfound' :
            return False
        # 현상에 다 몰린 경우
        if splt[0] != 'notfound' and splt[1] == 'notfound' and splt[2] == 'notfound' and splt[3] == 'notfound' :
            return False
        return True
    
    def find_best(self, x, candidates) :
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
            cur_cnt = countExists(cand)
            if count <= cur_cnt :
                count = cur_cnt
                best = cand
        x.extend(best)
        return x
