from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget
from kivy.uix.floatlayout import FloatLayout
import requests
from bs4 import BeautifulSoup
from kivy.uix.scrollview import ScrollView

layout = FloatLayout()

def process():
    text1 = TextInput(multiline=False, size_hint=(0.2,0.05),pos_hint={'x':0.1, 'y':0.85})
    text2 = TextInput(multiline=False, size_hint=(0.2,0.05),pos_hint={'x':0.1, 'y':0.65})
    text3 = TextInput(font_size=15, size_hint=(0.6,1),pos_hint={'x':0.4, 'y':0.0})
    label1 = Label(font_size=30, color=(0.3,0.6,0.7,1), size_hint=(0.0002, 0.7), pos_hint={'x':0.2 , 'y':0.6}, text= "Song Name")
    label2 = Label(font_size=30, color=(0.3,0.6,0.7,1), size_hint=(0.0002, 0.7), pos_hint={'x':0.2 , 'y':0.4}, text= "Artist Name")
    layout.add_widget(text1)
    layout.add_widget(text2)
    layout.add_widget(label1)
    layout.add_widget(label2)

    def pressed(instance):
        try:
            process()

            song = text1.text
            artist = text2.text
            song = song.replace(' ', '-')
            artist = artist.replace(' ', '-')
            artist = str.casefold(artist)
            song = str.casefold(song)

            url = ('https://www.lyricfinder.org/lyrics/'+ artist +'?track='+ song)

            a = requests.get(url)
            soup = BeautifulSoup(a.content, 'html.parser')
            lyrics = soup.find(class_='col-lg-6')
            d = lyrics.get_text()
            layout.add_widget(text3)
            text3.text = d

        except:
            layout.add_widget(text3)
            text3.text = 'Check Spelling or Lyrics Not Available'


    button = Button(text='Submit' , font_size=40, color=(0.3,0.6,0.7,1), size_hint=(0.2, 0.1), pos_hint={'x':0.1, 'y':0.4})
    layout.add_widget(button)
    button.bind(on_press=pressed)

process()




class MyApp(App):
    def build(self):
        return layout
if __name__ == '__main__':
    MyApp().run()