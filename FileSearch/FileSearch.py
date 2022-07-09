import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import os
from datetime import datetime
import math
import xlsxwriter

# V3 fixes
# Added a folder path option to GUI choose where xlsx file gets saved (need to add a check for ending "\"  If added manually it breaks the path)
# Added a timestamp to avoid any writing errors if the current xlsx file is still open on someone's computer ( Timestamp takes time the script is STARTED )
# Fixed and made the Clear button functional
# Added a Default Button to GUI in case users wanted to undo the clear button

def set_defaults():
    now = datetime.now()
    year = now.strftime("%Y")
    month = now.strftime("%m")
    day = now.strftime("%d")
    time = now.strftime("_%H%M%S")
    today = year + month + day + time
    pathEntry.delete(0,"end")
    pathEntry.insert(0,r"\\pghetlprod03\Infa_Shared\Param")
    stringEntry.delete(0,"end")
    stringEntry.insert(0,"ODS_INFA_WRITE")
    savePathEntry.delete(0,"end")
    savePathEntry.insert(0,r"\\pghetlprod03\Infa_Shared\Python_Test")
    saveAsEntry.delete(0,"end")
    saveAsEntry.insert(0,"PythonSearchResult_" + today + ".xlsx")


def clear_fields():
    pathEntry.delete(0,"end")
    pathEntry.insert(0,"")
    stringEntry.delete(0,"end")
    stringEntry.insert(0,"")
    savePathEntry.delete(0,"end")
    savePathEntry.insert(0,"")
    saveAsEntry.delete(0,"end")
    saveAsEntry.insert(0,"")



def update_progress(perc):
    progress['value'] = perc
    root.update_idletasks()


def run_search():

    # clear the progress bar
    progress['value'] = 0
    root.update_idletasks()

    # confirm that the entered path is valid
    if os.path.exists(pathEntry.get()):

        search_path = pathEntry.get()
        search_str = stringEntry.get()
        # TODO paramaterize file_type
        file_type = ".PARM"

        count = 1
        xlsxname = saveAsEntry.get()
        filepath = savePathEntry.get()
        workbook = xlsxwriter.Workbook(fr"{filepath}\{xlsxname}")
        worksheet = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})
        searched_format = workbook.add_format()
        searched_format.set_bold()
        searched_format.set_font_color('red')
        return_format = workbook.add_format()
        return_format.set_font_size(8)

        # Creating headers and default output fields
        worksheet.write("A1", "Folder Path", bold)
        worksheet.write("B1", "File Name", bold)
        worksheet.write("C1", "Line Number", bold)

        worksheet.write("E3", f"Searched Path:", bold)
        worksheet.write("F3", search_path, searched_format)
        worksheet.write("E4", f"Searched String:", bold)
        worksheet.write("F4", search_str, searched_format)

        maxFolderLength = 0
        maxParamLength = 0

        # Repeat for each subfolder in the directory
        subfolders = [f.path for f in os.scandir(search_path) if f.is_dir()]

        # get a count of files that will need processed in order to calculate the progress bar
        fileTotalCount = 0    # running count for stats and progress bar
        folderTotalCount = 0    # running count for stats
        for foldername in subfolders:
            folderTotalCount += 1

            for filename in os.listdir(foldername):
                if filename.endswith(file_type):
                    fileTotalCount += 1

        fileCurrCount = 0

        # begin the search by looping through all subfolders in the given path
        for foldername in subfolders:

            # get the max length for use in the spreadsheet column width
            if len(foldername) > maxFolderLength:
                maxFolderLength = len(foldername)

            # Repeat for each file in the directory
            for filename in os.listdir(foldername):

                # Apply file type filter
                if filename.endswith(file_type):

                    # Open file for reading
                    fo = open(foldername + "\\" + filename)

                    # Read the first line from the file
                    line = fo.readline()

                    # Initialize counter for line number
                    line_no = 1

                    # Loop until EOF
                    while line != '':
                        # Search for string in line
                        index = line.upper().find(search_str.upper())

                        if index != -1:
                            # print('\nFolder path: ', foldername)
                            # print('File name: ', filename, " [Line: ", line_no, "] ", sep="")
                            count += 1
                            worksheet.write(f"A{count}", foldername, return_format)
                            worksheet.write(f"B{count}", filename, return_format)
                            worksheet.write(f"C{count}", line_no, return_format)

                            if len(filename) > maxParamLength:
                                maxParamLength = len(filename)

                        # Read next line
                        line = fo.readline()

                        # Increment line counter
                        line_no += 1

                    # increment count and update progress bar every 3 files
                    fileCurrCount += 1
                    if fileCurrCount % 3 == 0:  # if the current count is evenly divisible by 3
                        update_progress(math.floor((fileCurrCount / fileTotalCount*100)))

                    # Close the files
                    fo.close()

        worksheet.set_column('A:A', max(maxFolderLength + 2, 11))
        worksheet.set_column('B:B', max(maxParamLength + 2, 10))
        worksheet.set_column('C:C', 12)
        worksheet.set_column('D:D', 3)
        worksheet.set_column('E:E', 15)
        worksheet.set_column('F:F', max(len(search_path), len(search_str)) + 2)

        if count == 1:
            worksheet.write("A2", "Error: The search string did not match to any files within the path or subfolders. ")
            worksheet.write("A3", "Please check your search string and try again.")

        workbook.close()

        # show the progress bar at 100%
        update_progress(100)
        outputLabel.configure(text="The search has completed. " +
                              "\nTotal Folders Searched: " + str(folderTotalCount) +
                              "\nTotal Files Searched: " + str(fileTotalCount))

    else:
        outputLabel.configure(text="Error: The path you entered is not a valid path.\n Be sure to include \\\ at the start")



