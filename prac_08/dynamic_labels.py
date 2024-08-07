"""
Dynamic Labels - Prac 08
Estimated Time: 30 minutes
Actual Time: 20 minutes
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label


class DynamicLabelsApp(App):
    """App that Displays String and Number"""


def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.letter_to_number = {"A": 1, "B": 2, "C": 3, "D": 4}


def build(self):
    self.title = "Dynamic Label"
    self.root = Builder.load_file('dynamic_labels.kv')
    for key, value in self.letter_to_number.items():
        self.root.ids.main.add_widget(Label(text=f"{key} - {value}"))
    return self.root


DynamicLabelsApp().run()
