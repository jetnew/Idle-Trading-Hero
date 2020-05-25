from strategies import *
import json
import time

with open('AUD_USD-1588780800-H6-10000.json') as audUsd:
    candles = json.load(audUsd)
    

first100 = candles[:100]
rest = candles[100:]

# a = MACDStrategy(10000, first100)

# s1 = time.perf_counter()
# for i in range(100):
#     a.acceptCandle(rest.pop(0))
# e1 = time.perf_counter()

# s2 = time.perf_counter()
# for i in range(100):
#     a.acceptCandle(rest.pop(0))
# e2 = time.perf_counter()

# print(e1-s1, e2-s2)

# a.sell()
# print(a.capital, a.holdings)

# rsis = RSIStrategy(10000, first100)

# rsisps = time.perf_counter_ns()
# for i in range(9900):
#     rsis.acceptCandle(rest.pop(0))
# rsispe = time.perf_counter_ns()

# rsis.sell()
# print(rsis.currentState(), rsispe - rsisps)

macd_rsis = MACD_RSIStrategy(10000, first100)

macd_rsis_ps = time.perf_counter_ns()
for i in range(9900):
    macd_rsis.acceptCandle(rest.pop(0))
macd_rsis_pe = time.perf_counter_ns()

print(macd_rsis.currentState(), macd_rsis_pe - macd_rsis_ps)
macd_rsis.sell()
print(macd_rsis.currentState())