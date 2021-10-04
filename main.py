import time
import winsound
import pyttsx3

def main():
    engine = pyttsx3.init()
    while True:
        TWENTY_FIVE = 1500
        FIVE = 300

        totalTime = 0

        print('\nTime to get to work\n')
        engine.say("Time to get to work")
        engine.runAndWait()
        winsound.Beep(150, 1000)
        while totalTime != TWENTY_FIVE:
            time.sleep(1)
            totalTime += 1
            print(totalTime, end='\r', flush=True)

        totalTime = 0

        print('\nTake a quick break\n')
        engine.say("Take a quick break")
        engine.runAndWait()
        winsound.Beep(150, 1000)
        while totalTime != FIVE:
            time.sleep(1)
            totalTime += 1
            print(totalTime, end='\r', flush=True)


if __name__ == '__main__':
    main()