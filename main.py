import time
import winsound

def main():
    while True:
        totalTime = 0
        TWENTY_FIVE = 1500
        FIVE = 300


        print('\nTime to get to work')
        winsound.Beep(150, 1000)
        while totalTime != TWENTY_FIVE:
            time.sleep(1)
            totalTime += 1
            print(totalTime, end='\r', flush=True)

        print('\nTake a quick break\n')
        winsound.Beep(150, 1000)
        totalTime = 0
        while totalTime != FIVE:
            time.sleep(1)
            totalTime += 1
            print(totalTime, end='\r', flush=True)


if __name__ == '__main__':
    main()