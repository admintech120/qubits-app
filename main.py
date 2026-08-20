import webbrowser
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class QubitsApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        label = Label(
            text="Qubits.io Web Application", 
            font_size='20sp', 
            bold=True
        )
        
        btn = Button(
            text="Open Qubits.io", 
            font_size='18sp', 
            background_color=(0.3, 0.69, 0.31, 1),
            size_hint=(1, 0.3)
        )
        btn.bind(on_press=self.open_qubits)
        
        layout.add_widget(label)
        layout.add_widget(btn)
        return layout

    def open_qubits(self, instance):
        webbrowser.open("https://qubitsio.pythonanywhere.com/")

if __name__ == '__main__':
    QubitsApp().run()
