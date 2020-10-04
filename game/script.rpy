# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define t = Character("Трикстер")#, color='#990066', image = "will")
define d = Character("Дерево")#, color='#990066', image = "will")
define e = Character("Эхо", color='#990066')
define r = Character("Русалка")#, color='#990066', image = "will")

init:
# hide screen daytime with noisedissolve
    $ blod = ImageDissolve(im.Tile("blod.png"), 3.0, 30, reverse=False)
    $ flash = ImageDissolve(im.Tile("flash.png"), 2.0, 20)

    $ dt = "ночь"
screen daytime:
    if dt == "пыль":
        add "#7679"
    if dt == "ночь":
        add "#000b"

init:
    $ timer_range = 0
    $ timer_jump = 0
    $ renpy.music.register_channel("bgloop", mixer="sfx", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    $ renpy.music.register_channel("bgloop2", mixer="sfx", loop=True, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    $ renpy.music.register_channel("bgsfx1", mixer="sfx", loop=False, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    $ renpy.music.register_channel("bgsfx2", mixer="sfx", loop=False, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    $ renpy.music.register_channel("bgsfx3", mixer="sfx", loop=False, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)
    $ renpy.music.register_channel("bgsfx4", mixer="sfx", loop=False, stop_on_mute=True, tight=False, file_prefix='', file_suffix='', buffer_queue=True, movie=False, framedrop=True)

init:
    transform cred_up:
        yalign 1.5
        linear 10 yalign 0.5
        
    transform alpha_dissolve:
        alpha 0.0
        linear 0.5 alpha 1.0
        on hide:
            linear 0.5 alpha 0
    screen countdown:
        timer 0.01 repeat True action If(time > 0, true=SetVariable('time', time - 0.01), false=[Hide('countdown'), Jump(timer_jump)])
        bar value time range timer_range xalign 0.5 yalign 0.9 xmaximum 300 at alpha_dissolve
        $ time = 0.7
        $ timer_range = 0.7
        $ timer_jump = 'deadone'
    #show screen countdown
    
# Изображения
init:
    image black = Solid("#000000")
    image smert = Solid("#980002")
    
# Заставка

label splashscreen:
    scene black
    with Pause(1)

    show text "Content Warning: Offensive language" with dissolve
    with Pause(2)

    hide text with dissolve
    with Pause(1)

    return
    
# Игра начинается здесь:

label start:
    scene black
    $ renpy.pause(3.0, hard=True)
    
    scene l1 with flash
    stop music
    play music "audio/BGsound.wav"
    show eileen happy

    t "Так-так-так. Еще один заплутавший."
    
    scene l1_2

    t "Вижу, ты попал сюда из другого мира. Много странников сюда уже забрело. Не боишься повторить их судьбу?"

    t "Не переживай, еще недавно я был таким же скитающимся по мирам бродягой. Скоро и ты привыкнешь к этому месту."

    jump label2

    return

label label2:
    scene l1
    $ q = []
    while len(q) < 3:
        menu:
            "Идти вперед":
                $ q.append(1)
                $ renpy.block_rollback()
                scene l1
                e "Неужели заблудился?"
            "Идти назад":
                $ q.append(1)
                $ renpy.block_rollback()
                scene l1
                e "Подсказать дорогу?"
            "Заблудиться":
                jump label3
        
    return
        
label label3:           
    scene l3
    
    d "Ты заблудился? Выглядишь усталым, я бы сказало - изможденным. Не хочешь прилечь здесь, на моих удобных корнях?"
    $ q = []
    while len(q) < 5:
                    menu:
                        "Cогласиться с предложением":
                            "Теплые корни дерева будто бы обнимают, сладкая тяжесть болотного воздуха клонит к земле, а голова наполняется баюкающей монотонной песней дерева."
                            "К сожалению, проснуться вам уже не суждено. Вы погибли!"
                            scene smert with blod
                            "Попытка пройти по топкой трясине обернулась печальным, но предсказуемым исходом."
                            "Вас ждала долгая и мучительная смерть, несущая чувства беспомощности и неотвратимости."
                            "Вы погибли!"
                            jump start
                        "Cпросить о лесе":
                            $ q.append(1)
                            $ renpy.block_rollback()
                            d "О, я помню этот лес... Я - одно из старейших деревьев в нем! Я проросло здесь еще когда не было никаких идо..."
                            "Вы услышали странный звук. Кажется, дерево захрапело."
                            menu:
                                "Обратить на себя внимание вежливым кашлем":
                                    d "Кто посмел потревожить мой... Ого!"
                                    d "Ты заблудился? Выглядишь усталым, я бы сказало - изможденным. Не хочешь прилечь здесь, на моих удобных корнях?"
                                    jump label3
                                "Пнуть дерево":
                                    d "Кто посмел потревожить мой... Ого!"
                                    d "Ты заблудился? Выглядишь усталым, я бы сказало - изможденным. Не хочешь прилечь здесь, на моих удобных корнях?"
                                    jump label3
                                "Уйти":
                                    d "Путники нынче такими невоспитанными стали!"
                                    jump label3_2
                        "Cпросить о правильной дороге":
                            d "Посмотри на меня внимательно."
                            d "Я похоже на что-то, что умеет пользоваться дорогами? Я дерево!"
                            d "Я не знаю никаких правильных путей. Да и тебе никуда идти не нужно, ведь тут так хорошо, так сонно, так спокойно. Лучше отдохнуть, поспать немного..."
                            e "Какой-то заколдованный круг, не правда ли?"
                            $ q.append(2)
                            $ renpy.block_rollback()
                        "Cпросить, почему дерево говорит":
                            d "В каком смысле, почему я говорю?{w=1} Что за некультурный вопрос!"
                            d "Все деревья говорят. Но я понимаю, ты не со зла, от усталости лезут в голову всякие глупости."
                            d "Тебе нужно просто прилечь и восстановить силы."
                            $ q.append(3)
                            $ renpy.block_rollback()
                        "Cпросить про торчащий из коры кинжал":
                            d "Ах это? Его со злобой воткнула в меня одна истеричная особа."
                            d "Она истекала кровью и пошатывалась мимо, когда я просто предложило прилечь и отдохнуть на своих корнях. Вот и проявляй потом заботу!"
                            d "Вообще, я плохо разбираюсь в личинах людей, но кажется, она была чем-то опечалена. И что самое возмутительное, перед этим она даже не удосужилась вытереть его от своей мерзкой крови!"
                            menu:
                                "Попытаться вытащить кинжал!":
                                    d "А ну прекрати! Не отдам!"
                                    d "Сейчас вынешь, и я соком своим истеку."
                            d "Коли не найдешь мне живой водицы дабы рану мою залечить, даже не проси."
                            $ q.append(4)
                            $ renpy.block_rollback()
                        "Проигнорировать дерево":
                            d "Путники нынче такими невоспитанными стали!"
                            jump label3_3
    return

label label3_2:

    scene l3
    
    menu:
        "Идти дальше через болото":
            scene smert with blod
            "Попытка пройти по топкой трясине обернулась печальным, но предсказуемым исходом."
            "Вас ждала долгая и мучительная смерть, несущая чувства беспомощности и неотвратимости."
            "Вы погибли!"
            jump start
        "Вернуться назад":
            jump label2

    return
    
label label3_3:

    scene l3
    
    menu:
        "Идти дальше через болото":
            jump label4
        "Вернуться назад":
            jump label2

    return
    
label label4:

    scene l2_2
    
    r "Уйди! Я не желаю ничего слышать! Можешь так ему и сказать!"
    menu:
        "Поинтересоваться, что происходит":
            r "А, ты… А кто ты, собственно такой? Никогда не видела тебя раньше."
            r "Ты ведь не отсюда. Ты заблудился?"
            menu:
                "Согласиться":
                    r "Ужасно! Еще одна жертва этого проклятого места..."
                "Отрицать":
                    r "Ты просто еще не понял, куда попал."
                    r "И как плохи твои дела..."
        "Уйти":
            jump label4_2
            
    r "Здесь все искажено, извращенно и зацикленно."
    r "Жизнь в этом лесу - сплошная пытка."
    r "Я столько раз пыталась убежать отсюда.{w=1} Но, как видишь, даже смерть не помогла."
    menu:
        "Переспросить про смерть":
            r "Ты не видишь? Я навья. Русалка. Я убила себя в надежде на избавление. Но и это не помогло. Лес вцепился в мою душу и никогда уже не отдаст."
            menu:
                "Промолчать":
                    "Удивлен? Не бойся."
                "Попятиться":
                    "Стой, не бойся!"
    r "Я не причиню тебе вреда. Единственная в этом лесу, наверное."
    r "Для тебя может еще есть шанс. Я дам тебе это. Навий посох. Коль на что-то направишь свет из глазниц черепа, так оно откроет тебе сокрытое."
    menu:
        "Поблагодарить":
            "Получен Навий посох."
    r "Как давно я не слышала эти слова. Послушай, коль и вправду хочешь отблагодарить, то не в службу, а в дружбу: найдешь поминальный пирожок, не ешь и не выкидывай, а мне принеси, хорошо?{w=3} И берегись того, в красной рубашке!"
    
    return
    

label label4_2:

    scene l2
    
    menu:
        "Идти вперед":
            jump label5
        "Идти назад":
            jump label5
            
    return
    
    
label label5:

    scene l4
    
    "Похоже, вы смогли выбраться из топей"
    
    
    
    return
    
    
label end:

    scene black with dissolve
    show text "Менеджер проекта:{p}{p}Анна Большекова vk.com/machaonorientis{p}{p}Главный сценарист:{p}{p}Святослав Жиленко{p}{p}Программист:{p}{p}Анна Большекова vk.com/machaonorientis{p}{p}Художники:{p}{p}...{p}{p}{p}{p}{p}Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)" at cred_up
    $ renpy.pause(14, hard = True)
    
    return