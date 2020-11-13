import csv
import requests
from bs4 import BeautifulSoup

pages_num = list(range(1,26))
raw_link = 'https://www.kivano.kg/mobilnye-telefony?page='
links = []
for x in pages_num:
    links.append(raw_link + str(x))


def get_html(url):
    res = requests.get(url)
    return res.text


def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    try:
        name = soup.find('div', class_='listbox_title oh').get_text(strip=True)
    except:
        name = ''

    try:
        price = soup.find('div', class_='listbox_price text-center').get_text(strip=True)
    except:
        price = ''
    try:
        photo = soup.find('div', class_='listbox_img pull-left').get_text(strip=True)
    except:
        photo = ''
    data = {'name': name, 'price': price, 'photo': photo}
    return data

def write_csv(data):
    with open('phones.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['name'], data['price'], data['photo']])
        print([data['name'], data['price'], data['photo']], 'parsed')

def main():
        for link in links:
            html = get_html(link)
            data = get_page_data(html)
            write_csv(data)

if name == "__main__":
    main()