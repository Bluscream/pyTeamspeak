import requests

url = "https://www.myteamspeak.com/login"

payload = "_token={token}&ts_password={ts_password}&ts_email={ts_email_encoded}"
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.0",
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    'Accept-Language': "en-US,en;q=0.5",
    'Referer': "https://www.myteamspeak.com/login",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cookie': "__cfduid={cfuid}; cookieconsent_status=dismiss; XSRF-TOKEN={xsrf_token}; myts_session={myts_session}",
    'DNT': "1",
    'Connection': "keep-alive",
    'Upgrade-Insecure-Requests': "1",
    'Pragma': "no-cache",
    'Cache-Control': "no-cache"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)