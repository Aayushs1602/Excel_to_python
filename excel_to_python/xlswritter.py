import xlsxwriter
import wmi


def createfile():
    # Initializing the wmi constructor
    f = wmi.WMI()

    # Creating a list to store name and processes
    observations = []

    # Iterating through all the running processes
    for process in f.Win32_Process():

        # Adding the P_ID and P_Name of the process into a list
        observations.append((process.ProcessId, process.Name))

    # Creating a workbook
    workbook = xlsxwriter.Workbook('testing.xlsx')

    # Adding a worksheet
    worksheet = workbook.add_worksheet("apple")

    # Adding the header for the later columns
    worksheet.write("A1", "pid ")
    worksheet.write("B1", "Process name")

    # Adding the values in Excel file
    for i, j in zip(range(2, len(observations)), observations):
        worksheet.write("A"+str(i), observations[i][0])
        worksheet.write("B"+str(i), observations[i][1])

    # closing the workbook
    workbook.close()


createfile()
