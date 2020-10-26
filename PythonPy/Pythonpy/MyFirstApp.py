from kivy.app import App
from kivy.uix.button import Button

class Myapp(App):
  def build(self):
   B=Button(text='Press the button!')
   return B
Myapp().run()