# get today's date to print as part of the suggested save as name
now = datetime.now()
year = now.strftime("%Y")
month = now.strftime("%m")
day = now.strftime("%d")
time = now.strftime("_%H%M%S")
today = year + month + day + time

root = tk.Tk()
root.title("File Search")

# create the backdrop
canvas = tk.Canvas(root, height=200, width=1000, bg="#263D42")
canvas.pack()

# create a frame that sits within the backdrop
main_frame = tk.Frame(canvas, bg="white")
main_frame.grid(row=0, column=0, sticky="nsew")
load_frame = tk.Frame(canvas, bg="white", pady=5)
load_frame.grid(row=1, column=0, sticky="nsew")
output_frame = tk.Frame(canvas, bg="white")
output_frame.grid(row=2, column=0, sticky="nsew")

# create various necessary parts
runButton = tk.Button(main_frame, text="Begin Search", padx=10, pady=5, fg="white", bg="#263D42", command=run_search)
clearButton = tk.Button(main_frame, text="Clear Entry Boxes", padx=10, pady=5, fg="white", bg="#263D42", command=clear_fields)
defaultButton = tk.Button(main_frame, text="Default Search", padx=10, pady=5, fg="white", bg="#263D42", command=set_defaults)

pathLabel = tk.Label(main_frame, width=21, text="Enter Search Path: ", padx=2, bg="gray", font=("Courier", 15), anchor="e")
pathEntry = tk.Entry(main_frame, width=60, bg="light gray", font=("Courier", 15))
pathEntry.insert(0, r"\\pghetlprod03\Infa_Shared\Param")

stringLabel = tk.Label(main_frame, width=21, text="Enter Search String: ", padx=2, bg="gray", font=("Courier", 15), anchor="e")
stringEntry = tk.Entry(main_frame, width=60, bg="light gray", font=("Courier", 15))
stringEntry.insert(0, "ODS_INFA_WRITE")

savePathLabel = tk.Label(main_frame, width=21, text="Save To Path: ", padx=2, bg="gray", font=("Courier", 15), anchor="e")
savePathEntry = tk.Entry(main_frame, width=60, bg="light gray", font=("Courier", 15))
savePathEntry.insert(0, r"\\pghetlprod03\Infa_Shared\Python_Test")

saveAsLabel = tk.Label(main_frame, width=21, text="Save Spreadsheet As: ", padx=2, bg="gray", font=("Courier", 15), anchor="e")
saveAsEntry = tk.Entry(main_frame, width=60, bg="light gray", font=("Courier", 15))
saveAsEntry.insert(0, "PythonSearchResult_" + today + ".xlsx")


# put the various parts on the screen
pathLabel.grid(row=0, column=0, padx=5, sticky='w')
pathEntry.grid(row=0, column=2)

stringLabel.grid(row=1, column=0, padx=5, sticky='w')
stringEntry.grid(row=1, column=2)

savePathLabel.grid(row=2, column=0, padx=5, sticky='w')
savePathEntry.grid(row=2, column=2)

saveAsLabel.grid(row=3, column=0, padx=5, sticky='w')
saveAsEntry.grid(row=3, column=2)

runButton.grid(row=10, column=0)
clearButton.grid(row=10, column=2)
defaultButton.grid(row=15, column=2)

outputLabel = tk.Label(output_frame, width=60, height=10, text="", padx=5, bg="light blue", font=("Courier", 10))
outputLabel.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")

progress = Progressbar(load_frame, orient=HORIZONTAL, length=800, mode='determinate')
progress.pack()


root.mainloop()
