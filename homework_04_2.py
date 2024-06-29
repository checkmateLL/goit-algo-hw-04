def get_cats_info(path):
    try:

        # Creating empty list
        full_cat_list = []

        # Opening file, using utf-8 encoding
        with open(path, encoding='utf-8') as ct:
            for line in ct:                
                # Splitting lines with comma and deleting potential empty spaces and new line symbols
                parts = line.strip().split(',')
                # Creating dictionary and adding cat info there
                cat_dict = {
                    "id": parts[0],
                    "name": parts[1],
                    "age": parts[2]
                }

                full_cat_list.append(cat_dict)

        return full_cat_list
                        
    # Messages to users in case of exeptions
    except FileNotFoundError:
        print(f'File {path} not found!')
    except Exception as exeptn:
        print(f'There is a problem with your file. Error: {exeptn}')


# Example

cats_info = get_cats_info('cat_info.txt')
print(cats_info)
