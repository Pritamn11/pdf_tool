from pylovepdf.tools.merge import Merge
from pylovepdf.tools.split import Split
from pylovepdf.tools.unlock import Unlock
from pylovepdf.tools.imagetopdf import ImageToPdf
import json 
import sys
import os 

class pdftool:

    def __init__(self):
        self.api_key = self.read_api_key("creds.json")

    def read_api_key(self,file_name):
        with open(file_name,"r") as file:
            credintials = json.load(file)
            public_key = credintials.get('ILovePDF_API_KEY')
            if public_key:
                return public_key
            else:
                return ValueError("ILovePDF_API_KEY is not found in json file")


    def mergePdf(self, file_mappings):
        t = Merge(public_key=self.api_key ,proxies=None, verify_ssl=True)

        # two files needed 
        for file_path in file_mappings:
            t.add_file(file_path= file_path)

        t.debug = False
        t.set_output_folder('output_directory')
        t.execute()
        t.download()
        t.delete_current_task()
        return "PDF merge operation completed successfully"

    def splitPdf(self, pdf_file_path, fixed_range):
        t = Split(public_key=self.api_key, proxies=None, verify_ssl=True)
        t.add_file(pdf_file_path)
        t.debug = False
        t.split_mode = 'fixed_range'
        t.fixed_range = fixed_range
        t.set_output_folder('output_directory')

        t.execute()
        t.download()
        t.delete_current_task()
        return "PDF split operation completed successfully"

    def unlockPdf(self, file_path):
        t = Unlock(public_key=self.api_key, proxies=None, verify_ssl=True)
        t.add_file(file_path)
        t.debug = False
        t.set_output_folder('output_directory')

        t.execute()
        t.download()
        t.delete_current_task()
        return "PDF unlock operation completed successfully"
    
    def imagePdf(self, file_path):
        t = ImageToPdf(public_key= self.api_key, proxies=None, verify_ssl=True)
        t.add_file(file_path)
        t.debug = False
        t.orientation = 'portrait'
        t.margin = 0
        t.pagesize = 'fit'
        t.set_output_folder('output_directory')

        t.execute()
        t.download()
        t.delete_current_task()
        return "Image conversion to PDF opearation completed successfully"


pdf_tool = pdftool()

while True:
    print()
    print("Enter 1 for Merge pdf") 
    print("Enter 2 for split pdf") 
    print("Enter 3 for remove protected password from pdf") 
    print("Enter 4 for converting image to pdf") 
    print("Enter 0 for Exit ")
    choice = int(input("Enter Choice: "))
    print()

    if choice == 1:
        num_files = int(input("Enter the number of files to merge : "))
        file_mappings = []
        for i in range(num_files):
            file_path = input(f"Enter path of file {i+1} : ")
            file_mappings.append(file_path)
        result = pdf_tool.mergePdf(file_mappings)
        print(result)
        sys.exit()

    elif choice == 2:
        pdf_file_path = input("Enter the file path to split :")
        fixed_range = input("Enter the number of pages to split : ")
        result = pdf_tool.splitPdf(pdf_file_path, fixed_range)
        print(result)
        sys.exit()

    elif choice == 3:
        pdf_file_path = input("Enter the file path to remove protection password : ")
        result = pdf_tool.unlockPdf(pdf_file_path)
        print(result)
        sys.exit() 

    elif choice == 4:
        file_path = input("Enter file path to convert into pdf : ") 
        result = pdf_tool.imagePdf(file_path)   
        print(result)
        sys.exit()

    elif choice == 0:
        print("Program Exit Successfully")
        sys.exit()
        
    else:
        print("Enter correct choice")    
 