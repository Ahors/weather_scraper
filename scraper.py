import requests
from bs4 import BeautifulSoup
import random


def get_user_agent():
    ua_file = 'user_agents.txt'
    random_ua = ''
    try:
        with open(ua_file, 'rt') as f:
            lines = f.readlines()
        random_ua = random.choice(lines).strip('\n')
    except Exception as ex:
        print('Something went wrong with')
        print(str(ex))
    finally:
        return random_ua


user_agent = get_user_agent()
site_url = 'https://www.ilmatieteenlaitos.fi/saa/turku?forecast=daily'
headers = {
    'user-agent': user_agent}
page = requests.get(site_url, headers=headers)
soup = BeautifulSoup(page.content, 'html.parser')


def get_temperature():
    temperatures = []
    for temp in soup.select('.local-weather-forecast-day-menu-item'):
        temperatures.append(temp.get_text().split())
    return temperatures


print(get_temperature())
