from kivy.app import App
from kivy.uix.label import Label

class ElonApp(App):
    def build(self):
        return Label(text="Hello, Elon App Working!")

ElonApp().run()
