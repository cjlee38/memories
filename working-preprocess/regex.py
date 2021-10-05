import re

class RegexGroup() :

    x = r"(?P<text>.*?)" # target

    def __init__(self) :
        self._rgroup = []
    
    def add(self, partition) :
        if not isinstance(partition, dict) :
            raise "partition should be dict with 4 keys(a, b, c, d)"
            
        for i in ['a', 'b', 'c', 'd'] :
            if i not in partition.keys() :
                raise "there is no {} key in your partition".format(i)
        self._rgroup.append(self.grouping(partition))
        
    def grouping(self, partition) :
        r = partition
        return {
            'A' : re.compile(r['a'] + RegexGroup.x + self.ending(r['b'], r['c'], r['d'])),
            'B' : re.compile(r['b'] + RegexGroup.x + self.ending(r['c'], r['d'])),
            'C' : re.compile(r['c'] + RegexGroup.x + self.ending(r['d'])),
            'D' : re.compile(r['d'] + RegexGroup.x + self.ending())
        }

    def ending(self, *args) :
        return "(" + "|".join(list(args)) + "{}$)".format("|" if len(args) > 0 else "")
    