# Countries
from Devoir_utils import Utils
from Devoir_BCAO import CurrencyScrapper
from Devoir_BCAO import URL
from Devoir_utils import Utils
import requests
import pandas as pd



url = 'https://restcountries.com/v3.1/all'

class ApiFetcher(object):
    
    def httpFetcher(cls, url : str, params = None, headers = None):
        with requests.Session() as session : 
            res = session.get(url, params = params, headers= headers)
            return res.json()


    def countriesLister(cls, data):
        res = []
        for item in data:
            res.append(
                {
                    'name' : item['name']['official'],
                    'flag' : item['flags']['png']
                }
            )
        return res   


    @classmethod
    def addCountriesName(cls,  listCountries):
        print(Utils.divider())
        df1 = (CurrencyScrapper.main())
        df2 = CurrencyScrapper.makeCurrencyList(URL)
        newdf = Utils.contertToXOF(df1,df2)
        
        fetched = ApiFetcher.httpFetcher(cls, url)
        listCountries = ApiFetcher.countriesLister(cls, fetched)
        data = pd.DataFrame.from_dict(listCountries, orient='columns')
        dataCountries = data['name']
        
        newdf['country'] = ''
        newdf['country'] = newdf['country'].apply(lambda x: Utils.choiceRandomise(dataCountries))
        
        return newdf


    @classmethod
    def addCountriesFlag(cls, newdf, dataCountries):
        for i in range(len(dataCountries)):
            for j in range(len(newdf)):
                if newdf['country'][j] == dataCountries['name'][i]:
                    newdf['flag'] = dataCountries['flag'][i]
        return newdf


    @classmethod
    def main(cls):

        data = ApiFetcher.httpFetcher(cls, url)
        data = ApiFetcher.countriesLister(cls, data)
        data = ApiFetcher.addCountriesName(data)
        fetched = ApiFetcher.httpFetcher(cls, url)
        listCountries = ApiFetcher.countriesLister(cls, fetched)
        dataCountries = pd.DataFrame.from_dict(listCountries, orient='columns')
        dataframe = ApiFetcher.addCountriesFlag(data, dataCountries)
        return dataframe
