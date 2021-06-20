import requests
from bs4 import BeautifulSoup

report_vaccine_covid19_url ='https://ddc.moph.go.th/vaccine-covid19/pages/%E0%B8%A3%E0%B8%B2%E0%B8%A2%E0%B8%87%E0%B8%B2%E0%B8%99%E0%B8%84%E0%B8%A7%E0%B8%B2%E0%B8%A1%E0%B8%81%E0%B9%89%E0%B8%B2%E0%B8%A7%E0%B8%AB%E0%B8%99%E0%B9%89%E0%B8%B2%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B9%83%E0%B8%AB%E0%B9%89%E0%B8%9A%E0%B8%A3%E0%B8%B4%E0%B8%81%E0%B8%B2%E0%B8%A3%E0%B8%89%E0%B8%B5%E0%B8%94%E0%B8%A7%E0%B8%B1%E0%B8%84%E0%B8%8B%E0%B8%B5%E0%B8%99%E0%B9%82%E0%B8%84%E0%B8%A7%E0%B8%B4%E0%B8%94-19'

def show_report_vaccines(url):
    res = requests.get(url)
    res.encoding = "utf-8"

    if res.status_code == 200:
        print('call http = Success.', res)
        soup = BeautifulSoup(res.text, 'html.parser')
        # print(soup.prettify())
        soup_label = soup.find('label',{'class':'top-highlight'}).get_text()
        soup_img = soup.find('img').get('src')
        # print('soup_label: ',soup_label, '->', type(soup_label))
        # print('soup_img: ',soup_img, '->', type(soup_img))
        obj_img = soup_img
        obj_label = soup_label
        dict_report_values = {'R1': ''}
        list_report_values = []
        list_report_values.append(obj_label.strip())
        list_report_values.append(obj_img.strip())
        dict_report_values = {'R1': list_report_values}
        print(dict_report_values)
        
        for key in dict_report_values.values():
            print(key)
            print(key[0])
            # print(item[0])
            # print(item[1])

        return dict_report_values

    elif res.status_code == 404:
        print('call http = NotFound.', res) 
    else:
        print('call http = Error.', res)


if __name__ == '__main__':
    show_report_vaccines()