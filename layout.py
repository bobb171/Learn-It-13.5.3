# ==========================================
# LEARN IT 13.5.2: THE GODLY EDITION
# layout.py - THE AESTHETIC FRONTEND
# ==========================================

import os
import random
import json
import engine  # <--- THE MAGIC ENGINE CONNECTION

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, NumericProperty, DictProperty, ListProperty
from kivy.core.window import Window

# --- SECTION 1: THE UI DESIGN (KV) ---
KV = '''
<MenuButton@Button>:
    font_size: '18sp'
    background_normal: ''
    background_color: (0, 0, 0, 0)
    color: (1, 0.84, 0, 1)
    canvas.before:
        Color:
            rgba: (0, 0.7, 0.3, 1) if self.state == 'normal' else (1, 0.84, 0, 0.5)
        RoundedRectangle:
            pos: self.pos
            size: self.size
            radius: [15,]
        Line:
            width: 2
            rounded_rectangle: (self.x, self.y, self.width, self.height, 15)

WindowManager:
    LoginScreen:
    MainDashboard:

<LoginScreen>:
    name: 'login'
    canvas.before:
        Color:
            rgba: (0.01, 0.01, 0.03, 1)
        Rectangle:
            pos: self.pos
            size: self.size
    BoxLayout:
        orientation: 'vertical'
        padding: 60
        spacing: 30
        Label:
            text: "LEARN IT: GODLY"
            font_size: '42sp'
            bold: True
            color: (1, 0.84, 0, 1)
        TextInput:
            id: pass_key
            hint_text: "Admin Code"
            password: True
            size_hint_y: None
            height: '60dp'
        Button:
            text: "INITIALIZE SYSTEM"
            size_hint_y: None
            height: '70dp'
            background_color: (0, 0.6, 0.4, 1)
            on_release: root.verify_admin(pass_key.text)

<MainDashboard>:
    name: 'dash'
    Label:
        text: "WELCOME TO THE VAULT"
'''

# --- SECTION 2: THE SCREEN LOGIC ---

class LoginScreen(Screen):
    def verify_admin(self, code):
        app = App.get_running_app()
        if code == "qwerty":
            app.user_tier = "Admin"
            self.manager.current = 'dash'
        else:
            self.manager.current = 'dash'

class MainDashboard(Screen):
    pass

class WindowManager(ScreenManager):
    pass

# --- SECTION 3: THE APP ENGINE ---

class LearnItApp(App):
    user_tier = StringProperty("Demo")
    user_level = NumericProperty(1)
    user_xp = NumericProperty(0)
    
    def build(self):
        Window.size = (360, 640)
        # CALLING THE WAREHOUSE
        try:
            self.db = engine.GlobalData()
            print("✅ Engine Connected Successfully")
        except Exception as e:
            print(f"❌ Engine Connection Failed: {e}")
            
        return Builder.load_string(KV)

if __name__ == "__main__":
    LearnItApp().run()
