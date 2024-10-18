import turtle                                                       # Подключение библиотеки turtle

from time import sleep                                              # Подключение метода sleep библиотеки time
from math import tan, sqrt, pi, pow, radians                        # Подключение методов для работы с математическими функциями


__all__ = ["main"]
def clock(clockRadius):                                             # Функция рисования часов, передаваемые значаения - радиус часов
    t.pensize(3)                                                    # Установка толщины пера на 3 px
    t.penup()                                                       # Поднятие пера
    t.home()                                                        # Возврат пера в изначальное положение
    t.pendown()                                                     # Опустить перо
    t.dot(10)                                                       # Рисование точки размером 10 px
    t.penup()                                                       # Поднятие пера
    t.goto(0,-clockRadius)                                          # Перемещение пера в казанную точку
    t.pendown()                                                     # Опустить перо
    t.circle(clockRadius)                                           # Рисование круга с заданным радиусом

def arrow(degree, r, th):                                           # Функция рисование стрелы, передаваеммые значения - градус, длина, толщина стрелки
    t.pensize(th)                                                   # Установка толщину пера на th
    if degree <= 90:                                                # Если градус <= 90 то
        angle = abs(degree - 90)                                    # Вычитание 90 градусов
    elif degree <= 180:                                             # Если градус <= 180 то
        angle = abs(degree - 180)                                   # Вычитание 180 градусов
    elif degree <= 270:                                             # Если градус <= 270 то
        angle = abs(degree - 180)                                   # Вычитание 270 градусов
    elif degree <= 360:                                             # Если градус <= 360 то
        angle = abs(degree - 180)                                   # Вычитание 360 градусов
    t.penup()                                                       # Поднятие пера
    x = sqrt(pow(r, 2)/(1+pow(tan(radians(angle)), 2)))             # Расчет абсциссы крайней точки стрелки
    y = int(sqrt(pow(r, 2) - pow(x, 2)))                            # Расчет ординаты крайней точки стрелки
    if degree <= 90:                                                # Если градус <= 90 то
        t.goto(int(x), int(y))                                      # Распологаем стрелку в первой четверти
    elif degree <= 180:                                             # Если градус <= 180 то
        t.goto(y, -int(x))                                          # Распологаем стрелку во второй четверти
    elif degree <= 270:                                             # Если градус <= 270 то
        t.goto(-y, -int(x))                                         # Распологаем стрелку в третьей четверти
    elif degree <= 360:                                             # Вычитание 360 градусов
        t.goto(-y, int(x))                                          # Распологаем стрелку в четвертой четверти
    t.pendown()                                                     # Опустить перо
    t.home()                                                        # Возврат пера в изначальное положение


def main(args: list[str]) -> None:
    turtle.screensize(canvwidth=300, canvheight=300, bg="black")        # Установка размеров окна и его задний фон
    print(turtle.screensize())                                          # Вывод размеров окна в консоль
    t = turtle.Turtle()                                                 # Создание "черепашки" в переменной t

    t.hideturtle()                                                      # Спрятать "черепашку"
    t.color("white")                                                    # Установить цвет "черепашки" на белый
    turtle.title("My Clocks")                                           # Изменение названия окна на "My Clocks"
    clockRadius = 300                                                   # Установка радиуса часов на 300

    turtle.tracer(0, 0)                                                 # Ускорение анимации по средством вывода всего за раз а не постепенно
    seconds = 0                                                         # Установка секунд на ноль
    angleSeconds = 0                                                    # Установка угла секунд на ноль
    angleMinutes = 0                                                    # Установка угла минут на ноль
    angleHours = 0                                                      # Установка угла часов на ноль

    while True:                                                         # Бесконечный цикл для работы часов
        clock(clockRadius)                                              # Вызов функции рисования часов
        arrow(angleSeconds, clockRadius-40, 1)                          # Вызов функции рисования секундной стрелки
        arrow(angleMinutes, clockRadius-60, 2)                          # Вызов функции рисования минутной стрелки
        arrow(angleHours, clockRadius-120, 3)                           # Вызов функции рисования часовой стрелки
        turtle.update()                                                 # Обновление экрана

        seconds += 1                                                    # Увеличение секунд на единицу
        angleSeconds += 6                                               # Увеличение секундного угла на 6, тк в минуте 60 секунд а в окружности 360 градусов
        if seconds % 10 == 0:                                           # Если количество секунд кратно 10 без остатка то
            angleMinutes += 1                                           # Увеличение минутного угла на 1
        if seconds % 120 == 0:                                          # Если количество секунд кратно 120 без остатка то
            angleHours += 1                                             # Увеличение часового угла на 1

        if angleSeconds == 360:                                         # Если секундный угол равен 360 то
            angleSeconds = 0                                            # Обнуление секундного угла
        if angleMinutes == 360:                                         # Если минутный угол равен 360 то
            angleMinutes = 0                                            # Обнуление минутного угла
        if angleHours == 360:                                           # Если часовой угол равен 360 то
            angleHours = 0                                              # Обнуление часового угла
        # sleep(0.001)
        t.clear()                                                       # Очистка экрана


    # r = const
    # y = tg(degree)*x
    # y^2 + x^2 = r^2
    # y^2 = (tg(degree)*x)^2
    # x^2(1+tg(degree)^2) = r^2
    # x = sqrt(r^2/(1+tg(degree)^2))
    # y = sqrt(r^2-x^2)
