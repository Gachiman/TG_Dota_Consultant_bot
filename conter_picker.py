import dotabuff_parse
import json
from decimal import Decimal


heroes_slang = None
with open('heroes.json', encoding='utf-8') as data_file:
    heroes_slang = json.load(data_file)

heroes_names_list = dotabuff_parse.get_heroes_names_list()


class Picker:
    def __init__(self, lang):
        self.allies = set()
        self.enemies = set()
        self.suggestions = {}
        self.lang = lang

    def ally_add(self, hero):
        if len(self.allies) >= 4:
            return
        hero = self.find_hero_name(hero)
        if hero is None:
            return
        contr_list = dotabuff_parse.get_hero_crypronit(hero)

        self.allies.add(hero)
        for hero_name, hero_value in contr_list.items():
            self.suggestions[hero_name] = self.suggestions.get(hero_name, 0) + Decimal(hero_value)

    def enemy_add(self, hero):
        if len(self.enemies) >= 5:
            return
        hero = self.find_hero_name(hero)
        if hero is None:
            return
        contr_list = dotabuff_parse.get_hero_crypronit(hero)

        self.enemies.add(hero)
        for hero_name, hero_value in contr_list.items():
            self.suggestions[hero_name] = self.suggestions.get(hero_name, 0) - Decimal(hero_value)

    def ally_del(self, hero):
        if len(self.allies) <= 0:
            return
        hero = self.find_hero_name(hero)
        if hero is None:
            return
        contr_list = dotabuff_parse.get_hero_crypronit(hero)

        self.allies.remove(hero)
        for hero_name, hero_value in contr_list.items():
            self.suggestions[hero_name] = self.suggestions.get(hero_name, 0) + Decimal(hero_value)

    def enemy_del(self, hero):
        if len(self.enemy) <= 0:
            return
        hero = self.find_hero_name(hero)
        if hero is None:
            return
        contr_list = dotabuff_parse.get_hero_crypronit(hero)

        self.enemy.remove(hero)
        for hero_name, hero_value in contr_list.items():
            self.suggestions[hero_name] = self.suggestions.get(hero_name, 0) - Decimal(hero_value)

    def picker_refresh(self):
        self.allies = set()
        self.enemies = set()
        self.suggestions = {}

    def show_current_pick(self):
        allies = [heroes_names_list[hero] for hero in self.allies]
        allies_mes = '  ||  '.join(allies) if allies else '  -'
        enemies = [heroes_names_list[hero] for hero in self.enemies]
        enemies_mes = '  ||  '.join(enemies) if enemies else '  -'

        shown_message = self.lang.cp_show_current_pick.format(allies_mes, enemies_mes)
        return shown_message

    def show_suggestions(self):
        selected_heroes = self.allies | self.enemies
        suggestion = self.suggestions

        if len(selected_heroes) > 1:
            for hero in selected_heroes:
                suggestion.pop(hero)
        suggestion = sorted(suggestion.items(), key=lambda y: y[1], reverse=True)

        suggestion = [f'{heroes_names_list[hero[0]]}: {str(hero[1]).lstrip("-")}' for hero in suggestion]
        shown_message = '\n'.join(suggestion)

        return self.lang.cp_show_suggestion.format(shown_message)

    def find_hero_name(self, hname):
        hname = hname.lower()
        return_name = None
        for hero_id_name, hero_name in heroes_names_list.items():
            if hname == hero_name:
                return_name = hero_id_name
        for hero_id_name, hero_slang_names in heroes_slang.items():
            if hname in hero_slang_names[0].split(', ') or hname == hero_id_name:
                return_name = hero_id_name

        if return_name in (self.allies | self.enemies):
            return None
        return return_name


if __name__ == '__main__':
    pass
