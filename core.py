from aiocfscrape import CloudflareScraper

class WebSession(object):
    csrf_token = None
    async def get(self, url, loop=None):
        async with CloudflareScraper(loop=loop) as session:
            async with session.get(url) as resp:
                data = await resp.text()
        csrf_token = resp.cookies["XSRF-TOKEN"].value
        if not self.csrf_token or self.csrf_token != csrf_token:
            self.csrf_token = csrf_token
        return data

    async def post(self, url, payload=None, headers: dict = {}, loop=None):
        headers["XSRF-TOKEN"] = self.csrf_token
        async with CloudflareScraper(loop=loop) as session:
            async with session.post(url=url, data=payload, headers=headers) as resp:
                data = await resp.text()
        return data