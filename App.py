#THERE WILL BE TWO FILES.
#
# FIRST ONE-THE PYTHON FILE'S CODE IS GIVEN HERE


import kivy

import sqlite3 as sql

kivy.require("1.11.1")

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
from kivy.base import runTouchApp
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
# from kivy.base import runTouchApp
from kivy.uix.screenmanager import ScreenManager, Screen, CardTransition

Builder.load_file('kivy.kv')


class ScreenOne(Screen):
    pass
class ScreenTwo(Screen):
    pass


class ScreenThree(Screen):

    def double_operation(self):

        str1 = self.inp.text
        string1 = str1.lower()

        dict1 = {
            "a": "._ ",
            "b": "_... ",
            "c": "_._. ",
            "d": "_.. ",
            "e": ". ",
            "f": ".._. ",
            "g": "__. ",
            "h": ".... ",
            "i": ".. ",
            "j": ".___ ",
            "k": "_._ ",
            "l": "._.. ",
            "m": "__ ",
            "n": "_. ",
            "o": "___ ",
            "p": ".__. ",
            "q": "__._ ",
            "r": "._. ",
            "s": "... ",
            "t": "_ ",
            "u": ".._ ",
            "v": "..._ ",
            "w": ".__ ",
            "x": "_.._ ",
            "y": "_.__ ",
            "z": "__.. ",
            "1": ".____ ",
            "2": "..___ ",
            "3": "...__ ",
            "4": "...._ ",
            "5": "..... ",
            "6": "_.... ",
            "7": "__... ",
            "8": "___.. ",
            "9": "____. ",
            "0": "_____ ",
            ".": "._._._ ",
            ",": "__..__ ",
            "?": "..__.. ",
            "!": "_._.__ ",
            "'": ".____. ",
            "(": "_.__. ",
            ")": "_.__._ ",
            "&": "._... ",
            ":": "___... ",
            ";": "_._._. ",
            "/": "_.._. ",
            "_": "..__._ ",
            "=": "_..._ ",
            "+": "._._. ",
            "-": "_...._ ",
            "$": "..._.._ ",
            "@": ".__._. ",
            " ": " "
        }
        output = ""
        for word in string1:
            output += dict1.get(word, "NR")
        self.dbl.text = output
        self.inp.text = ""
        print(f" In English '{str1}' in morse code '{output}'")

    def single_operation(self):


        dict2 = {
            "._": "a",
            "_...": "b",
            "_._.": "c",
            "_..": "d",
            ".": "e",
            ".._.": "f",
            "__.": "g",
            "....": "h",
            "..": "i",
            ".___": "j",
            "_._": "k",
            "._..": "l",
            "__": "m",
            "_.": "n",
            "___": "o",
            ".__.": "p",
            "__._": "q",
            "._.": "r",
            "...": "s",
            "_": "t",
            ".._": "u",
            "..._": "v",
            ".__": "w",
            "_.._": "x",
            "_.__": "y",
            "__..": "z",
            ".____": "1",
            "..___": "2",
            "...__": "3",
            "...._": "4",
            ".....": "5",
            "_....": "6",
            "__...": "7",
            "___..": "8",
            "____.": "9",
            "_____": "0",
            "._._._": ".",
            "__..__": ",",
            "..__..": "?",
            "_._.__": "!",
            ".____.": "'",
            "_.__.": "(",
            "_.__._": ")",
            "._...": "&",
            "___...": ":",
            "_._._.": ";",
            "_.._.": "/",
            "..__._": "_",
            "_..._": "=",
            "._._.": "+",
            "_...._": "-",
            "..._.._": "$",
            ".__._.": "@"

        }

        str2 = self.dbl.text
        msg = str2
        out = []
        letter = []
        j = -1
        for i in msg.split(' '):
            j += 1
            letter += [i.split('|')]
            for k in range(len(letter[j])):
                out += dict2.get(letter[j][k], 'NN')
            out += ' '

        # ''.join(out)
        self.inp.text = ''.join(out)
        self.dbl.text = ""
        print(f" In Morse '{str2}' in morse code '{''.join(out)}'")
        # output2 = ""
        # for word in list:
        #     output2 += dict2.get(word, "NIL")
        # self.inp.text = output2
        # self.dbl.text = ""
        # # print(str3)
        # print(f" In Morse '{str2}' in morse code '{output2}'")

    def add_user(self):
        con = sql.connect('m.db')
        cur = con.cursor()
        cur.execute(""" INSERT INTO id (inp,dbl) VALUES (?,?)""", (self.inp.text, self.dbl.text))

        con.commit()
        con.close()


