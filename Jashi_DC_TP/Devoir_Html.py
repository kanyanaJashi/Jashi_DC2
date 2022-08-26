from Devoir_utils import Utils
import json
import bs4
from bs4 import BeautifulSoup


BASE_URL = 'data-zIybdmYZoV4QSwgZkFtaB.html'


class HtmlFactory(object):
    @classmethod
    def openFile(cls):
        with open(BASE_URL) as file:
            data = file.read()
            data = BeautifulSoup(
                data,
                'html.parser')
            file.close()
        return data
    
    @classmethod
    def fetchData(cls, data):
        data1 = []
        trs_blocks = data.find_all('tr')
        for items in trs_blocks[1::]:
            tds_blocks = items.find_all('td')
            # print(tds_blocks) # activate here for verification
            data1.append(
                {
                    'name' : tds_blocks[0].text,
                    'phone' : tds_blocks[1].text,
                    'email' : tds_blocks[2].text,
                    'latlon' : tds_blocks[3].text,
                    'salary' : tds_blocks[4].text,
                    'age' : tds_blocks[5].text
                }
            )
        # else: # activate here for verification
            # print(data1) # activate here for verification
        return data1

    @classmethod
    def naming(cls, data):
        def name(x):
            x['name'] = x['name'].split(' ')
            last_name = x['name'][1].upper()
            first_name = x['name'][0].capitalize()
            x['name'] = ' '.join([first_name, last_name])
            return x
        data = map(name, data)
        return list(data)
    
    @classmethod
    def main(cls):
        data = cls.openFile()
        data = cls.fetchData(data)
        data = cls.naming(data)
        return(data)

if __name__=="__main__":
    fetched_data=HtmlFactory.main()
    print(fetched_data)
    print(type(fetched_data)) # to confirm that fetched_data is a list