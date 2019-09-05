from stock_modules import ProfitMaximizerUtility
from stock_modules import NonRecursive

class StockHelper:
    def doTask(self):
        nr = NonRecursive()
        output = nr.doOperation()
        self.writeOutPutForNR(output)

    #This function will write output to file using Non-Recursive Approach
    def writeOutPutForNR(self,MoneyGainResult):
        f= open("outputPS5.txt","w+")
        f.write("Maximum Profit(Iterative Solution): " + str(MoneyGainResult.moneyGain)+"\n")
        f.write("Day to buy: "+str(MoneyGainResult.bestBuyDay)+"\n")
        f.write("Day to sell: " +  str(MoneyGainResult.bestSellDay)+"\n")
        f.close()
        self.writeOutPutForDAQ(MoneyGainResult)

    #This function will write output to file using Divide and Conquer Approach
    def writeOutPutForDAQ(self,MoneyGainResult):
        f= open("outputPS5.txt","a+")
        f.write("Maximum Profit(Divide & Conquer): " + str(MoneyGainResult.moneyGain)+"\n")
        f.write("Day to buy: "+str(MoneyGainResult.bestBuyDay)+"\n")
        f.write("Day to sell: " +  str(MoneyGainResult.bestSellDay)+"\n")
    
stockHelper = StockHelper()
stockHelper.doTask()