class ScreenFour(Screen):
    pass

class ScreenFive(Screen):
    pass

class ScreenSix(Screen):
    pass


class ScreenSeven(Screen):
    pass


class ScreenEight(Screen):
    pass

class ScreenNine(Screen):

    def bin_dec(self):
        ab=self.btod.text
        num = str(ab)

        if "." in num:
            splitted = num.split(".")
            str3 = str(splitted[0])
            str4 = str(splitted[1])
            ss = ""
            sum1 = 0
            sum2 = 0
            c = -1
            f = -1

            for b in range(len(str3)):
                ss = ss + str3[c]
                c = c - 1
            for d in range(len(str3)):
                sum1 = sum1 + int(ss[d]) * (2 ** d)

            for e in range(len(str4)):
                sum2 = sum2 + int(str4[e]) * (2 ** f)
                f = f - 1

            sum = sum1 + sum2

        else:
            strk = ""
            sum = 0
            l = -1
            for i in range(len(num)):
                strk = strk + num[l]
                l = l - 1
            for k in range(len(num)):
                sum = sum + int(strk[k]) * (2 ** k)

        self.btd.text = str(sum)
    def add2_user(self):


        ab =  sql.connect('l.db')
        ab1 = ab.cursor()
        ab1.execute(""" INSERT INTO id (btod,btd) VALUES (?,?)""", (self.btod.text, self.btd.text))
        ab.commit()
        ab.close()






class ScreenTen(Screen):

    def bin_oct(self):

        num = self.btoo.text

        if "." in num:
            splitted = num.split(".")
            str1 = str(splitted[0])
            str2 = str(splitted[1])
            ss = ""
            sum1 = 0
            sum2 = 0
            c = -1
            f = -1

            for b in range(len(str1)):
                ss = ss + str1[c]
                c = c - 1
            for d in range(len(str1)):
                sum1 = sum1 + int(ss[d]) * (2 ** d)

            for e in range(len(str2)):
                sum2 = sum2 + int(str2[e]) * (2 ** f)
                f = f - 1

            sum = sum1 + sum2

        else:
            strk = ""
            sum = 0
            l = -1
            for i in range(len(num)):
                strk = strk + num[l]
                l = l - 1
            for k in range(len(num)):
                sum = sum + int(strk[k]) * (2 ** k)

        x = int(sum)
        sumd = ""
        strk = ""
        l = -1

        while x >= 1:
            c = x // 8
            d = str(x % 8)
            sumd = sumd + d
            x = c
        for i in range(len(sumd)):
            strk = strk + sumd[l]
            l = l - 1

        self.bto.text=strk
        self.btoo.text=""

    def add1_user(self):

        conn = sql.connect('k.db')
        curr = conn.cursor()
        curr.execute(""" INSERT INTO id (btoo,bto) VALUES (?,?)""", (self.btoo.text, self.bto.text))

        conn.commit()
        conn.close()



