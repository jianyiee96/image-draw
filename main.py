import os
import welcome
import draw

def main():
    while True:
        os.system("cls")
        print(welcome.welcome("IMAGE-DRAW"))
        print("\nChoose the mode that you want to use : ")
        print("""
            1 : Basic draw image
            0 : Exit"""
        )
        choice = input("\nEnter your choice : ")
        if choice == '0':
            print("Bye")
            exit()
        elif choice == '1':
            draw.basic_draw()
            print("Bye")
            exit()


        os.system("cls")

if __name__ == "__main__":
    main()