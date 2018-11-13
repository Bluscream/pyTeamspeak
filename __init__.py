from sys import version_info
outdated = False
if version_info[0] < 3: outdated = True
elif version_info[1] < 5: outdated = True
elif version_info[2] < 3: outdated = True
if outdated: raise Exception("Python 3.5.3+ is required!")
"""
from myteamspeak import *
from teamspeak import *

Python 3.5.3+
"""
from core import WebSession
from asyncio import get_event_loop

if __name__ == '__main__':
    session = WebSession()
    loop = get_event_loop()
    print("csrf_token:", session.csrf_token)
    test = loop.run_until_complete(session.get('https://www.myteamspeak.com/login', loop=loop))
    print("csrf_token:", session.csrf_token)
    test = loop.run_until_complete(session.post('https://www.myteamspeak.com/login?_token:{token}&ts_password:{ts_password}&ts_email:{ts_email_encoded}', loop=loop))
    print("csrf_token:", session.csrf_token)
    print(test)
    loop.close()