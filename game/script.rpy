﻿# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define t = Character("Трикстер")#, color='#990066', image = "will")
define d = Character("Дерево")#, color='#990066', image = "will")
define e = Character("Эхо", color='#990066')
define r = Character("Русалка")#, color='#990066', image = "will")
define v = Character("Ведьма")#, color='#990066', image = "will")
define l = Character("Леший")#, color='#990066', image = "will")
define i = Character("Идол")#, color='#990066', image = "will")

init:
# hide screen daytime with noisedissolve
    $ blod = ImageDissolve(im.Tile("blod.png"), 3.0, 30, reverse=False)
    $ flash = ImageDissolve(im.Tile("flash.png"), 2.0, 20)

    $ dt = "ночь"
screen daytime:
    if dt == "ночь":
        add "#000b"

init:
    $ timer_range = 0
    $ timer_jump = 0
    
init:
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
$ timer_jump = 'dead'
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
    
    centered "На вещем камне написано:{p}{p}Направо пойдешь - к мертвым на обед попадешь. Как хочешь, так и понимай.{p}{p}Налево пойдешь - сердце тьмы найдешь. Хотя туда только по записи, так что не факт.{p}{p}Прямо пойдешь - а сам сходи и узнай, чего это я тут распинаюсь. Да еще и в рифму, мне за такое не платят"
    
    menu:
        "Идти вперед":
            jump label7
        "Идти налево":
            jump label6
        "Идти направо":
            jump label6
        "Идти назад":
            jump label5
    
    return
    
label label6:

    scene l5
    
    v "Мравствуй. И откуда мы такие красивые? Какой румянец да вид свежий. Очень соблазнительно."
    v "А пойдем ко мне в избу, я тебя накормлю, напою да спать уложу."
    v "Круг кружит, пруток лежит, ручеек под ним бежит, как сломаю я пруток, ворожбы настанет срок, бег воды остановится, слово крепкое смолвится."

    menu:
        "Сопротивляться чарам": #qte
            v "Ах, не слушай глупую одинокую женщину, несу всякий вздор. Пойдем лучше в избу, пироги да блины остывают, я тебе угожу, раны твои исцелю да силы восстановлю."
    v "Ну вот и славно. Пойдем, пойдем. Раздевайся, тебе это все уже будет не нужно. Садись пока сюда, на лопату, а я добавлю жару в печи."
    
    $ q = []
    while len(q) < 5:
        menu:
            "Принять предложение":
                v "Мудро рассудил. Проходи через порожек аккуратно. Вот и все. Кто через порог прошел, тот моим стал. Раздевайся, тебе это все уже будет не нужно. Садись пока сюда, на лопату, а я добавлю жару в печи."
                jump start
            "Убежать":
                jump label8
            "Спросить про правильный путь из леса":
                v "Путь путеюшки змеятся, лентой ситцевой кружатся, ленточкой тебя свяжу, чары в сердце положу"
                menu:
                    "Сопротивляться": #qte
                        v "Я та, кого ты и искал. Коль хочешь выбраться из чащи, так я одна тебе и помогу. Но для почину тебя надо в баньке попарить да блинами накормить."
                        menu:
                            "Применить навий посох": #qte
                                jump label7
            "Спросить, кто она":
                v "Я та, кого ты и искал. Коль хочешь выбраться из чащи, так я одна тебе и помогу. Но для почину тебя надо в баньке попарить да блинами накормить."
                $ q.append(2)
                $ renpy.block_rollback()
            "Применить навий посох":
                v "Эти мавкины причуды здесь не работают."
                $ q.append(1)
                $ renpy.block_rollback()
    
    return
    
label label6_1:

    scene l5
    "На миг вместо прекрасной женщины перед вами предстала уродливая мертвая старуха."
    v "Ах ты лиходей срамный! Получай костяной ногой!"
    menu:
        "Уклониться": #qte
            jump label7
    
return
    
label label7:

    scene l1_2
    
    l "Кто это бродит по моему лесу? Не видал твою морду раньше. Ну, поклонись лесному хозяину!"
    menu:
        "Поклониться":
            l "Ха-ха, ну спасибо! Давно меня никто уже хозяином сего леса не признает."
        "Отказаться":
            l "Вот, никто меня теперь не считает здесь хозяином."
            
    l "А все из-за зла давно уж здесь поселившегося. Все думают, коль плутаем да блуждаем, коль тьма душит, так это леший повинен. Ан нет, все нечистое от того поганого капища идет!"
    l "Помоги нам! Разломай идола на капище! Спаси лес, а мы уж в долгу не останемся. Коль исполнишь просьбу да пожелаешь, выведу тебя самой короткой дорогой, не будь я леший."
    
    menu:
        "Согласиться":
            l "Вот и славно! Скоро мы все наконец вздохнем спокойно да закатим пир на весь мир. И ты отправишься домой мед пиво пить."
        "Отказаться":
            l "Эх, не зазорна трусость. Коль сам бы не трусил, вызвал бы силу нечистую на поле бранное!"
        "Использовать посох навьи": #qte
            l "Ах ты..дочурка моя, девица красна. Сгубил ее этот лес, все силы выжал. А я, не смог уберечь ни лес, ни ее. Бедняжка руки на себя наложила. Жалкий я дурень..."
            l "Послушай, возьми водичку живую. Коль встретится она тебе, молю, плесни на нее. Она вновь в живую обратится. Я бы сам сходил... да не могу ей в очи смотреть ее навьи, укора и ненависти полные. "
            l "От стыда в голове будто чаща от ветра дикого шумит."
            # смерть
        
    jump label8
    
    return
    
label label8:
    
    scene l6
    
    i "Еще один смертный. Ты пришел принести жертву?"
    
    $ q = []
    while len(q) < 5:
        menu:
            "Спросить про жертву":
                i "Ты разговариваешь с богом этого леса! Пади ниц и принеси мне достойную жертву! Сердце разумного существа! И тогда, я смилостивлюсь и не покараю тебя за твою дерзость, червь. И может даже выпущу отсюда. Обещаю, что выпущу."
                $ q.append(1)
                $ renpy.block_rollback()
            "Применить посох": #qte
                i "Я - злая, испорченная душа этого леса. Мне нужны вкусные души путников вроде тебя, забредших в этот мир случайно."
                i "Если меня не будут кормить жертвами, я умру. А я очень боюсь умирать. Не будет никакого перерождения. Я не хочу. Я должен поглотить души!"
                i "Я ведь могу закончить твои страдания… Выпустить тебя. Просто принеси мне сердца!"
                $ q.append(2)
                $ renpy.block_rollback()
            "Потребовать освободить себя":
                i "Ты смеешь что-то требовать от меня? Кто тебе вообще разрешил разговаривать со мной? Исчезни, ничтожество."
                jump dead
            "Уйти":
                jump dead
    # menu:
            "Разломать идол":
                "Вы касаетесь идола и земля проваливается у вас под ногами."
                jump dead
    
    return
    
label dead:
    
    scene smert with blod:
        time 3
    $ renpy.pause(3.0, hard=True)
    "Вы погибли!"
    
    jump end
    
    return
    
label end:

    scene black with dissolve
    show text "Менеджер проекта:{p}{p}Анна Большекова vk.com/machaonorientis{p}{p}Главный сценарист:{p}{p}Святослав Жиленко{p}{p}Программист:{p}{p}Анна Большекова vk.com/machaonorientis{p}{p}Художники:{p}{p}...{p}{p}{p}{p}{p}Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)" at cred_up
    $ renpy.pause(14, hard = True)
    
    return