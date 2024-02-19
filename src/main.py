from kivy.app import App
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.utils import get_color_from_hex

class ClockApp(App):
    pass

if __name__ == '__main__':
    Window.clearcolor = get_color_from_hex('#101216')
    LabelBase.register(name='Roboto',
                       fn_regular='fonts/Roboto-Thin.ttf',
                       fn_bold='fonts/Roboto-Medium.ttf')
    ClockApp().run()