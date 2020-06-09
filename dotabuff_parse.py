import sqlite3
import requests
import sys
import lxml.html


headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/81.0.4044.96 YaBrowser/20.4.0.1461 Yowser/2.5 Safari/537.36'
}


def sql_connection():
    try:
        con = sqlite3.connect('dotabuff.db')
        return con
    except sqlite3.Error as e:
        print(e)
        sys.exit()


def get_heroes_list():
    try:
        response = requests.get('https://ru.dotabuff.com/heroes', headers=headers)
    except requests.ConnectionError as e:
        print(e)
        sys.exit()
    dota_doc = lxml.html.fromstring(response.content)
    heroes_list = dota_doc.xpath('/html/body/div[1]/div[8]/div[3]/section[2]/footer/div/a/div/div[1]/text()')
    heroes_list = ((hero,) for hero in heroes_list)
    return heroes_list


def get_heroes_cryptonyt(hero_name):
    try:
        response = requests.get(f'https://ru.dotabuff.com/heroes/{hero_name}/counters', headers=headers)
    except requests.ConnectionError as e:
        print(e)
        sys.exit()
    doc = lxml.html.fromstring(response.content)
    cryptonyt_name = doc.xpath('/html/body/div[1]/div[8]/div[3]/section[3]/article/table/tbody/tr/td[2]/a/text()')
    cryptonyt_value = [item.rstrip('%') for item in
                       doc.xpath('/html/body/div[1]/div[8]/div[3]/section[3]/article/table/tbody/tr/td[3]/text()')]
    cryptonyt = zip(cryptonyt_name, cryptonyt_value)
    return cryptonyt


def create_table_heroes_list(con):
    cursor = con.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS Heroes('
                   'id INTEGER PRIMARY KEY NOT NULL,'
                   'hero_name TEXT NOT NULL)')
    if not cursor.execute('SELECT * FROM Heroes WHERE id=1').fetchone():
        for hero in get_heroes_list():
            cursor.execute('INSERT INTO Heroes(hero_name) VALUES (?)', hero)
    con.commit()


def create_cryptonits_tables(con):
    cursor = con.cursor()
    heroes_list = [item[0].lower() for item in cursor.execute('SELECT hero_name FROM Heroes').fetchall()]
    for hero in heroes_list:
        hero = hero.replace("\'", "").replace(" ", "-")
        hero1 = hero.replace("-", "_").replace(" ", "_")
        cursor.execute(f'CREATE TABLE IF NOT EXISTS {hero1}_contr('
                       'id INTEGER PRIMARY KEY NOT NULL,'
                       'hero_name TEXT NOT NULL,'
                       'hero_value TEXT NOT NULL)')
        for contr_hero in get_heroes_cryptonyt(hero):
            cursor.execute(f'INSERT INTO {hero1}_contr(hero_name, hero_value) VALUES (?, ?)', contr_hero)
    con.commit()


def get_hero_crypronit(hero):
    cursor = sql_connection().cursor()
    hero = hero.replace("-", "_")
    hero_contr_list = {item[0].lower().replace(' ', '-').replace('\'', ''): item[1] for item in cursor.execute(
            f'SELECT hero_name, hero_value FROM {hero}_contr'
    )}
    return hero_contr_list


def get_heroes_names_list():
    cursor = sql_connection().cursor()
    hero_contr_list = {item[0].lower().replace(' ', '-').replace('\'', ''): item[0] for item in cursor.execute(
        'SELECT hero_name FROM Heroes')}
    return hero_contr_list


if __name__ == '__main__':
    create_cryptonits_tables(sql_connection())
