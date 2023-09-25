import pyttsx3

if __name__ == '__main__':
    print("Welcome to RoboSpeaker, press q to exit the program ")
    while True:
        x = input("Enter what you want to speak \n")
        if x == "q":
            break
        engine = pyttsx3.init()
        engine.say(x)
        engine.runAndWait()
