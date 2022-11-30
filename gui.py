'''
GUI Code
'''

import tkinter as tk
from tkinter import Frame, Label, Button
from tkinter import filedialog as fd

from csv_helper import read_csv, sort_csv, write_csv

class GUI:
    '''
    Class for GUI initalization and methods
    '''

    def __init__(self, window) -> None:

        ### Variables

        self.filename_in = None
        self.filename_out = None
        self.rows = None

        ### Widget Setup

        self.window = window

        # Input filename label & button
        self.frame_file_in = Frame(self.window)
        self.label_file_in = Label(self.frame_file_in, text='Input File:')
        self.entry_file_in = Button(self.frame_file_in, text='Select File', width=34, command=self.select_file_in)
        self.label_file_in.pack(padx=5, side='left')
        self.entry_file_in.pack(padx=25, side='left')
        self.frame_file_in.pack(anchor='w', pady=10)

        # Selected input file labels
        self.frame_filename_in = Frame(self.window)
        self.label_input_file = Label(self.frame_filename_in, text="Selected File:")
        self.label_input_file.pack(padx=5, side='left')
        self.label_filename_in = Label(self.frame_filename_in, text="No file selected")
        self.label_filename_in.pack(padx=7, side='left')
        self.frame_filename_in.pack(anchor='w')

        # Output filename label & button
        self.frame_file_out = Frame(self.window)
        self.label_file_out = Label(self.frame_file_out, text='Output File:')
        self.entry_file_out = Button(self.frame_file_out, text='Select File', width=34, command=self.select_file_out)
        self.label_file_out.pack(padx=5, side='left')
        self.entry_file_out.pack(padx=15, side='left')
        self.frame_file_out.pack(anchor='w', pady=10)

        # Selected output file labels
        self.frame_filename_out = Frame(self.window)
        self.label_output_file = Label(self.frame_filename_out, text="Selected File:")
        self.label_output_file.pack(padx=5, side='left')
        self.label_filename_out = Label(self.frame_filename_out, text="No file selected")
        self.label_filename_out.pack(padx=7, side='left')
        self.frame_filename_out.pack(anchor='w')

        # Result text
        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result) # No initial text
        self.label_result.pack(padx=20, side='left')
        self.frame_result.pack(pady=20)

        # "Sort" button
        self.frame_button = Frame(self.window)
        self.button_compute = Button(self.frame_button, text='Sort!', width=25, command=self.sort)
        self.button_compute.pack(pady=20)
        self.frame_button.pack(side=tk.BOTTOM)

    def select_file_in(self) -> None:
        '''
        Opens a file dialog to get input filename and sets self.filename_in as the result
        '''
        self.filename_in = fd.askopenfilename(title='Open a file', initialdir='.', filetypes=(('CSV Files', '*.csv'),))
        if self.filename_in == '':
            self.filename_in = None
            return
        self.label_filename_in.config(text=self.filename_in)

    def select_file_out(self) -> None:
        '''
        Opens a file dialog to get output filename and sets self.filename_out as the result
        '''
        self.filename_out = fd.asksaveasfilename(title='Save file', initialdir='.', filetypes=(('CSV Files', '*.csv'),))
        # Ensure extension is used
        if self.filename_out == '':
            self.filename_out = None
            return
        if not self.filename_out.endswith('.csv'):
            self.filename_out = self.filename_out + ".csv"
        self.label_filename_out.config(text=self.filename_out)

    def sort(self) -> None:
        '''
        Sorts the currently selected CSV file
        '''

        # Validate input
        if self.filename_in is None:
            self.label_result.config(text="Please select an input file.")
            return

        if self.filename_out is None:
            self.label_result.config(text="Please select an output file.")
            return

        # Read
        try:
            rows_in = read_csv(self.filename_in)
        except FileNotFoundError:
            self.label_result.config(text="Input file not found.")
            return
        except PermissionError:
            self.label_result.config(text="Unable to read input file, lacking permissions.")
            return

        # Sort
        try:
            sorted_rows = sort_csv(rows_in)
        except ValueError:
            self.label_result.config(text="Unable to sort data, first column is not numeric.")
            return

        # Write
        try:
            write_csv(self.filename_out, sorted_rows)
        except PermissionError:
            self.label_result.config(text="Unable to write output file, lacking permissions.")
            return


        self.label_result.config(text=f"Success! Wrote sorted csv to {self.filename_out}")
        self.filename_in = None
        self.filename_out = None
        self.label_filename_in.config(text="No file selected")
        self.label_filename_out.config(text="No file selected")
