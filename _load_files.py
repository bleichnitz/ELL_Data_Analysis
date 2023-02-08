import openpyxl as openpyxl
import warnings as warnings


def load_file(file_name):
    """ Load data from an Excel file. NOTE: the load typically throws this error "UserWarning: Data Validation
    extension is not supported and will be removed warn(msg)", as openpyxl does not support data validation
    (see dropdown OLG and SC columns on 'Tracking Sheet') but should NOT affect overall functioning of this program.
    The 'warnings' module removes the warning from printing in the turn terminal to minimize confusion.
    """
    warnings.simplefilter(action='ignore', category=UserWarning)
    print("")
    print("File <" + str(file_name) + "> has loaded successfully.")

    return openpyxl.load_workbook(file_name, data_only=True)
