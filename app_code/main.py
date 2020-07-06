from kivy.app import App
from kivymd.theming import ThemeManager


# The main application itself
class mainApp(App):
    theme_cls = ThemeManager()
    pass

# Running the function mainApp()
mainApp().run() 