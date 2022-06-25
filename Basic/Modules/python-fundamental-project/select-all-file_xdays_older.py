
from datetime import datetime
from logging import exception
import sys, os

def checkFileLessThanXdays(file_path):
    """_summary_
      this function checks all file less than xdays ad delete
      parameter: 1(str) description
      file_path: requires directory path.
      variables:[]
      return None
    """
    age = 3
    try:
        if not os.path.exists(file_path):
            print("please provide a valid path")
        if os.path.isfile(file_path):
            print("ooops you just provided a file please provide directory path.!")
        for each_file in os.listdir(file_path):
            result = os.path.join(file_path, each_file)
            if os.path.isfile(result):
                time_stamp = datetime.fromtimestamp
                file_creation_date = time_stamp(result.os.path.getctime(result))
                if file_creation_date.day > age:
                  print(f"{result},created {file_creation_date.day} days ago")
                #rint(each_file)
    except Exception as e:
        print(e)
    return None


file_path = input("enter directory path:")
checkFileLessThanXdays(file_path)