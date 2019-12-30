if __name__ == '__main__':
    s = input()
    function_list = [str.isalnum,str.isalpha,str.isdigit,str.islower,str.isupper]
    for function in function_list:
        for char in s:
            if function(char) == True:
                print("True")
                break
        else:
                print("False")