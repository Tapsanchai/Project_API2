# from app import __init__
import requests
from bs4 import BeautifulSoup

size_effects_covid_astra_url ='https://thematter.co/quick-bite/astrazeneca-side-effects/145303'
size_effects_covid_sino_url = 'https://thematter.co/quick-bite/sinovac-side-effect/141501'

def show_size_effects_vaccines(url_as,url_sino):
    # astra
    res_as = requests.get(url_as,timeout=(20,20))
    res_as.encoding = "utf-8"

    # sino
    res_si = requests.get(url_sino,timeout=(20,20))
    res_si.encoding = "utf-8"

    # if res_as.status_code == 200 and res_si.status_code == 200:
    # print('call http = Success.', res_as)
    soup_as = BeautifulSoup(res_as.text, 'html.parser')
    soup_si = BeautifulSoup(res_si.text, 'html.parser')
    # print(soup.prettify())
    soup_img_as = soup_as.find('img',{'class':'aligncenter wp-image-145401 size-full'}).get('src')
    soup_img_si = soup_si.find('img',{'class':'aligncenter wp-image-141502 size-full'}).get('src')
    # soup_img_all = soup_all.find('div',{'id':'QA_1'})

    # print('soup_img_as: ',soup_img_as, '->', type(soup_img_as))
    # print('soup_img_as: ',soup_img_si, '->', type(soup_img_si))
    # print('soup_img_all: ',soup_img_all.find_all('li'), '->', type(soup_img_all))
    
    dict_size_effect_values = {}
    list_size_effect_values = []
    list_size_effect_values.append(soup_img_as.strip())
    list_size_effect_values.append(soup_img_si.strip())
    dict_size_effect_values = {'SF1': list_size_effect_values}
    # print(dict_size_effect_values)
    
    # for key in dict_report_values.values():
    #     print(key)
    #     print(key[0])
    #     # print(item[0])
    #     # print(item[1])

    return dict_size_effect_values

    # elif res_as.status_code == 404 and res_si.status_code == 404:
    #     print('call http = NotFound.', res_as) 
    # else:
    #     print('call http = Error.', res_as)


# if __name__ == '__main__':
#     show_size_effects_vaccines()