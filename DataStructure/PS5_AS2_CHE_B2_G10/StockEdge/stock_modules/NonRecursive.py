from stock_modules.ProfitMaximizerUtility import  MoneyGainResult

class NonRecursive:
    def get_data(self,line):
        key, sep, value = line.strip().partition("/")
        return int(key), value
    def doOperation(self):
        with open("inputPS5.txt") as fd:
            d = dict(self.get_data(line) for line in fd)
            min=int(d[1])
            max=0
            minKey=0
            maxKey=0
            for key in d:
                if min> int(d[key]):
                    min=int(d[key])
                    minKey = key
                    maxKey = key
                    max=min
                if max< int(d[key]):
                    max= int(d[key])
                    maxKey = key

        profit=max-min;
        resultObject = MoneyGainResult(profit,minKey,maxKey)

        return resultObject
