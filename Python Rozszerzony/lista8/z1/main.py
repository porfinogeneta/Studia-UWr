# TODO
# - pobrać dane z dwóch serwisów oferujących API
# - 1 ma mieć uwierzytelnianie
# - wykorzystać asyncio/aiohttp
# - importować klucze prywatne

import asyncio
import aiohttp
from aiohttp import ClientSession
from secrets import api_key
async def fetch_page(session, url):
    async with session.get(url) as result:
        res = await result.text()
    return res


async def main():
    API_url = ['https://wolnelektury.pl/api/epochs/', f'https://api.spoonacular.com/recipes/complexSearch?apiKey={api_key}']
    async with aiohttp.ClientSession() as session:
        requests = [fetch_page(session, url) for url in API_url]
        # * odpakowuje nam listę, tworząc osobne argumenty dla funkcji
        return await asyncio.gather(*requests)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for elem in asyncio.run(main()):
        print(elem)
