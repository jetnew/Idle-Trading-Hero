import oandapyV20
import oandapyV20.endpoints.instruments as instruments
import oandapyV20.endpoints.accounts as accounts

class Oanda:
    def __init__(self, accountID, access_token):
        self.accountID = accountID
        self.access_token = access_token
        self.client = oandapyV20.API(access_token)

    def get_data(self, instrument, count, granularity):
        r = instruments.InstrumentsCandles(instrument, {'count': count, 'granularity': granularity})
        self.client.request(r)
        return r.response
    
    def get_account(self):
        r = accounts.AccountDetails(self.accountID)
        self.client.request(r)
        return r.response
    
    def get_orders(self):
        account = self.get_account()
        return account['account']['orders']
    
    def buy(self, instrument, units):
        data = {'order': {
                'units': 100,
                'instrument': instrument,
                'type': 'MARKET',
                'positionFILL': 'DEFAULT'}}
        r = orders.OrderCreate(self.accountID, data)
        self.client.request(r)
        return r.response