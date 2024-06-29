from pathlib import Path
import re

def total_salary(path):
    try:
        # Opening file, using utf-8 encoding
        with open(path, encoding='utf-8') as sfile:
            salary_separate = [
                # Every line in the file is cleared of characters up to first comma,
                # stripped of new line characters
                # and comverted to integer
                int(re.sub('^.*?,', '', sal).strip()) for sal in sfile.readlines()
            ]
            
            # Calculating sum of all list items
            total_s = sum(salary_separate)

            # Calcuating average of all list items, using length of the list and cheking that list is not empty
            average_s = total_s / len(salary_separate) if salary_separate else 0
            return( total_s, average_s)
            
    # Messages to users in case of exeptions
    except FileNotFoundError:
        print(f'File {path} not found!')
    except Exception as exeptn:
        print(f'There is a problem with your file. Error: {exeptn}')


# Example
total, average = total_salary("salaries.txt")
print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
