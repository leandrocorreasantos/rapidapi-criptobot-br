import requests
import json


class Client:
    def __init__(self, rapidapi_key):
        self.base_url = 'https://criptobot-br.p.rapidapi.com'
        self.headers = {
            'x-rapidapi-key': rapidapi_key
        }
        self.valid_timeframes = [
            '1m', '5m', '15m', '30m', '1h', '2h', '4h', '1d'
        ]
        self.exchange = None
        self.base = None
        self.quote = None
        self.symbol = None

    def validate_timeframe(self, timeframe):
        if timeframe not in self.valid_timeframes:
            return False

        return True

    def set_exchange(self, exchange):
        self.exchange = exchange

    def set_market(self, base, quote):
        self.base = base
        self.quote = quote
        self.symbol = '{}/{}'.format(self.base, self.quote)

    def _get(self, endpoint, params=None):
        url = '{}{}'.format(self.base_url, endpoint)
        result = {}
        try:
            result = requests.get(url, params=params, headers=self.headers)
        except Exception as e:
            raise e
        return json.loads(result.content)

    def get_strategies(self):
        endpoint = '/v1/strategy'
        return self._get(endpoint)

    def get_strategy(self, strategy):
        endpoint = '/v1/strategy/{}'.format(strategy)
        return self._get(endpoint)

    def get_strategy_parameters(self, strategy):
        endpoint = '/v1/strategy/{}/parameter'
        return self._get(endpoint)

    def get_markets(self):
        endpoint = '/v1/exchange/{}/markets'.format(self.exchange)
        return self._get(endpoint)

    def get_market_data(self):
        if self.symbol:
            endpoint = '/v1/exchange/{}/market/{}'.format(
                self.exchange, self.symbol
            )
            return self._get(endpoint)

        return {}

    def get_ticker(self):
        endpoint = '/v1/exchange/{}/pair/{}/ticker'.format(
            self.exchange, self.symbol
        )
        return self._get(endpoint)

    def get_candles(self, timeframe):
        if self.validate_timeframe(timeframe):
            endpoint = '/v1/exchange/{}/market/{}/timeframe/{}/candles'.format(
                self.exchange, self.symbol, timeframe
            )
            return self._get(endpoint)

        return {}

    def get_signal(self, strategy, parameters, timeframe):
        if self.validate_timeframe(timeframe):
            endpoint = '/v1/strategy/{}/signal'.format(strategy)
            queryparams = {
                'parameters': parameters,
                'exchange': self.exchange,
                'symbol': self.symbol,
                'timeframe': timeframe
            }
            return self._get(endpoint, queryparams)

        return {}
