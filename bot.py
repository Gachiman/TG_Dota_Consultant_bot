import config
import conter_picker
import dotabase
import telebot
from telebot import types
import language

bot = telebot.TeleBot(config.TOKEN)

lang = {}
steam_id = {}
picker = {}
pick_status = {}


# @bot.message_handler()
# def lol(message):
# 	bot.send_message(message.chat.id, 'Return me to the main page.')


@bot.message_handler(commands=['start'])
def start(message):
    global lang
    if message.from_user.language_code == 'ru':
        lang[message.chat.id] = language.Russian()
    else:
        lang[message.chat.id] = language.English()

    if picker.get(message.chat.id, None):
        picker.pop(message.chat.id, None)

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add(lang[message.chat.id].start_print_info_about, lang[message.chat.id].conter_picker)
    markup.add(lang[message.chat.id].help, lang[message.chat.id].change_steam_id)

    bot.send_message(message.chat.id, lang[message.chat.id].start_next, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == lang[message.chat.id].go_to_the_start)
def start_menu(message):
    if picker.get(message.chat.id, None):
        picker.pop(message.chat.id, None)

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add(lang[message.chat.id].start_print_info_about, lang[message.chat.id].conter_picker)
    markup.add(lang[message.chat.id].help, lang[message.chat.id].change_steam_id)

    bot.send_message(message.chat.id, lang[message.chat.id].start_next, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == lang[message.chat.id].help)
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.send_message(message.chat.id, lang[message.chat.id].help_description)


@bot.message_handler(func=lambda message: message.text == lang[message.chat.id].change_steam_id)
@bot.message_handler(commands=['change_steam_id'])
def change_steam_id(message):
    bot.send_message(message.chat.id, lang[message.chat.id].change_steam_id_0)


@bot.message_handler(regexp=r'\d+')
def save_steam_id(message):
    steam_id[message.chat.id] = int(message.text)
    bot.send_message(message.chat.id, lang[message.chat.id].change_steam_id_1 + message.text)
    start(message)


@bot.message_handler(func=lambda message: message.text == lang[message.chat.id].start_print_info_about)
@bot.message_handler(commands=['get_info_about'])
def info_about_(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=False)
    markup.add(lang[message.chat.id].info_get_player)
    markup.add(lang[message.chat.id].help_info_about, lang[message.chat.id].go_to_the_start)

    bot.send_message(message.chat.id, lang[message.chat.id].what_info, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == lang[message.chat.id].help_info_about)
@bot.message_handler(commands=['get_info_about_help'])
def send_help_info_about(message):
    bot.send_message(message.chat.id, lang[message.chat.id].help_info_about_description)


@bot.message_handler(func=lambda message: message.text == lang[message.chat.id].info_get_player)
def get_player_info(message):
    if not steam_id.get(message.chat.id, None):
        bot.send_message(message.chat.id, lang[message.chat.id].change_steam_id_0)
        return

    player = dotabase.get_player_by_id(steam_id[message.chat.id])
    bot.send_message(message.chat.id, lang[message.chat.id].player_info_hi + player['name'])
    bot.send_photo(message.chat.id, player['pic_src'])
    most_played_heroes = player['most_played_heroes']
    most_played_heroes_msg = lang[message.chat.id].player_most_played_heroes
    for hero in most_played_heroes:
        most_played_heroes_msg += lang[message.chat.id].player_most_played_heroes_matches.format(hero[0], hero[1])
    bot.send_message(message.chat.id, most_played_heroes_msg)


@bot.message_handler(func=lambda message: message.text == lang[message.chat.id].conter_picker)
@bot.message_handler(commands=['start_pick'])
def picker_start(message):
    picker[message.chat.id] = conter_picker.Picker(lang[message.chat.id])
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(lang[message.chat.id].picker_ally, lang[message.chat.id].picker_enemy)
    markup.add(lang[message.chat.id].picker_delete_hero_ally, lang[message.chat.id].picker_delete_hero_enemy)
    markup.add(lang[message.chat.id].picker_refresh, lang[message.chat.id].go_to_the_start)
    bot.send_message(message.chat.id, lang[message.chat.id].picker_pick_hero, reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == lang[message.chat.id].picker_ally)
@bot.message_handler(commands=['ally'])
def ally_picked(message):
    if not picker.get(message.chat.id, None):
        return
    if len(picker[message.chat.id].allies) >= 4:
        return
    if message.text.startswith('/ally') and len(message.text.split(' ')) > 1:
        hero_name = ' '.join(message.text.split()[1:])
        if not picker[message.chat.id].find_hero_name(hero_name):
            bot.send_message(message.chat.id, lang[message.chat.id].picker_try_again)
            return

        picker[message.chat.id].ally_add(hero_name)
        bot.send_message(message.chat.id, picker[message.chat.id].show_suggestions())
        bot.send_message(message.chat.id, picker[message.chat.id].show_current_pick())
    else:
        pick_status[message.chat.id] = 'ally_pick'
        bot.reply_to(message, lang[message.chat.id].what_hero)


