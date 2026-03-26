from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=50, spacing=20)
        label = Label(text='智农慧眼', font_size='40sp')
        btn = Button(text='点我测试', font_size='30sp')
        
        def on_press(instance):
            label.text = '打包成功！'
        
        btn.bind(on_press=on_press)
        layout.add_widget(label)
        layout.add_widget(btn)
        return layout

if __name__ == '__main__':
    MyApp().run()
