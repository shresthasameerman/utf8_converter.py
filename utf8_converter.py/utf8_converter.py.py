from unittest import result


def validate_input(user_input):
    try: 
        int_value=int(user_input)
        if 32 <= int_value <=126:
            return True,int_value
        else:
            return False, f"\u001b[the entered value is out of range. Please enter a value between 32 and 126.\u001b[0m]]"
    except ValueError:
        return False, f"\u001b[31mPlease enter a valid number.\u001b[0m"
def get_user_input():
    while True:
        user_input = input("enter a UTF-8 value between 32 and 126:")
        is_valid,result = validate_input(user_input)
        if is_valid:
            return result
        else:
            print(result)
def display_character(int_value):
    print(f"\u001b[32mThe corresponding character is: {chr(int_value)}\u001b[0m")
def main(): 
    int_value=get_user_input()
    display_character(int_value)
if __name__=="__main__":
    main()
            