class ScreenEleven(Screen):

    def bin_hex(self):

        num = str(self.btoh.text)

        if "." in num:
            splitted = num.split(".")
            str1 = str(splitted[0])
            str2 = str(splitted[1])
            ss = ""
            sum1 = 0
            sum2 = 0
            c = -1
            f = -1

            for b in range(len(str1)):
                ss = ss + str1[c]
                c = c - 1
            for d in range(len(str1)):
                sum1 = sum1 + int(ss[d]) * (2 ** d)

            for e in range(len(str2)):
                sum2 = sum2 + int(str2[e]) * (2 ** f)
                f = f - 1

            sum = sum1 + sum2

        else:
            strk = ""
            sum = 0
            l = -1
            for i in range(len(num)):
                strk = strk + num[l]
                l = l - 1
            for k in range(len(num)):
                sum = sum + int(strk[k]) * (2 ** k)

        x = int(sum)
        sumd1 = ""

        strk = ""

        l = -1

        while x >= 1:
            c = x // 16
            d = (x % 16)
            if d >= 10 and d <= 15:
                dict1 = {
                    10: "A",
                    11: "B",
                    12: "C",
                    13: "D",
                    14: "E",
                    15: "F"
                }
                sumd1 = sumd1 + str(dict1[d])
            else:
                sumd1 = sumd1 + str(d)
            x = c

        for i in range(len(sumd1)):
            strk = strk + sumd1[l]
            l = l - 1

        self.bth.text=strk
        self.btoh.text=""
    def add3_user(self):
        qw=sql.connect('n.db')
        qw1=qw.cursor()
        qw1.execute("""INSERT INTO id (btoh,bth) VALUES (?,?)""",(self.btoh.text, self.bth.text))

        qw.commit()
        qw.close()

class ScreenTwelve(Screen):

    def oct_dec(self):

        ab = self.otod.text
        num=str(ab)
        if "." in num:
            splitted = str(num).split(".")
            str1 = str(splitted[0])
            str2 = str(splitted[1])
            ss = ""
            sum1 = 0
            sum2 = 0
            c = -1
            f = -1

            for b in range(len(str1)):
                ss = ss + str1[c]
                c = c - 1
            for d in range(len(str(splitted[1]))):
                sum1 = sum1 + int(ss[d]) * (8 ** d)

            for e in range(len(str2)):
                sum2 = sum2 + int(str2[e]) * (8 ** f)
                f = f - 1

            sum = sum1 + sum2

        else:
            strk = ""
            sum = 0
            l = -1
            for i in range(len(num)):
                strk = strk + num[l]
                l = l - 1
            for k in range(len(num)):
                sum = sum + int(strk[k]) * (8 ** k)

        self.otd.text = str(sum)
        self.otod.text=""

    def add4_user(self):
        wq = sql.connect('o.db')
        wq1 = wq.cursor()
        wq1.execute("""INSERT INTO id (otod,otd) VALUES (?,?)""", (self.otod.text, self.otd.text))

        wq.commit()
        wq.close()


class ScreenThirteen(Screen):

    def oct_bin(self):

        num = str(self.otob.text)

        if "." in num:
            splitted = num.split(".")
            str1 = str(splitted[0])
            str2 = str(splitted[1])
            ss = ""
            sum1 = 0
            sum2 = 0
            c = -1
            f = -1

            for b in range(len(str1)):
                ss = ss + str1[c]
                c = c - 1
            for d in range(len(str1)):
                sum1 = sum1 + int(ss[d]) * (8 ** d)

            for e in range(len(str2)):
                sum2 = sum2 + int(str2[e]) * (8 ** f)
                f = f - 1

            sum = sum1 + sum2

        else:
            strk = ""
            sum = 0
            l = -1
            for i in range(len(num)):
                strk = strk + num[l]
                l = l - 1
            for k in range(len(num)):
                sum = sum + int(strk[k]) * (8 ** k)

        x = int(sum)
        sumd = ""
        strk = ""
        l = -1

        while x >= 1:
            c = x // 2
            d = str(x % 2)
            sumd = sumd + d
            x = c
        for i in range(len(sumd)):
            strk = strk + sumd[l]
            l = l - 1

        self.otb.text = strk
        self.otob.text = ""

    def add5_user(self):
        er = sql.connect('q.db')
        er1 = er.cursor()
        er1.execute("""INSERT INTO id (otob,otb) VALUES (?,?)""", (self.otob.text, self.otb.text))

        er.commit()
        er.close()


