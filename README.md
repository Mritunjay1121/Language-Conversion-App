# verbose-sniffle
Kivy

import kivy
import sqlite3 as sql

kivy.require("1.11.1")

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
#from kivy.base import runTouchApp
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
            " ": "   ",
        }
        output = ""
        for word in string1:
            output += dict1.get(word, "NR")
        self.dbl.text = output
        self.inp.text = ""
        print(f" In English '{str1}' in morse code '{output}'")

    def single_operation(self):

        str2 = self.dbl.text
        list = str2.split(" ")

        dict2 = {
            "._": "a",
            "_...": "b",
            "_._.": "c",
            "_..": "d",
            ".": "e",
            ".._.": "f",
            "__.": "g",
            "....": "h",
            ".. ": "i",
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
            ".__._.": "@",

        }
        output2 = ""
        for word in list:
            output2 += dict2.get(word, "NR")
        self.inp.text = output2
        self.dbl.text = ""
        print(f" In Morse '{str2}' in morse code '{output2}'")

    def add_user(self):
        con = sql.connect('m.db')
        cur = con.cursor()
        cur.execute(""" INSERT INTO id (inp,dbl) VALUES (?,?)""", (self.inp.text, self.dbl.text)
                )
        con.commit()
        con.close()

#class ScreenFour(Screen):
 #   pass

screen_manager= ScreenManager()

screen_manager.add_widget(ScreenOne(name="screen_one"))
screen_manager.add_widget(ScreenTwo(name="screen_two"))
screen_manager.add_widget(ScreenThree(name="screen_three"))
#screen_manager.add_widget(ScreenFour(name="screen_four"))




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

    def build(self):
        return screen_manager

sample_app=KivyApp()
sample_app.run()



