import datetime
import os
import speech_recognition as sr
import win32com.client
import webbrowser
import openai

# Initialize the speaker
speaker = win32com.client.Dispatch("SAPI.SpVoice")

def say(s):
    speaker.Speak(s)

import random
def ai(prompt):
    #openai.api_key = "api_key"
    text = f"OpenAI response for {prompt}\n **************\n"
    response = openai.Completion.create(
        model="gpt-3.5-turbo-instruct",
        prompt=prompt,
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if os.path.exists("OpenAi"):
        os.mkdir("OpenAi")
    with open(f"OpenAi/prompt- {random.randint(1, 9999)}", "w") as f:
        f.write(text)
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        print("Listening...")
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()
        except Exception as e:
            print("Some Error Occurred: ", e)
            return "none"

if __name__ == "__main__":
    say("Hii...")
    while True:

        query = takeCommand()
        if query == "none":
            continue
        if "open youtube" in query:
            say("Opening YouTube sir...")
            webbrowser.open("https://youtube.com")
        elif "open music" in query:
            musicPath = "C:/Users/DELL/Music/Music/bling.mp4"
            os.startfile(musicPath)
        elif "the time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M")
            say(f"Sir the time is {strfTime}")
        elif "open camera" in query:
            os.system("start microsoft.windows.camera:")


        elif "using artificial intelligence" in query.lower():

            say("What would you like to do using artificial intelligence?")

            prompt = takeCommand()

            ai(prompt=prompt)

        else:
            say(f"{query}")