class ScreenFourteen(Screen):
    def oct_hex(self):

        num = str(self.otoh.text).upper()
        if "." in num:
            splitted = num.split(".")
            str1 = str(splitted[0])
            str2 = str(splitted[1])
            ss = ""
            sum1 = 0
            sum2 = 0
            c = -1
            f = -1

            for b in range(len(str1)):
                ss = ss + str1[c]
                c = c - 1
            for d in range(len(str1)):
                sum1 = sum1 + int(ss[d]) * (8 ** d)

            for e in range(len(str2)):
                sum2 = sum2 + int(str2[e]) * (8 ** f)
                f = f - 1

            sum = sum1 + sum2

        else:
            strk = ""
            sum = 0
            l = -1
            for i in range(len(num)):
                strk = strk + num[l]
                l = l - 1
            for k in range(len(num)):
                sum = sum + int(strk[k]) * (8 ** k)

        x = int(sum)
        sumd1 = ""

        strk = ""

        l = -1

        while x >= 1:
            c = x // 16
            d = (x % 16)
            if d >= 10 and d <= 15:
                dict1 = {
                    10: "A",
                    11: "B",
                    12: "C",
                    13: "D",
                    14: "E",
                    15: "F"
                }
                sumd1 = sumd1 + str(dict1[d])
            else:
                sumd1 = sumd1 + str(d)
            x = c

        for i in range(len(sumd1)):
            strk = strk + sumd1[l]
            l = l - 1
        self.oth.text=strk
        self.otoh.text=""

    def add6_user(self):
        ty = sql.connect('p.db')
        ty1 = ty.cursor()
        ty1.execute("""INSERT INTO id (otoh,oth) VALUES (?,?)""", (self.otoh.text, self.oth.text))

        ty.commit()
        ty.close()



class ScreenFifteen(Screen):

    def dec_bin(self):

        x = int(self.dtob.text)
        sumd = ""
        strk = ""
        lll = -1

        while x >= 1:
            c = x // 2
            d = str(x % 2)
            sumd = sumd + d
            x = c
        for i in range(len(sumd)):
            strk = strk + sumd[lll]
            lll = lll - 1
        self.dtb.text = strk
        self.dtob.text = ""

    def add7_user(self):
        ui = sql.connect('r.db')
        ui1 = ui.cursor()
        ui1.execute("""INSERT INTO id (dtob,dtb) VALUES (?,?)""", (self.dtob.text,self.dtb.text))

        ui.commit()
        ui.close()


class ScreenSixteen(Screen):

    def dec_oct(self):

        x = int(self.dtoo.text)
        sumd = ""
        strk = ""
        l = -1

        while x >= 1:
            c = x // 8
            d = str(x % 8)
            sumd = sumd + d
            x = c
        for i in range(len(sumd)):
            strk = strk + sumd[l]
            l = l - 1
        self.dto.text = str(strk)
        self.dtoo.text = ""

    def add8_user(self):
        op = sql.connect('s.db')
        op1 = op.cursor()
        op1.execute("""INSERT INTO id (dtoo,dto) VALUES (?,?)""", (self.dtoo.text,self.dto.text))

        op.commit()
        op.close()


class ScreenSeventeen(Screen):

    def dec_hex(self):

        x = int(self.dtoh.text)
        sumd1 = ""

        strk = ""

        l = -1

        while x >= 1:
            c = x // 16
            d = (x % 16)
            if d >= 10 and d <= 15:
                dict1 = {
                    10: "A",
                    11: "B",
                    12: "C",
                    13: "D",
                    14: "E",
                    15: "F"
                }
                sumd1 = sumd1 + str(dict1[d])
            else:
                sumd1 = sumd1 + str(d)
            x = c

        for i in range(len(sumd1)):
            strk = strk + sumd1[l]
            l = l - 1
        self.dth.text = strk
        self.dtoh.text = ""

    def add9_user(self):
        ad = sql.connect('t.db')
        ad1 = ad.cursor()
        ad1.execute("""INSERT INTO id (dtoh,dth) VALUES (?,?)""", (self.dtoh.text,self.dth.text))

        ad.commit()
        ad.close()


