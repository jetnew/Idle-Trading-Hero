# Idle Trading Hero

![banner](https://user-images.githubusercontent.com/27071473/83358983-bc2ba980-a3a9-11ea-80eb-f4467c001de6.png)

# About Idle Trading Hero

In one sentence, Idle Trading Hero is a trading platform to jumpstart automated trading strategies, coupled with an analytics dashboard for profit visualisation. Idle Trading Hero offers a suite of strategies that traders can employ to perform live algorithmic trading on the chosen market, with control over algorithm parameters.

# Why Idle Trading Hero?

Many potential traders seek profitable passive trading, using easily understandable trading algorithms, yet with control over how the algorithms make use of the trader's capital. Idle Trading Hero stems from 3 core needs: Profitability, Accessibility and Control. Idle Trading Hero therefore aims to resolve this 3-way dilemma that many existing platforms do not offer.

# Core Features

* Login-Registration System
* Strategy Live Deployment
* Performance Evaluation & Notification

## 1. Login-Registration System

The Login-Registration System is essential to ensure secure and private management of financial capital. The system is user-facing and users register for an account before logging in to the platform. + Security Testing

### Backend

/diagram

### Security

The system encrypts passwords using a secure hash to store in the database, and locks the account upon 3 login attempts.

## 2. Live Strategy Deployment

The Live Strategy Deployment allows the user deploy strategies live via a Graphical User Interface (GUI) through the Oanda v20 API. Users can select from a suite of algorithms and select specific parameters for those algorithms.

### About Oanda

Oanda v20 is an API that provides programmatic access to Oanda's trading engine. Using Oanda, trades can be automatically performed using trading algorithms. To read more about Oanda, click [here](https://developer.oanda.com/rest-live-v20/introduction/).

### Algorithm Explanation

Trading algorithms are programs that, given the current conditions of the market, outputs an action (e.g. buy/sell/do nothing), with the goal of maximising profits. *Indicators* refer to the data that is input into the algorithm, and the *Strategy* refers to the function that maps input data to output action. Trading algorithms are implemented using [ta](https://technical-analysis-library-in-python.readthedocs.io/en/latest/ta.html) (Technical Analysis Library in Python).

Available Strategies:

* Moving Average Convergence Divergence (MACD)
* Relative Strength Index
* Money Flow Index

Moving Average Convergence Divergence (MACD)

* About
  * The Exponential Moving Average ([EMA](https://www.investopedia.com/terms/e/ema.asp)) is computed by taking the exponentially-weighted average of the past n days of the variable.

* Detail
  * The MACD strategy consists of multiple indicators: The MACD line consists of the 12-day EMA subtracting the 26-day EMA. The Signal line is computed as the 9-day EMA of the MACD line. The MACD histogram is computed by the MACD line subtracted by the Signal line.
  * When the MACD histogram is positive, it means that upside momentum is increasing, and when negative, downside momentum is increasing.
  * When the MACD histogram crosses over from positive to negative, it triggers a sell action, and when negative to positive, it triggers a buy action.

Relative Strength Index

* About
  * The Relative Strength Index ([RSI](https://www.investopedia.com/terms/r/rsi.asp)) is a momentum indicator that measures the magnitude of recent price changes to evaluate overbought or oversold conditions in the price of the instrument.

* Detail
  * The RSI strategy indicates whether an asset is considered overbought or oversold.
  * RSI is computed by the following formula:

    ![image](https://user-images.githubusercontent.com/27071473/87248568-aae7b980-c48c-11ea-8e91-831ff9c1ff6d.png)

  * RSI ranges from 0 to 100. When RSI is lower than 30, it indicates an oversold or undervalued condition.
  * When RSI is higher than 70, it indicates an overbought or overvalued condition, and may be primed for a reversal or pullback in price.

Money Flow Index (MFI)

* About
  * The Money Flow Index ([MFI](https://school.stockcharts.com/doku.php?id=technical_indicators:money_flow_index_mfi)) is an oscillator that uses both price and volume to measure buying and selling pressure.

* Detail
  * The MFI is usually computed on a 14-day period.
  * Typical Price = (High + Low + Close) / 3
  * Raw Money Flow = Typical Price * Volume
  * Money Flow Ratio = (14-period Positive Money Flow) / (14-period Negative Money Flow)
  * Money Flow Index = 100 - 100/(1+Money Flow Ratio)

### Algorithm Parameter Selection

Algorithm Parameter Selection is a dashboard that allows the trader to easily configure and customise the trading strategy to the 

## 3. Performance Evaluation & Notification

Performance Evaluation & Notification allows the user to visualise earnings and losses across time at a glance using visualisation plots. Users receive a notification whenever the deployed algorithm performs an action.

### 