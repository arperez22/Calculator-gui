from logic import *

def main():
    window = Tk()
    window.title('Calculator')
    window.geometry('450x450')
    window.resizable(False, False)

    Logic(window)

    window.mainloop()

if __name__ == '__main__':
    main()