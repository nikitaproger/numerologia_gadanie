from doctest import master


class numerology():
    def __init__(self):
        self.basic_num = {
            "1": "1 - Лидер, пионер. Энергия действия, амбиции, независимость. Минус: эгоизм.",
            "2": "2 - Миротворец. Дипломатия, партнерство, интуиция. Минус: неуверенность, зависимость от других.",
            "3": "3 - Творец. Оптимизм, талант, общительность. Минус: поверхностность, разбросанность.",
            "4": "4 - Строитель. Стабильность, трудолюбие, надежность. Минус: скука, негибкость.",
            "5": "5 - Искатель приключений. Свобода, любознательность, страсть к переменам. Минус: безответственность.",
            "6": "6 - Заботливый. Ответственность, семья, гармония, служение. Минус: желание все контролировать.",
            "7": "7 - Мыслитель. Анализ, мудрость, уединение, интуиция. Минус: замкнутость.",
            "8": "8 - Босс. Власть, материальный успех, амбиции. Минус: одержимость деньгами.",
            "9": "9 - Мудрец. Сострадание, завершение, широта души. Минус: иллюзии, желание спасать всех.",
            "11": "11 - Мастер-интуиции. Просветление, вдохновение, связь с тонким миром.",
            "22": "22 - Мастер-строитель. Воплощение великих идей в реальность, глобальные проекты.",
            "33": "33 - Мастер-целитель. Высшее сострадание, безусловная любовь, исцеление мира.",
        }
    def mt(self, a):
        ch = 0
        for z in str(a):
            ch += int(z)
        return ch

    def pr(self, a):
        dip = ""
        for i in a:
            dip = dip + "," + str(i)
        return dip

    def main_chet(self, XX, YY, ZZ):
        self.p1 = XX
        self.p2 = YY
        self.p3 = ZZ
        self.master_num = []

        if XX not in [11, 22, 33]:
            self.p1 = self.mt(XX)
        else:
            self.master_num.append(self.p1)
        if YY not in [11, 22, 33]:
            self.p2 = self.mt(YY)
        else:
            self.master_num.append(self.p2)
        if ZZ not in [11, 22, 33]:
            self.p3 = self.mt(ZZ)
        else:
            self.master_num.append(self.p3)
        if (self.p1 + self.p2 + self.p3) not in [11, 22, 33]:
            self.C = self.p1 + self.p2 + self.p3
            if self.C in [11, 22, 33]:
                self.otvet = self.C
            else:
                self.otvet = self.C
                while self.otvet > 9:
                    if self.otvet == 11 or self.otvet == 22 or self.otvet == 33:
                        break
                    self.otvet = self.mt(self.otvet)
        else:
            self.otvet = self.p1 + self.p2 + self.p3
        if self.master_num != 0:
            return self.basic_num[str(self.otvet)], self.master_num

a = int(input("Введите число дня рождения: "))
b = int(input("Введите месяц рождения (числом): "))
c = int(input("Введите год рождения: "))
num = numerology()
result, mater_nim = num.main_chet(a, b, c)
if len(mater_nim) > 0:
    mater_nim_itog = num.pr(mater_nim)
    print(result,"ваше число под усилением мастер-чисел: ",mater_nim_itog)
else:
    print(result)