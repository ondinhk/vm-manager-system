import asyncio
import csv
import logging

import requests
from bs4 import BeautifulSoup

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', level=logging.INFO)


def crawl_data(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    resource = soup.find_all('div', class_='flex items-center astro-lmapxigl')
    data_html = []
    chunk_size = 5
    for i in range(0, len(resource), chunk_size):
        chunk = resource[i:i + chunk_size]
        data_html.append(chunk)
    total_data = []
    for item in data_html:
        text_list = [html.text for html in item]
        total_data.append(text_list)
    return total_data


def export_data(data):
    csv_file_path = 'output.csv'
    with open(csv_file_path, 'a', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        if csv_file.tell() == 0:
            csv_writer.writerow(['IP Address', 'Port', 'Protocol', 'Country', 'City'])
        csv_writer.writerows(data)


async def run():
    for idx in range(69):
        url_crawl = f'https://iproyal.com/free-proxy-list/?page={idx + 1}&entries=100'
        data_crawl = crawl_data(url_crawl)
        export_data(data_crawl)
        logging.info(f"Export success {idx}")
        await asyncio.sleep(3)
        logging.info("Sleep 3s")


if __name__ == '__main__':
    asyncio.run(run())
