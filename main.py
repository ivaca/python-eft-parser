from apscheduler.schedulers.blocking import BlockingScheduler
import json
import requests, random
import time
from datetime import datetime
import os

#time.sleep(5)


def parseItems():
    proxies = {
        'http': '88.198.50.103:3128',

    }

    # response = requests.get("https://tarkov-market.com/api/items?lang=en&search=&tag=&sort=avgDayPrice&sort_direction=desc&skip=0&limit=20",  headers={"Cookie":"__cfduid=dc416ccf6dc52a9824333196319a0f25d1592079845; _ga=GA1.2.1197220046.1592079847; _ym_d=1592079847; _ym_uid=1592079847807987920; _gid=GA1.2.1885108695.1593162633; uid=6bcbe408-771b-43c2-9cee-84e504bd0c6a; _ym_isad=1; _ym_visorc_56354407=w; token=VmH73MU8-gjjQhVyJajvyT3X88LKLuhJcZsk"},proxies=proxies)

    # json_data = json.loads(response.text)['items']
    json_data = json.loads("[]")
    ID = 1
    # 149

    for i in range(0, 107):
        response = requests.get(
            f'https://tarkov-market.com/api/items?lang=en&search=&tag=&sort=avgDayPrice&sort_direction=desc&skip={i * 20}&limit=20',
            #headers={
             #   "Cookie":
              #      "__cfduid=dc416ccf6dc52a9824333196319a0f25d1592079845; _ga=GA1.2.1197220046.1592079847; _ym_d=1592079847; _ym_uid=1592079847807987920; _gid=GA1.2.1885108695.1593162633; uid=6bcbe408-771b-43c2-9cee-84e504bd0c6a; _ym_isad=1; _ym_visorc_56354407=w; token=VmH73MU8-gjjQhVyJajvyT3X88LKLuhJcZsk"},
            proxies=proxies)

        for n in range(0, len(json.loads(response.text)['items'])):
            item = json.loads(response.text)['items'][n]
            try:
                item['id'] = item.pop('_id')
                item['id'] = str(ID)
            except:
                print()

            item.pop('uid', None)
            item.pop('tags', None)
            item.pop('url', None)
            item.pop('enImg', None)
            item.pop('enName', None)
            item.pop('change24', None)
            item.pop('change7d', None)
            item.pop('updated', None)
            item.pop('avgDayPrice', None)
            item.pop('avgWeekPrice', None)
            item.pop('priceUpdated', None)
            item.pop('shortName', None)
            item.pop('ruImg', None)
            item.pop('ruName', None)
            item.pop('cnName', None)
            item.pop('cnShortName', None)
            item.pop('ruShortName', None)
            item.pop('deName', None)
            item.pop('deShortName', None)
            item.pop('frName', None)
            item.pop('frShortName', None)
            item.pop('esName', None)
            item.pop('esShortName', None)
            item.pop('pricePerSlot', None)
            item.pop('avgDayPricePerSlot', None)
            item.pop('avgWeekPricePerSlot', None)

            if 100000 > item['price'] > 50000:
                if random.randint(1, 5) > 3:
                    item['price'] += random.randint(1000, 3000)
                else:
                    item['price'] -= random.randint(1000, 7000)

            elif 20000000 > item['price'] > 100000:
                if random.randint(1, 5) > 3:
                    item['price'] += random.randint(1000, 15000)
                else:
                    item['price'] -= random.randint(3000, 12000)
            item['price'] = (round(item['price'] / 1000) * 1000)
            json_data.append(item)
            ID += 1

        print(i)
        time.sleep(0.0)

    completeName = os.path.join("D:\Dev\Tarkov Vue And API\eft_api\prices", f'{datetime.date(datetime.now())}.json')
    with open(completeName, 'w') as outfile:
        json.dump(json_data, outfile)
        outfile.close()




def clearItemsFile(file):
    ID = 1
    with open(file) as json_file:
        data = json.load(json_file)
        for i in range(0, len(data)):
            item = data[i]
            try:
                item['id'] = item.pop('_id')
            except:
                print()


            item['id'] = str(ID)
            item.pop('uid', None)
            item.pop('tags', None)
            item.pop('url', None)
            item.pop('enImg', None)
            item.pop('enName', None)
            item.pop('change24', None)
            item.pop('change7d', None)
            item.pop('updated', None)
            item.pop('avgDayPrice', None)
            item.pop('avgWeekPrice', None)
            item.pop('priceUpdated', None)
            item.pop('shortName', None)
            item.pop('ruImg', None)
            item.pop('ruName', None)
            item.pop('cnName', None)
            item.pop('cnShortName', None)
            item.pop('ruShortName', None)
            item.pop('deName', None)
            item.pop('deShortName', None)
            item.pop('frName', None)
            item.pop('frShortName', None)
            item.pop('esName', None)
            item.pop('esShortName', None)
            item.pop('pricePerSlot', None)
            item.pop('avgDayPricePerSlot', None)
            item.pop('avgWeekPricePerSlot', None)
            if 100000 > item['price'] > 50000:
                if random.randint(1, 5) > 3:
                    item['price'] += random.randint(1000, 3000)
                else:
                    item['price'] -= random.randint(1000, 7000)

            elif 20000000 > item['price'] > 100000:
                if random.randint(1, 5) > 3:
                    item['price'] += random.randint(1000, 15000)
                else:
                    item['price'] -= random.randint(3000, 12000)
            item['price'] = (round(item['price']/1000)*1000)

            ID += 1
        with open(file, 'w') as outfile:
            json.dump(data, outfile)

parseItems()
#clearItemsFile("2020-06-28.json")

