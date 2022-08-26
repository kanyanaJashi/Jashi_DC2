# Devoir_BCAO.py

from Devoir_utils import Utils
from Devoir_csv import CsvFactory
from Devoir_json import JsonFactory
from Devoir_Html import HtmlFactory
import pandas as pd
import requests
from bs4 import BeautifulSoup

PATH_URL = 'cours/cours-des-devises-contre-Franc-CFA-appliquer-aux-transferts'
URL = "https://www.bceao.int/fr/{}".format(PATH_URL)


class DataSouper(object):
    @classmethod
    def httpFetcher(cls, URL):
        with requests.Session() as session:
            result = session.get(URL)
            result = result.text
            return result

class CurrencyScrapper(object):
    @classmethod
    def scrapLink(cls, URL):
        gosub1=DataSouper.httpFetcher(URL)
        return gosub1

    @classmethod
    def souper(cls, URL):
        result = cls.scrapLink(URL)
        gosub2=BeautifulSoup(result,'html.parser')
        return gosub2

    @classmethod
    def getBoxCourse(cls, URL):
        soupering = cls.souper(URL)
        # print(soupering) # Activate for verification
        soupering = soupering.find_all(attrs={'id': 'box_cours'})
        if soupering:
            table = soupering[0].table
            return table
        return None

    @classmethod
    def makeCurrencyList(cls, URL):
        soupering = cls.getBoxCourse(URL)

        if soupering:
            tr_block = soupering.find_all('tr')
            factory = [item.find_all('td')for item in tr_block][1:]
            factory = [
                {
                    'Devise': x.string.strip(),
                    'Achat': float(y.string.strip().replace(',', '.')),
                    'Vente': float(z.string.strip().replace(',', '.')),
                }
                for (x, y, z) in factory
            ]
            factory = pd.DataFrame.from_dict(factory, orient='columns')

            return factory
        return None


    @classmethod
    def save(cls, URL, format=None):
        soupering = cls.makeCurrencyList(URL)
        if soupering:
            return soupering
        return None

    @classmethod
    def addDevise(cls, data):

        dataCsv = CsvFactory.main()
        dataJson = JsonFactory.main()
        dataHtml = HtmlFactory.main()
        globData =  dataCsv + dataJson + dataHtml
        data = pd.DataFrame.from_dict(globData, orient='columns')
        #data.insert(2, "XOF", [], True) ##
        devList = ["Euro", "Dollar_CAN", "Yen japonais"]
        data['devise'] = ''
        data['devise'] = data['devise'].apply(lambda x: Utils.choiceRandomise(devList))
        return data

    @classmethod
    def main(cls):
        data = CurrencyScrapper.makeCurrencyList(URL)
        data = CurrencyScrapper.addDevise(data)
        return data

if __name__=="__main__":

    data_final=CurrencyScrapper.main()
    print(data_final)