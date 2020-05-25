class Strategy(object):
    def acceptCandle(self, candle):
        raise NotImplementedError

    def currentState(self):
        raise NotImplementedError