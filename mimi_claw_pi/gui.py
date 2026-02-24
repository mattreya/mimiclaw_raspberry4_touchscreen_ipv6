import os
import json
import time
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

class MimiClawGUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.alert_label = Label(text="Hello! I'm MimiClaw. Waiting for alerts...", font_size='24sp')
        self.add_widget(self.alert_label)
        self.action_button = Button(text="Dismiss", size_hint=(1, 0.2), opacity=0)
        self.action_button.bind(on_release=self.dismiss_alert)
        self.add_widget(self.action_button)
        # Check for new alerts every 1 second
        Clock.schedule_interval(self.check_alerts, 1.0)

    def check_alerts(self, dt):
        alert_file = 'mimi_claw_pi/ui/latest_alert.json'
        if os.path.exists(alert_file):
            with open(alert_file, 'r') as f:
                data = json.load(f)
                self.alert_label.text = data.get('message', "New message!")
                self.action_button.opacity = 1
                self.action_button.text = data.get('action', "OK")

    def dismiss_alert(self, instance):
        self.alert_label.text = "Listening..."
        self.action_button.opacity = 0
        alert_file = 'mimi_claw_pi/ui/latest_alert.json'
        if os.path.exists(alert_file):
            os.remove(alert_file)

class MimiClawApp(App):
    def build(self):
        return MimiClawGUI()

if __name__ == '__main__':
    MimiClawApp().run()
