import csv
import requests
from bs4 import BeautifulSoup

# pages_num = list(range(1,26))
# raw_link = 'https://www.kivano.kg/mobilnye-telefony?page='
# links = []
# for x in pages_num:
#     links.append(raw_link + str(x))


def get_html(url):
    res = requests.get(url)
    return res.text



max_page = 25
pages = []

for x in range(1,max_page + 1):
    pages.append('https://www.kivano.kg/mobilnye-telefony?page=' + str(x))


def get_page_data(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('div', class_ = 'item product_listbox oh')
    tels = []
    for item in items :
        tels.append (
            {
                'name' : item.find('div', class_ = 'listbox_title oh').find('a').get_text(strip = True),
                'price' : item.find('div', class_ = 'listbox_price text-center').find('strong').get_text(strip = True),
                'image' : item.find('div',class_ = 'listbox_img pull-left').find_all('img src')
            }
        )

    print(tels)

        # try:
    #     price = soup.find(class_='listbox_price text-center')
    # except:
    #     price = ''
    # try:
    #     photo = soup.find(class_='listbox_img pull-left')
    # except:
    #     photo = ''
    # data = {'name': name, 'price': price, 'photo': photo}
#     print(tels)

def write_csv(data):
    with open('phones.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['name'], data['price'], data['image']])
        print([data['name'], data['price'], data['image']], 'parsed')

def main():
    tels = []
    for page in pages:
        html = get_html(pages)
        data = get_page_data(html)
        write_csv(data)


if __name__ == "__main__":
    main()