@bot.message_handler(func=lambda message: message.text == lang[message.chat.id].picker_enemy)
@bot.message_handler(commands=['enemy'])
def enemy_picked(message):
    if not picker.get(message.chat.id, None):
        return
    if len(picker[message.chat.id].enemies) >= 5:
        return
    if message.text.startswith('/enemy') and len(message.text.split(' ')) > 1:
        hero_name = ' '.join(message.text.split()[1:])
        if not picker[message.chat.id].find_hero_name(hero_name):
            bot.send_message(message.chat.id, lang[message.chat.id].picker_try_again)
            return

        picker[message.chat.id].enemy_add(hero_name)
        bot.send_message(message.chat.id, picker[message.chat.id].show_suggestions())
        bot.send_message(message.chat.id, picker[message.chat.id].show_current_pick())
    else:
        pick_status[message.chat.id] = 'enemy_pick'
        bot.reply_to(message, lang[message.chat.id].what_hero)


@bot.message_handler(func=lambda message: message.text == lang[message.chat.id].picker_delete_hero_ally)
@bot.message_handler(commands=['del_ally'])
def ally_delete(message):
    if not picker.get(message.chat.id, None):
        return
    if len(picker[message.chat.id].allies) <= 0:
        return
    if message.text.startswith('/ally') and len(message.text.split(' ')) > 1:
        hero_name = ' '.join(message.text.split()[1:])
        if not picker[message.chat.id].find_hero_name(hero_name):
            bot.send_message(message.chat.id, lang[message.chat.id].picker_try_again)
            return

        picker[message.chat.id].ally_del(hero_name)
        bot.send_message(message.chat.id, picker[message.chat.id].show_suggestions())
        bot.send_message(message.chat.id, picker[message.chat.id].show_current_pick())
    else:
        pick_status[message.chat.id] = 'ally_del'
        bot.reply_to(message, lang[message.chat.id].what_hero)


@bot.message_handler(func=lambda message: message.text == lang[message.chat.id].picker_delete_hero_enemy)
@bot.message_handler(commands=['del_enemy'])
def enemy_delete(message):
    if not picker.get(message.chat.id, None):
        return
    if len(picker[message.chat.id].enemies) <= 0:
        return
    if message.text.startswith('/enemy') and len(message.text.split(' ')) > 1:
        hero_name = ' '.join(message.text.split()[1:])
        if not picker[message.chat.id].find_hero_name(hero_name):
            bot.send_message(message.chat.id, lang[message.chat.id].picker_try_again)
            return

        picker[message.chat.id].enemy_del(hero_name)
        bot.send_message(message.chat.id, picker[message.chat.id].show_suggestions())
        bot.send_message(message.chat.id, picker[message.chat.id].show_current_pick())
    else:
        pick_status[message.chat.id] = 'enemy_del'
        bot.reply_to(message, lang[message.chat.id].what_hero)


@bot.message_handler(func=lambda message: message.text == lang[message.chat.id].picker_refresh)
@bot.message_handler(commands=['refresh'])
def refresh_hero_pick(message):
    if picker.get(message.chat.id, None):
        picker[message.chat.id].picker_refresh()
        pick_status[message.chat.id] = None
        bot.send_message(message.chat.id, picker[message.chat.id].show_current_pick())


@bot.message_handler()
def pick_hero(message):
    if message.chat.id not in pick_status.keys():
        return
    if not picker[message.chat.id].find_hero_name(message.text):
        bot.send_message(message.chat.id, lang[message.chat.id].picker_try_again)
        return

    if pick_status[message.chat.id] == 'ally_pick':
        if len(picker[message.chat.id].allies) >= 4:
            return
        picker[message.chat.id].ally_add(message.text)
    elif pick_status[message.chat.id] == 'enemy_pick':
        if len(picker[message.chat.id].enemies) >= 5:
            return
        picker[message.chat.id].enemy_add(message.text)
    elif pick_status[message.chat.id] == 'ally_del':
        if len(picker[message.chat.id].allies) <= 0:
            return
        picker[message.chat.id].ally_del(message.text)
    elif pick_status[message.chat.id] == 'enemy_del':
        if len(picker[message.chat.id].enemies) <= 0:
            return
        picker[message.chat.id].enemy_del(message.text)

    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(lang[message.chat.id].picker_ally, lang[message.chat.id].picker_enemy)
    markup.add(lang[message.chat.id].picker_delete_hero_ally, lang[message.chat.id].picker_delete_hero_enemy)
    markup.add(lang[message.chat.id].picker_refresh, lang[message.chat.id].go_to_the_start)

    bot.send_message(message.chat.id, picker[message.chat.id].show_suggestions())
    bot.send_message(message.chat.id, picker[message.chat.id].show_current_pick(), reply_markup=markup)


try:
    bot.polling()
except KeyError as e:
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add('/start')
    bot.send_message(e, 'I\'m ready to rise.', reply_markup=markup)
    bot.polling()
