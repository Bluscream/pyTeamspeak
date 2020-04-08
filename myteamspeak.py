from enum import Enum
from pprint import pprint
import requests
from requests import get, post
from asyncio import get_event_loop
# from aiocfscrape import CloudflareScraper
from bs4 import BeautifulSoup
import cfscrape


# async def test_open_page(url, loop=None):
# async with CloudflareScraper(loop=loop) as session:
#  async with session.get(url) as resp:
# data = await resp.text()
# return data

class myTeamSpeak(object):
    scraper: cfscrape.CloudflareScraper
    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0",
        'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        'Accept-Language': "en-US,en;q=0.5",
        'Referer': "https://www.myteamspeak.com/userarea/badges/redeem",
        'Content-Type': "application/x-www-form-urlencoded",
        #'Cookie': "__cfduid={cfuid}; cookieconsent_status=dismiss; XSRF-TOKEN={xsrf_token}; myts_session={myts_session}",
        'DNT': "1",
        'Connection': "keep-alive",
        'Upgrade-Insecure-Requests': "1",
        'Pragma': "no-cache",
        'Cache-Control': "no-cache"
    }

    def __init__(self):
        # session = requests.Session()
        self.scraper = cfscrape.create_scraper() # sess=session
        self.scraper.headers["Origin"] = "https://www.myteamspeak.com"
        self.scraper.headers["Host"] = "www.myteamspeak.com"

    def getCF(self, url: str):
        return self.scraper.get(url).content

    def RedeemBadgeCode(self, code: str):
        payload = "_token={token}}&ts_redeem_code={code}".format(code=code, token="") # ToDo: Fix token
        self.scraper.headers["Referer"] = "https://www.myteamspeak.com/userarea/badges/redeem"
        self.scraper.headers["Content-Type"] = "application/x-www-form-urlencoded"
        self.scraper.headers['Accept-Encoding'] = None
        pprint(self.scraper.headers)
        ret = self.scraper.post("https://www.myteamspeak.com/userarea/badges/redeem", data=payload)
        pprint(ret)
        print(ret.status_code)
        html = BeautifulSoup(ret.content, features="lxml")
        print(html.find("div", class_="alert"))

    def getServerNickname(socket: object):
        pass

    def modifyServerNicknames(socket: object, nickname_type: str):
        pass


class ServerNicknameType(Enum):
    IP_ADDRESS = "ip_address"
    DOMAIN_NAME = "domain_name"


myts = myTeamSpeak()
myts.RedeemBadgeCode("1234")