class ScreenEighteen(Screen):

    def hex_bin(self):

        num = str(self.htob.text)
        strk = ""
        sum1 = 0
        sum2 = 0

        l = -1
        for i in range(len(num)):
            strk = strk + num[l]
            l = l - 1
            strk = strk.upper()

        for k in strk:

            if k.isalpha():

                dict = {
                    "A": 10,
                    "B": 11,
                    "C": 12,
                    "D": 13,
                    "E": 14,
                    "F": 15
                }

                sum2 = sum2 + dict[k] * (16 ** strk.find(k))
            elif k.isdigit():
                sum1 = sum1 + int(k) * (16 ** (strk.find(k)))

        x = int(sum1 + sum2)
        sumd = ""
        strk = ""
        l = -1

        while x >= 1:
            c = x // 2
            d = str(x % 2)
            sumd = sumd + d
            x = c
        for i in range(len(sumd)):
            strk = strk + sumd[l]
            l = l - 1
        self.htb.text = strk
        self.htob.text=""

    def add10_user(self):
        fg = sql.connect('u.db')
        fg1 = fg.cursor()
        fg1.execute("""INSERT INTO id (htob,htb) VALUES (?,?)""", (self.htob.text,self.htb.text))

        fg.commit()
        fg.close()


class ScreenNineteen(Screen):

    def hex_oct(self):
        num = str(self.htoo.text)
        strk = ""
        sum1 = 0
        sum2 = 0

        l = -1
        for i in range(len(num)):
            strk = strk + num[l]
            l = l - 1
            strk = strk.upper()

        for k in strk:

            if k.isalpha():

                dict = {
                    "A": 10,
                    "B": 11,
                    "C": 12,
                    "D": 13,
                    "E": 14,
                    "F": 15
                }

                sum2 = sum2 + dict[k] * (16 ** strk.find(k))
            elif k.isdigit():
                sum1 = sum1 + int(k) * (16 ** (strk.find(k)))

        x = int(sum1 + sum2)
        sumd = ""
        strk = ""
        l = -1

        while x >= 1:
            c = x // 8
            d = str(x % 8)
            sumd = sumd + d
            x = c
        for i in range(len(sumd)):
            strk = strk + sumd[l]
            l = l - 1
        self.hto.text=strk
        self.htoo.text=""

    def add11_user(self):
        hj = sql.connect('v.db')
        hj1 = hj.cursor()
        hj1.execute("""INSERT INTO id (htoo,hto) VALUES (?,?)""", (self.htoo.text,self.hto.text))

        hj.commit()
        hj.close()

class ScreenTwenty(Screen):

    def hex_dec(self):
        ab=self.htod.text
        num = str(ab)
        strk = ""
        sum1 = 0
        sum2 = 0

        l = -1
        for i in range(len(num)):
            strk = strk + num[l]
            l = l - 1
            strk = strk.upper()

        for k in strk:

            if k.isalpha():

                dict = {
                    "A": 10,
                    "B": 11,
                    "C": 12,
                    "D": 13,
                    "E": 14,
                    "F": 15
                }

                sum2 = sum2 + dict[k] * (16 ** strk.find(k))
            elif k.isdigit():
                sum1 = sum1 + int(k) * (16 ** (strk.find(k)))

        self.htd.text=str(sum1+sum2)
        self.htod.text=""

    def add12_user(self):
        kl = sql.connect('w.db')
        kl1 = kl.cursor()
        kl1.execute("""INSERT INTO id (htod,htd) VALUES (?,?)""", (self.htod.text,self.htd.text))

        kl.commit()
        kl.close()



screen_manager = ScreenManager()

screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))
screen_manager.add_widget(ScreenThree(name="screen_three"))
screen_manager.add_widget(ScreenFour(name="screen_four"))
screen_manager.add_widget(ScreenFive(name="screen_five"))
screen_manager.add_widget(ScreenSix(name="screen_six"))
screen_manager.add_widget(ScreenSeven(name="screen_seven"))
screen_manager.add_widget(ScreenEight(name="screen_eight"))
screen_manager.add_widget(ScreenNine(name="screen_nine"))
screen_manager.add_widget(ScreenTen(name="screen_ten"))
screen_manager.add_widget(ScreenEleven(name="screen_eleven"))
screen_manager.add_widget(ScreenTwelve(name="screen_twelve"))
screen_manager.add_widget(ScreenThirteen(name="screen_thirteen"))
screen_manager.add_widget(ScreenFourteen(name="screen_fourteen"))
screen_manager.add_widget(ScreenFifteen(name="screen_fifteen"))
screen_manager.add_widget(ScreenSixteen(name="screen_sixteen"))
screen_manager.add_widget(ScreenSeventeen(name="screen_seventeen"))
screen_manager.add_widget(ScreenEighteen(name="screen_eighteen"))
screen_manager.add_widget(ScreenNineteen(name="screen_nineteen"))
screen_manager.add_widget(ScreenTwenty(name="screen_twenty"))


class KivyApp(App):
    try:

        con = sql.connect('m.db')
        cur = con.cursor()
        cur.execute(""" CREATE TABLE id(
            inp text,
            dbl text)
            """)

        con.commit()
        con.close()




    except:

        pass

    try:
        conn = sql.connect('k.db')
        curr = conn.cursor()
        curr.execute(""" CREATE TABLE id(
                btoo text,
                bto text)
                """)

        conn.commit()
        conn.close()
    except:

        pass

    try:
        ab = sql.connect('l.db')
        ab1 = ab.cursor()
        ab1.execute(""" CREATE TABLE id(
                        btod text,
                        btd text)
                        """)

        ab.commit()
        ab.close()
    except:
        pass

    try:
        qw = sql.connect('n.db')
        qw1 = qw.cursor()
        qw1.execute("""CREATE TABLE id(
                        btoh text,
                        bth text)
                        """)
        qw.commit()
        qw.close()
    except:
        pass
    try:
        wq = sql.connect('o.db')
        wq1 = wq.cursor()
        wq1.execute("""CREATE TABLE id(
                        otod text,
                        otd text)
                        """)
        wq.commit()
        wq.close()
    except:
        pass

    try:
        er = sql.connect('q.db')
        er1 = er.cursor()
        er1.execute("""CREATE TABLE id(
                        otob text,
                        otb text)
                        """)
        er.commit()
        er.close()
    except:
        pass

    try:
        ty = sql.connect('p.db')
        ty1 = ty.cursor()
        ty1.execute("""CREATE TABLE id(
                        otoh text,
                        oth text)
                        """)
        ty.commit()
        ty.close()
    except:
        pass

    try:
        ui = sql.connect('r.db')
        ui1 = ui.cursor()
        ui1.execute("""CREATE TABLE id(
                        dtob text,
                        dtb text)
                        """)
        ui.commit()
        ui.close()
    except:
        pass

    try:
        op = sql.connect('s.db')
        op1 = op.cursor()
        op1.execute("""CREATE TABLE id(
                        dtoo text,
                        dto text)
                        """)
        op.commit()
        op.close()
    except:
        pass

    try:
        ad = sql.connect('t.db')
        ad1 = ad.cursor()
        ad1.execute("""CREATE TABLE id(
                           dtoh text,
                           dth text)
                           """)
        ad.commit()
        ad.close()
    except:
        pass

    try:
        fg = sql.connect('u.db')
        fg1 = fg.cursor()
        fg1.execute("""CREATE TABLE id(
                           htob text,
                           htb text)
                           """)
        fg.commit()
        fg.close()
    except:
        pass

    try:
        hj = sql.connect('v.db')
        hj1 = hj.cursor()
        hj1.execute("""CREATE TABLE id(
                           htoo text,
                           hto text)
                           """)
        hj.commit()
        hj.close()
    except:
        pass

    try:
        kl = sql.connect('w.db')
        kl1 = kl.cursor()
        kl1.execute("""CREATE TABLE id(
                           htod text,
                           htd text)
                           """)
        kl.commit()
        kl.close()
    except:
        pass

    def build(self):
        return screen_manager


sample_app = KivyApp()
sample_app.run()
