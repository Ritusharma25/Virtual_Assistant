import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import requests

def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening')


        r.pause_threshold = 0.5
        audio = r.listen(source)

        try:
            print("Recognizing")
            Query = r.recognize_google(audio, language='en-in')

            print("the command is printed=", Query)

        except Exception as e:
            print(e)
            print("Say that again sir")
            return "None"

        return Query


def speak(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[1].id)

    engine.say(audio)

    engine.runAndWait()


def tellDay():

    day = datetime.datetime.today().weekday() + 1

    Day_dict = {1: 'Monday', 2: 'Tuesday',
                3: 'Wednesday', 4: 'Thursday',
                5: 'Friday', 6: 'Saturday',
                7: 'Sunday'}

    if day in Day_dict.keys():
        day_of_the_week = Day_dict[day]
        print(day_of_the_week)
        speak("The day is " + day_of_the_week)


def tellTime():
    strTime = datetime.datetime.now().strftime("%H:%M:%S")
    speak(f"the time is {strTime}")


def Hello():
    speak("hello I am Zira your personal assistant, How may i help you?")


def Take_query():
    Hello()

    while (True):

        query = takeCommand().lower()
        if "wynk music" in query:
            speak("Opening wynk music ")
            webbrowser.open("https://wynk.in/music?gclid=CjwKCAiAm-2BBhANEiwAe7eyFDqe3aOX_V7OhWT25xQHdHn3gz5_7AyJH7ToC-IHS8pNFmE-4IqUjhoCu0wQAvD_BwE")
            continue
        elif "youtube" in query:
            speak("Opening Youtube ")
            webbrowser.open("www.youtube.com")
            continue
        elif "gmail" in query:
            speak("Opening Gmail ")
            webbrowser.open("www.gmail.com")
            continue
        elif "google" in query:
            speak("Opening Google")
            webbrowser.open("www.google.com")
            continue
        elif "which day it is" in query:
            speak("Today is ")
            tellDay()
            continue
        elif "time" in query:
            speak("The time is ")
            tellTime()
            continue
        elif 'search' in query:
            query =query.replace("search", "")
            speak(query)
            webbrowser.open_new_tab(query)
        elif "bye" in query:
            speak("Bye See You Soon")
            exit()

        elif "wikipedia" in query:
            speak("Checking the wikipedia ")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=4)
            speak("According to wikipedia")
            speak(result)
            webbrowser.open_new_tab(query)

        elif "weather" in query:
            api_key = "675203f27ae41842f75bd920ef3f58d2"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " + str(current_temperature) + "\n humidity in percentage is " + str(current_humidiy) +"\n description  " + str(weather_description))
                print(" Temperature in kelvin unit = " +str(current_temperature) +"\n humidity (in percentage) = " + str(current_humidiy) + "\n description = " + str(weather_description))

        elif "your name" in query:
            speak("I am Zira. Your Personal Assistant")

if __name__ == '__main__':
    Take_query()