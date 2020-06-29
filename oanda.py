import pandas as pd
from datetime import datetime
import oandapyV20
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.accounts as accounts
import oandapyV20.endpoints.orders as orders


class Oanda:
    def __init__(self, accountID, access_token):
        self.accountID = accountID
        self.access_token = access_token
        self.client = oandapyV20.API(access_token)

    def get_data(self, instrument, count, granularity):
        r = instruments.InstrumentsCandles(
            instrument, {"count": count, "granularity": granularity}
        )
        self.client.request(r)
        format_candle = lambda d: {
            "v": d["volume"],
            "t": datetime.strptime(d["time"][:-4], "%Y-%m-%dT%H:%M:%S.%f").timestamp(),
            **{key: float(val) for key, val in d["mid"].items()},
        }
        return list(map(format_candle, r.response["candles"]))

    def get_historic(self, instrument, count, granularity):
        d = self.get_data(instrument, count, granularity)
        return pd.DataFrame(d)

    def get_account(self):
        r = accounts.AccountDetails(self.accountID)
        self.client.request(r)
        return r.response

    def get_orders(self):
        account = self.get_account()
        return account["account"]["orders"]

    def buy(self, instrument, units):
        data = {"order": {"type": "MARKET", "units": units, "instrument": instrument}}
        r = orders.OrderCreate(self.accountID, data)
        self.client.request(r)
        return r.response
