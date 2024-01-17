"""Process Data V0.1
This is a script for generating .json files out of the taxes statistics which
are given by the government in form of excel-files.
"""



#Imports----------------------------------------------------------------------
import pandas as pd



#Run main program-------------------------------------------------------------
def main():
    
    excelSheet : pd.DataFrame = pd.read_excel("sources/ktn_zh.xlsx")
    
    print(excelSheet)



if __name__ == "__main__":
    main()