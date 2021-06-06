from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.properties import NumericProperty, ObjectProperty, StringProperty
import json


class TwoScalesWidget(BoxLayout):
    '''
    Two donut style gauges showing values from a json file.

    Attributes:
    The attributes are bound by name to propertis in the kv file. Updating them will automatically update the displayed data in the visualisation

        num1 (NumericProperty, float):
            Angle of the first donut style gauge. Calculated from the actual value val1 and the limits.
            Initially set to 150.
        num2 (NumericProperty, float):
            Angle of the second donut style gauge. Calculated from the actual value val2 and the limits.
            Initially set to 150.
        val1 (StringProperty, str):
            Value of the first donut style gauge.
        val2 (StringProperty, str):
            Value of the second donut style gauge.
        val3 (StringProperty, str):
            Copntains the time code of the measurement.
        unit1 (StringProperty, str):
            Unit of val1. Initially set to °C
        unit2 (StringProperty, str):
            Unit of val2. Initially set to %rH
    '''
    num1 = NumericProperty(150)
    num2 = NumericProperty(150)
    val1 = StringProperty('--')
    val2 = StringProperty('--')
    val3 = StringProperty('--')
    unit1= StringProperty('°C')
    unit2= StringProperty('%rH')

    def show_data(self, filename, low1, high1, low2, high2):
        '''Reads limits for the settings and values from a json file and updates the bound properties of the class.

        The data is read from a json file. The data needs to be stored in the file as a dict which contains the following keys:
        - temperature
        - humidity
        - time_code

        Args:
            filename (str): Path to the file which contains the data to display.
                            Path needs to be an absolute path.

        Returns:
            Nothing.
        '''
     
        #opens a json file and reads temperature and humidity
        with open(filename, 'r') as read_file:
            data=json.load(read_file)
            self.val1 = str(data['temperature'])
            self.val2 = str(data['humidity'])
            self.val3 = data['time_code']
            self.num1 = self.fit_to_scale(data['temperature'], low1, high1)
            self.num2 = self.fit_to_scale(data['humidity'], low2, high2)

    def fit_to_scale(self, value, minimum, maximum):
        '''scales the given value between the set max and min limits into an angle for the doughnut style gauge.

        Args:
            value (float): Value that shall be scaled.
            minimum (float): Minimum for scaling.
            maximum (float): Maximum for scaling.

        Returns:
            (float): Scaled value.
        '''
        return ((value - minimum) / (maximum - minimum) * 300) - 150

class TwoScalesTestLayout(BoxLayout):
    pass

class TwoScalesWidgetApp(App):
    def build(self):
        return TwoScalesTestLayout()

if __name__ == '__main__':
    TwoScalesWidgetApp().run()
