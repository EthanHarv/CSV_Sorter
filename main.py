'''
Program for sorting CSV files (by first column, numerical) - Final Project (1) for UNO CSCI-1620

Author: Ethan Harvey
'''

from tkinter import Tk
from gui import GUI

def main():
    '''
    Window setup & program entry point
    '''
    window = Tk()
    window.title('CSV Sorter')
    window.geometry('600x275')
    window.minsize(375, 275)
    window.resizable(True, False)

    # Add widgets
    GUI(window)

    window.mainloop()


if __name__ == '__main__':
    main()
