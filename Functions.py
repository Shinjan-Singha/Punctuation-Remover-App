Punctuations = ".?!,;:—-()""[]''{}'\/@#&*<>"
FILEPATH = "Data.txt"

def PuncPop(local_user_input:str):

    """This Function checks every letter of the input and, whenever a letter
    is matched with punctuation marks, the punctuation mark
    from the input is removed, and the result is returned"""

    for item in local_user_input:
        if item in Punctuations:
            local_user_input = local_user_input.replace(item,"")

    local_result = local_user_input
    return local_result


def PuncFilePop(filepath=FILEPATH):

    """This Function checks every letter of the file and, whenever a letter
    is matched with punctuation marks, the punctuation mark
    from the file is removed, and the file is updated with no punctuation marks"""

    with open(filepath,'r') as file:     # First Part Of The Function
        data = file.read()
    for item in data:
        if item in Punctuations:
            data = data.replace(item,"")

    local_result = data
    
    with open(filepath,"w") as file:    # Second Part Of The Function
        file.write(local_result)

