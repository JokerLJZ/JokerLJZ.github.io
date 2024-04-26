import os
import pandas as pd

def TransXlsToXlsx(path=os.getcwd(), remove=True):
    """
    def TransXlsToXlsx(path=os.getcwd(), remove=True):
        Transform all xls file to xlsx format in the path.

    parameters:

    path: 
        The path where all xls file will be tansform;
        Default is the current path
    remove: 
        If True will remove the xls file after transform.
        Default is True
    """
    if path[-2: 0] != "\\": path += "\\"

    for f in os.listdir(path):
        file_name, suff = os.path.splitext(f)
        if suff == ".xls":
            data = pd.DataFrame(
                pd.read_excel(path + f)) # Read the xls file
            # data = ILLEGAL_CHARACTERS_RE.sub(r'', data)
            data.to_excel(
                path
                + file_name
                + '.xlsx',
                index = False,
                engine='openpyxl') # Transform xls to xlsx
            if remove:
                os.remove(path + f) # Delete the xls file
            else:
                pass


if __name__ == "__main__":
    path = os.getcwd() + '/Original/'
    TransXlsToXlsx(path)