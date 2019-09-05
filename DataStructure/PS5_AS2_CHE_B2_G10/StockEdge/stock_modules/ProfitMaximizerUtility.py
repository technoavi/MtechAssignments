class MoneyGainResult:
	moneyGain = 0
	bestBuyDay = 0
	bestSellDay = 0

	def __init__(self, moneyGain,bestBuyDay,bestSellDay):
		self.moneyGain = moneyGain
		self.bestBuyDay = bestBuyDay
		self.bestSellDay = bestSellDay

class ProfitMaximizerUtility:

	def getMaximumMoneyGain(self,stockPrice=[],start=0,end=0):
		if start  >= end:
			result = MoneyGainResult(0 , 0 , 0)
			return result
		else:
				mid = start + (end - start) / 2
				lconclusion = self.getMaximumMoneyGain(stockPrice,start,mid)
				rconclusion = self.getMaximumMoneyGain(stockPrice,mid+1,end)
				minLeftIndex = self.minimumDayNumber(stockPrice, start, mid)
				maxRightIndex = self.maximumDayNumber(stockPrice, mid, end)
				centerMoneyGain = stockPrice[maxRightIndex] - stockPrice[minLeftIndex]
				if centerMoneyGain > lconclusion.MoneyGain and centerMoneyGain > rconclusion.MoneyGain:
					tempResult = MoneyGainResult(centerMoneyGain,minLeftIndex,maxRightIndex)
					return tempResult
				elif lconclusion.MoneyGain > centerMoneyGain and rconclusion.MoneyGain > centerMoneyGain:
					return lconclusion
				else:
					rconclusion

	def minimumDayNumber(self,stockPrice , index1, index2):
		minimum = index1
		for k in range(index1+1, index2+1):
			if stockPrice[k] < stockPrice[minimum]:
				minimum = k
		return minimum

	def maximumDayNumber(self,stockPrice , index1 , index2):
		maximum = index1
		for k in range(index1+1, index2+1):
			if stockPrice[k] > stockPrice[maximum]:
				maximum = k
		return maximum



