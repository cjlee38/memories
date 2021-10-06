import re

class RegexGroup() :

    x = r"(?P<text>.*?)" # target

    def __init__(self) :
        self._rgroup = []
    
    def get(self) :
        return self._rgroup

    def add(self, partition) :
        if not isinstance(partition, dict) :
            raise Exception("partition should be dict")

        self._rgroup.append(self.grouping(partition))
        return self
        
    def grouping(self, partition) :
        r = partition
        keys = list(r.keys()) # 현상 원인 조치 요망
        dct = dict()

        for i in range(len(keys)) :
            dct[r[keys[i]]] = re.compile(
                r[keys[i]] + \
                RegexGroup.x + \ 
                self.ending(*[r[keys[j]] for j in range(i + 1, len(keys))])
            )
                            
                            
        return dct

    def ending(self, *args) :
        return "(" + "|".join(list(args)) + "{}$)".format("|" if len(args) > 0 else "")
    