# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define e = Character("Уильям", color='#990066', image = "will")

init:
# hide screen daytime with noisedissolve
    $ blod = ImageDissolve(im.Tile("blod.png"), 3.0, 30, reverse=False)
    $ flash2 = ImageDissolve(im.Tile("flash.png"), 2.0, 20)

    $ dt = "ночь"
screen daytime:
    if dt == "пыль":
        add "#7679"
    if dt == "ночь":
        add "#000b"

init:
    transform cred_up:
        yalign 1.5
        linear 10 yalign 0.5
        
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

    scene bg room

    show eileen happy

    e "Вы создали новую игру Ren'Py."

    e "Добавьте сюжет, изображения и музыку и отправьте её в мир!"

    jump end

    return

label end:

    scene black with dissolve
    show text "Менеджер проекта:{p}{p}Анна Большекова vk.com/machaonorientis{p}{p}Главный сценарист:{p}{p}Святослав Жиленко{p}{p}Программист:{p}{p}Анна Большекова vk.com/machaonorientis{p}{p}Художники:{p}{p}...{p}{p}{p}{p}{p}Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)" at cred_up
    $ renpy.pause(14, hard = True)
    
    return