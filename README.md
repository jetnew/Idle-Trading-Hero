# Idle Trading Hero

An Artemis-level project for Orbital, CP2106: Independent Software Development Project at NUS School of Computing.

![poster](assets/poster.jpg)

# Project Motivation

Algorithmic trading (or automated trading) uses trading algorithms to place trades, generating profits at a speed and frequency impossible for a human trader. Idle Trading Hero serves as a trading platform for traders to jumpstart deployment of automated trading strategies, coupled with an analytics dashboard for profit visualisation. We hope that through this project, we learn more about quantitative finance while gaining side income in the process.

# Core Features

## 1. User Login System

Traders can register and login to manage personal accounts and trading strategies.

![login](assets/login_register.png)

## 2. Algorithm Selection Panel

The panel allows traders to select: 1. Assets, 2. Strategies, 3. Parameters, along with backtesting performance indications so that traders can make the optimal automated trading decisions.

![panel](assets/algo_selection_panel.png)

* Available Assets

  * AAPL: Apple Inc.
  * GOOGL: Alphabet Inc Class A
  * SPY: SPDR S&P 500 ETF Trust
  * VOO: VANGUARD IX FUN/S&P 500 ETF SHS NEW
  * To be added

* Available Strategies

  * MACD: Moving Average Convergence/Divergence
  * MFI: Money Flow Index
  * RSI: Relative Strength Index
  * To be added

* Available Parameters

  * Duration
  * Exit Condition
  * Capital
  * Algorithm-Specific Parameters

## 3. Analytics Visualisation Dashboard

The dashboard allows traders to visualise real-time performance analytics, ranging from total returns to Sharpe and Sortino ratios to gain insights about the automated trading algorithm.

## 4. Live Deployment

Live deployment is coupled with live notifications whenever the algorithm performs a buy/sell action or exit trigger, to the comfort of the trader's Telegram or email.
