class English:
    start_next = 'What are you wont?'
    change_steam_id = 'Change steam id.'
    change_steam_id_0 = 'Send me your steam_id.'
    change_steam_id_1 = 'Okay, this is your steam id: '
    start_start_pick = 'Start pick.'
    conter_picker = 'Conter-picker.'
    start_print_info_about = 'I want to see some information.'
    help = 'Help.'
    help_description = 'I am a Dota 2 consultant bot.\n' \
                       'I can help you pick hero base on dotabuff winrate statistic.' \
                       'You can name hero with usual doters slang names (I will try to guess).\n' \
                       'Also I can show you some of the interesting you information.\n\n' \
                       'You can use me with keyboard panel or with commands starts win symbol "/".\n' \
                       'Here list of commands:\n' \
                       '/start = Start me.\n' \
                       '/help = Get info about me (you read this tight now).\n' \
                       '/change_steam_id = Create a new one or change exist steam id.\n' \
                       '/get_info_about = Show you some of interesting you information.\n' \
                       '/get_info_about_help = Get info about dotabuff info section.\n' \
                       '/start_pick = Start the conterpicker.\n' \
                       '/ally = Uses only in Picker. Add an ally for your team.\n' \
                       '/enemy = Uses only in Picker. Add an enemy for enemy team.\n' \
                       '/del_ally = Uses only in Picker. Delete ally hero.\n' \
                       '/del_enemy = Uses only in Picker. Delete enemy hero.\n' \
                       '/refresh = Uses only in Picker. Delete all enemies and allies heroes from draft.\n\n' \
                       'If you somehow lose your control panel, use /start .\n'
    player_info_hi = 'Okay, seems i found you: '
    player_most_played_heroes = 'Your most played heroes are: \n'
    player_most_played_heroes_matches = '{} - {} matches.\n'
    go_to_the_start = 'Return to the main page.'

    what_info = 'What are you interesting for?'
    help_info_about = 'Help about this section.'
    help_info_about_description = 'There you can get some information from dotabuff:\n' \
                                  'Player info - get you information about player with the entered steam id.'
    info_get_player = 'Player info.'
    picker_refresh = 'Refresh pick.'
    picker_ally = 'Ally.'
    picker_enemy = 'Enemy.'
    picker_delete_hero_ally = 'Delete ally hero from pick.'
    picker_delete_hero_enemy = 'Delete enemy hero from pick.'
    picker_pick_hero = 'Who was picked?'
    what_hero = 'What hero name?'
    picker_try_again = 'Please, try again.'

    cp_show_current_pick = 'Allies:\n{}\n\nEnemies:\n{}'
    cp_show_suggestion = 'Pick suggestion:\n{}'


class Russian(English):
    start_next = 'Что пожелаете?'
    change_steam_id = 'Изменить steam id.'
    change_steam_id_0 = 'Пришлите мне свой steam id.'
    change_steam_id_1 = 'Окей, это ваш steam id: '
    start_start_pick = 'Начать пик.'
    conter_picker = 'Контр-пик.'
    start_print_info_about = 'Я хочу увидеть некоторую информацию.'
    help = 'Помощь.'
    help_description = 'Я - бот-консультант Dota 2.\n' \
                       'Я могу помочь вам выбрать героев, основываясь на статистике винрейта dotabuff.' \
                       'Вы можете называть героев обычными дотерскими сленговыми именами (Я постараюсь угадать).\n' \
                       'Также я могу показать вам некоторую интересующую вас информацию.\n\n' \
                       'Вы можете использовать меня с помощью клавиатурной панели или с помощью команд, ' \
                       'начинающихся с символа "/".\n' \
                       'Ниже список доступных команд:\n' \
                       '/start = Запустить меня.\n' \
                       '/help = Получить информацию обо мне (вы читаете это прямо сейчас).\n' \
                       '/change_steam_id = Создать новый или изменить существующий steam id.\n' \
                       '/get_info_about = Показать вам что-то из интересующей вас информации.\n' \
                       '/get_info_about_help = Получить информацию о секции с интересующей вас информацией.\n' \
                       '/start_pick = Запустить контр-пикер.\n' \
                       '/ally = Используется только в пикере. Добавляет союзника в вашу команду.\n' \
                       '/enemy = Используется только в пикере. Добавляет врага в команду противника.\n' \
                       '/del_ally = Используется только в пикере. Удаляет союзного героя.\n' \
                       '/del_enemy = Используется только в пикере. Удаляет вражеского героя.\n' \
                       '/refresh = Используется только в пикере. Удаляет всех союзных и вражеских героев из драфта.\n' \
                       '\nЕсли вы каким-то образом потеряли вашу панель контроля, используйте /start .\n'
    player_info_hi = 'Окей, похоже я нашёл вас: '
    player_most_played_heroes = 'Ваши герои с наибольшим количеством игр: \n'
    player_most_played_heroes_matches = '{} - {} матчей.\n'
    go_to_the_start = 'Вернуться на главную страницу панели.'

    what_info = 'Что вас интересует?'
    help_info_about = 'Вспомогательная информация об этой секции.'
    help_info_about_description = 'Здесь вы можете получить некоторую информацию, связанную с дотой:\n' \
                                  'Информация об игроке - получить информацию об игроке с введённым steam id.'
    info_get_player = 'Информация об игроке.'
    picker_refresh = 'Обновить пик.'
    picker_ally = 'Союзник.'
    picker_enemy = 'Враг.'
    picker_delete_hero_ally = 'Удалить союзного героя из пика.'
    picker_delete_hero_enemy = 'Удалить вражеского героя из пика.'
    picker_pick_hero = 'Кто был выбран?'
    what_hero = 'Назовите героя.'
    picker_try_again = 'Пожалуйста, попробуйте ещё раз.'

    cp_show_current_pick = 'Союзники:\n{}\n\nПротивники:\n{}'
    cp_show_suggestion = 'Предложение по пику:\n{}'
