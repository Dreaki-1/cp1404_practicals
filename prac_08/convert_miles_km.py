"""
Prac 08 - Convert miles to km
Estimate Time: 15 minutes
Actual Time: 25 minutes
It still doesn't work fully and I cant figure out why
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty

MILES_IN_KM = 1.60934


class Convert_Miles_To_Km(App):
    """App that converts miles to kilometres"""
    output_in_km = StringProperty()

    def build(self):
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def calculate(self, text):
        """Calculate miles to kilometres then updates output_in_km"""
        miles = self.convert_str_to_float(text)
        self.update_result(miles)

    @staticmethod
    def convert_str_to_float(miles):
        try:
            return float(miles)
        except ValueError:
            return 0

    def update_result(self, miles):
        self.output_in_km = str(miles * MILES_IN_KM)

    def adjust_input(self, text, change):
        miles = self.convert_str_to_float(text) + change
        self.root.ids.input_box.text = str(miles)


Convert_Miles_To_Km().run()
