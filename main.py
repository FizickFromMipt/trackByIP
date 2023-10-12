import requests
import pyfiglet
import folium

def get_info_by_ip(ip='127.0.0.1'):
    try:
        #получаем данные про наш ip посредствам get запроса
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        #делаем словарь под данные из ответа
        data = {
            '[IP]' : response.get('query'),
            '[Int prov]' : response.get('isp'),
            '[Org]' : response.get('org'),
            '[Country]' : response.get('country'),
            '[Region Name]' : response.get('regionName'),
            '[City]' : response.get('city'),
            '[ZIP]' : response.get('zip'),
            '[Lat]' : response.get('lat'),
            '[Lon]' : response.get('lon')
        }

        for k, v in data.items():
            print(f'{k} : {v}')

        #передает координаты
        area=folium.Map(location=[response.get('lat'), response.get('lon')])
        #сохраняем карту
        area.save(f'{response.get("query")}_{response.get("city")}.html')

    except requests.exceptions.ConnectionError:
        print('Проверьте соединение!')


def main():
    #красивая надпись в терминале)))
    preview_text = pyfiglet.Figlet(font='slant')
    print(preview_text.renderText('IP INFO'))
    ip = input('Введите ваш IP-адрес : ')

    get_info_by_ip(ip=ip)


if __name__ == '__main__':
    main()
