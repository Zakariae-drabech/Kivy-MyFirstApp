# application with one widget.

from kivy.app import App
# all widgets are in separate modules inside kivy.uix:
from kivy.uix.button import Button # button

class MyApp(App):
   # if the App class object has a build() method,
   # then run() will execute this method
   # and will display what "build" returns
   def build(self):
      btn = Button(text='This is a button')
      return btn # always returns a widget!

app = MyApp()
app.run() # the widget of the Button class will be shown
