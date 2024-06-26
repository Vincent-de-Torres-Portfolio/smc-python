import pyttsx3

def say_hello_world():
    engine = pyttsx3.init()
    engine.say("Hello, World!")
    engine.runAndWait()

def main():
    say_hello_world()


main()
