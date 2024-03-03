import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.config import Config
kivy.config.Config.set('graphics','resizable',True)


class RandomNumber(App):
    def build(self):
        Window.size=(400,600)
        return Label(text='Random Number Generator')


randomApp=RandomNumber()
randomApp.run()