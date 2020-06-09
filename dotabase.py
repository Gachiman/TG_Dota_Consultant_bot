import requests
import sys
import lxml.html

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/81.0.4044.96 YaBrowser/20.4.0.1461 Yowser/2.5 Safari/537.36'
}


def get_player_by_id(steam_id):
    try:
        response = requests.get(f'https://www.dotabuff.com/players/{steam_id}', headers=headers)
    except requests.ConnectionError as e:
        print(e)
        sys.exit()
    dota_doc = lxml.html.fromstring(response.content)
    player_name = dota_doc.xpath('.//div[@class="header-content-title"]/h1/text()')[0]
    player_pic_src = dota_doc.xpath(f'.//a[@href="/players/{steam_id}"]/img/@src')[0]
    hero_table = dota_doc.xpath('.//div[@class="row-12 player-summary"]/div/section[2]/article/div/div[@class="r-row"]')

    player = {
        'id': steam_id,
        'name': str(player_name),
        'pic_src': str(player_pic_src),
        'most_played_heroes': get_player_most_heroes(hero_table)
    }

    return player


def get_player_most_heroes(hero_table):
    hero_list = []
    for item in hero_table:
        hero_name = item.xpath('.//div/div/div[2]/a/text()')[0]
        hero_matches = item.xpath('.//div[2]/div[@class="r-body"]/text()')[0]
        hero_list.append((hero_name, hero_matches))

    return hero_list


if __name__ == '__main__':
    pass
