# Idle Trading Hero

![banner](https://user-images.githubusercontent.com/27071473/83358983-bc2ba980-a3a9-11ea-80eb-f4467c001de6.png)

# Project Description

Idle Trading Hero is a trading platform to jumpstart [automated trading](https://en.wikipedia.org/wiki/Algorithmic_trading) strategies, coupled with an analytics dashboard for profit visualisation. Idle Trading Hero offers a collection of strategies that traders can employ to perform live algorithmic trading on the chosen market, with control over algorithm parameters. The platform includes a data visualisation dashboard for indicator performance analytics, finished with an optional extension of action and notification tracking from the comfort of the trader's Telegram bot and email.

# Project Motivation

Many potential traders seek profitable passive trading, using easily understandable trading algorithms, yet with control over how the algorithms make use of the trader's capital. Idle Trading Hero stems from 3 core needs: Profitability, Accessibility and Control.  Idle Trading Hero therefore aims to resolve this 3-way dilemma that many existing platforms do not offer. Many are interested in exploring [passive income](https://en.wikipedia.org/wiki/Passive_income) options or [investment](https://en.wikipedia.org/wiki/Investment) options, and some are interested in exploring the field of [quantitative finance](https://en.wikipedia.org/wiki/Quantitative_analysis_(finance)). Jet is of the former and Ian is of the latter.

# Project Poster

<p align="center">
    <img src="https://user-images.githubusercontent.com/27071473/83369156-f3bc4500-a3ed-11ea-9a52-14aac952e08a.png" alt="drawing" width="50%"/>
</p>

# Project Ideation

| Questions                                   | Answers                                                                                                                                                                                                                                  |
|---------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Who is the target audience?              | Idle Trading Hero aims to target the market of potential algorithmic traders gate-kept by existing inaccessible trading platforms. The platform allows a whole youth-heavy generation of potential traders to begin algorithmic trading. |
| 2. What is the problem statement?           | Idle Trading Hero therefore tackles the problem statement: How can potential algorithmic traders gate-kept by existing inaccessible trading platforms begin their journey in algorithmic trading?                                        |
| 3. How does the solution solve the problem? | Idle Trading Hero resolves the 3-way dilemma among 1. Profitability, 2. Accessibility and 3. Control. With the Idle Trading Hero platform, traders can jumpstart automated trading strategies easily.                                    |

# Feature Deliverables for Milestone 1 (1 June 2020)

## 1. Login-Registration System

![login_register](https://user-images.githubusercontent.com/27071473/83352989-06993000-a382-11ea-9e1a-178013ee8721.PNG)

The login-registration system refers to the authentication system for individual traders to manage personal accounts, capital and algorithms. The system is implemented in Golang.

| Questions                                      | Answers                                                                                                                                                                           |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Who is the user role (public/member/admin)? | The login-registration system is used by the public (registration, login) and members (login) to create and manage personal accounts.                                             |
| 2. What is the desired outcome (user goal)?    | The system enables registration of new traders and the logging in of existing traders to the Idle Trading Hero platform, inclusive of a password-encrypted authentication system. |
| 3. What is the benefit?                        | The system allows secure and dedicated management of traders' personal accounts, which includes their capital and algorithms.                                                     |

## 2. Technical Analysis (TA) Indicators
   
Technical analysis indicators refer to the implementation of basic trading indicators for technical analysis, including the MACD (Moving Average Convergence Divergence), MFI (Money Flow Index) and RSI (Relative Strength Index). The TA indicators are implemented with  object-oriented (OO) interface in Python, using [Pandas](https://pandas.pydata.org/) and [TA](https://github.com/bukosabino/ta), indicator data visualisations plotted using [Matplotlib](https://matplotlib.org/), and interface endpoint exposed using [gRPC](https://grpc.io/). A tutorial is included for the usage of the TA indicators.
   
| Questions                                      | Answers                                                                                                                                                                                                                                                     |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Who is the user role (public/member/admin)? | The TA indicators are intended to be used by the admin, to be hosted through a server for the web backend to request for indicator computations and strategy buy/sell actions.                                                                              |
| 2. What is the desired outcome (user goal)?    | The TA indicators, after thorough design consideration, are implemented using DataFrame column-wise operations for each indicator. The indicators append new incoming data to the existing timeseries DataFrames to reduce unnecessary repeated operations. |
| 3. What is the benefit?                        | The TA indicators serve the project's 3 core needs by offering a set of baseline-performant (profitability) trading algorithms, which are beginner-friendly (accessiblity) and whose parameters are adjustable to maximise expected returns (control).      |

## 3. Algorithm Selection Panel

![algo_selection_panel](https://user-images.githubusercontent.com/27071473/83352990-0862f380-a382-11ea-98bd-9063326ed919.PNG)

The algorithm selection panel refers to the hosted web page that allows traders to select: 1. Assets, 2. Strategies, 3. Parameters, along with backtesting performance for traders to deploy the optimal trading algorithm. The web backend is implemented in Golang and developed using [Docker](https://www.docker.com/), and uses [gRPC](https://grpc.io/) to request data from the indicator server.

| Available Assets                         | Available Strategies                        | Available Parameters |
|------------------------------------------|---------------------------------------------|----------------------|
| AAPL: Apple Inc.                         | MACD: Moving Average Convergence/Divergence | Duration             |
| GOOGL: Alphabet Inc Class A              | MFI: Money Flow Index                       | Exit Condition       |
| SPY: SPDR S&P 500 ETF Trust              | RSI: Relative Strength Index                | Capital              |
| VOO: VANGUARD IX FUN/S&P 500 ETF SHS NEW |                                             | Algorithm Parameters |

| Questions                                      | Answers                                                                                                                                                                                                                                                              |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Who is the user role (public/member/admin)? | The algorithm selection panel is accessible to the public upon creation of an account on the Idle Trading Hero platform, to be used during algorithm creation pre-deployment.                                                                                        |
| 2. What is the desired outcome (user goal)?    | The panel enables the selection of asset, algorithm and parameters in a single display. The visualisation of indicators and performance metrics of each combination of asset-algorithm-parameters allows traders to develop an intuitive expectation of the returns. |
| 3. What is the benefit?                        | The panel serves the project's 3 core needs by offering a display of performance metrics (profitability), data visualisation of indicators (accessibility) and backtesting using parameter-tuning (control).                                                         |

## 4. Algorithm Backtesting Engine

The algorithm backtesting engine refers to the implementation of an engine to simulate algorithm performance based on historical data, while tuning algorithm parameters to maximise expected returns. The engine is implemented using [TA](https://github.com/bukosabino/ta) with the API endpoint exposed using [gRPC](https://grpc.io/).

| Questions                                      | Answers                                                                                                                                                                                                                                   |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Who is the user role (public/member/admin)? | The algorithm backtesting engine is accessible to the public through the algorithm selection panel, while the API endpoint is accessible to the admin for maintenance.                                                                    |
| 2. What is the desired outcome (user goal)?    | The engine facilitates the visualisation of expected performance given a particular combination of asset-algorithm-parameters.                                                                                                            |
| 3. What is the benefit?                        | The engine serves the project's core needs by providing an expected performance on historical data (profitability), visualisation of performance (accessibility) and an indicator for the result of algorithm parameter-tuning (control). |

# Feature Deliverables for Milestone 2

## 1. Fundamental Analysis (FA) Indicators

Fundamental analysis indicators refer to the implementation of methods to determine an asset's intrinsic value by examining related economic and financial factors. FA indicators are like technical analysis indicators, except that fundamental analysis does not make use of solely historical data.

| Questions                                      | Answers                                                                                                                                                                                            |
|------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Who is the user role (public/member/admin)? | The FA indicators are intended to be used by the admin, to be hosted through a server for the web backend to request for indicator computations and strategy buy/sell actions.                     |
| 2. What is the desired outcome (user goal)?    | The FA indicators provide external data, such as market sentiment or company financial information as an alternative to technical indicators.                                                      |
| 3. What is the benefit?                        | The FA indicators serve to provide the trader with additional trading options aside from technical indicators, allowing the trader to diversify risk and maximise returns.                         |
| 4. What is the feature specifications?         | The FA indicators, like TA indicators, are implemented in an OO-interface exposed using [gRPC](https://grpc.io/). The FA indicators should have performance metrics, including data visualisation. |

## 2. Market Data Supplier

The market data supplier serves to supply market data from the data source, such as Finnhub API. The supplier passes data into a message queue prior to supplying the data.

| Questions                                      | Answers                                                                                                            |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------|
| 1. Who is the user role (public/member/admin)? | The supplier is handled by the admin for creating/deleting new data sources.                                       |
| 2. What is the desired outcome (user goal)?    | The supplier provides data from the data source by running scheduled jobs before supplying into the message queue. |
| 3. What is the benefit?                        | The supplier distributes the computational load evenly between the services in the architecture.                   |
| 4. What is the feature specifications?         | The supplier calls the data source API periodically / listen on a stream and sends data to the message queue.      |

## 3. Algorithm Server

The algorithm server aims to compartmentalise the computation of algorithms to a separate server. The server uses a protocol to receive and supply relevant algorithm data.

| Questions                                      | Answers                                                                                                                                                                                                                     |
|------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1. Who is the user role (public/member/admin)? | The server is handled by the admin for creating/deleting new strategies.                                                                                                                                              |
| 2. What is the desired outcome (user goal)?    | The server performs strategy computations before returning the buy/sell action, as well as provides performance measurements when requested.                                                                          |
| 3. What is the benefit?                        | The server distributes the computational load evenly between the services in the architecture.                                                                                                                        |
| 4. What is the feature specifications?         | The server is called whenever messages from the market data supplier message queue is passed. The server performs required strategy computations, then returns the buy/sell action to the relevant destination. |

# Project Log

| S/N | Date      | Hours | Task                                                                           | Remarks                                                                                                               | Completed by |
|-----|-----------|-------|--------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------|--------------|
| 1   | 9/5/2020  | 3     | Literature Review: Finance                                                     | Read up finance concepts.                                                                                             | Jet New      |
| 2   | 9/5/2020  | 8     | Literature Review: Technical Analysis                                          | Read up on technical analysis concepts.                                                                               | Jet New      |
| 3   | 10/5/2020 | 5     | Literature Review: Trading Service Platforms (Oanda, Quantopian)               | Read up on Oanda and Quantopian, sign up and used APIs to obtain historical data.                                     | Jet New      |
| 4   | 10/5/2020 | 6     | Experimental Analysis: LSTM Forecasting on AUD_USD                             | Experiment on machine learning using Long Short-Term Memory networks for forecasting AUD_USD data for 10K timestamps. | Jet New      |
| 5   | 16/5/2020 | 6     | Literature Review: Trading Algorithms                                          | Read up on trading algorithms in general.                                                                             | Jet New      |
| 6   | 16/5/2020 | 4     | Implementation: MACD Indicator                                                 | Implemented MACD indicator in Python and exponential moving average with window size of 26, 12 and 9.                 | Jet New      |
| 7   | 16/5/2020 | 4     | Implementation: MACD Strategy                                                  | Implemented MACD strategy using Pandas DataFrames column operations, and mapping of indicator to buy/sell action.     | Jet New      |
| 8   | 16/5/2020 | 3     | Implementation: MACD Visualisation                                             | Implemented MACD visualisation of indicators using Matplotlib.                                                        | Jet New      |
| 9   | 17/5/2020 | 8     | Literature Review: Technical Analysis                                          | Read up further on technical analysis and compile list of trading algorithms for potential implementation.            | Jet New      |
| 10  | 23/5/2020 | 6     | Implementation: Algorithm and Strategy Interface                               | Design Object-Oriented interface of algorithms and each strategy for standardised usage.                              | Jet New      |
| 11  | 23/5/2020 | 5     | Implementation: MACD, MFI, RSI Indicators, Strategies and Visualisation        | Implemented MACD, MFI, RSI strategies using TA library and OO interface.                                              | Jet New      |
| 12  | 23/5/2020 | 3     | Implementation: Performance Metrics                                            | Implemented returns, alpha, beta, sharpe ratio and sortino ratio.                                                     | Jet New      |
| 13  | 24/5/2020 | 2     | Documentation: Algorithm and Strategy Interface                                | Documented the OO interface for algorithms and strategies.                                                            | Jet New      |
| 14  | 30/5/2020 | 4     | Literature Review: Protocol Buffer                                             | Read up documentation on gRPC for Protocol Buffer and server-client communication.                                    | Jet New      |
| 15  | 30/5/2020 | 4     | Implementation: Strategy Server                                                | Implemented gRPC Python server for algorithms and strategies and sample client for testing.                           | Jet New      |
| 16  | 30/5/2020 | 2     | Implementation: Indicator, Strategy and Parameter Selection on Strategy Server | Implemented functionality to customise indicator, strategy and parameters for all algorithms on the gRPC server.      | Jet New      |
| 17  | 31/5/2020 | 4     | Installation: Web Backend Server, Docker, Postman                              | Set up Go backend server, requiring setting up of Docker and Postman, and tested functionality of backend server      | Jet New      |
| 18  | 31/5/2020 | 8     | Documentation: Milestone 1                                                     | Write up Milestone README                                                                                             | Jet New      |
|     | 22 Days   | 85    |                                                                                |                                                                                                                       |              |