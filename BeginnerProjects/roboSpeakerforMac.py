import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker")
    while True:
        x = input("Enter what you want me to pronounce: ")
        if x == "q":
            break
        command = f"say {x}"
        os.system(command)
