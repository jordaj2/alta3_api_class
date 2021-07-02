import requests
from flask import jsonify

URL = 'http://10.222.3.122:2224/addrec'

def add_student(data):
    r = requests.post(URL, data)

def main():
    is_active = True
    while is_active:
        nm = input("Enter the student's name: ")
        addr = input("Enter the student's address: ")
        city = input("Enter the student's city:  ")
        pin = input("Enter student's PIN: ")

        # make dictionary
        student = {'nm': nm, 'addr': addr, 'city': city, 'pin': pin}

        try:
            add_student(jsonify(student))
        except Exception as e:
            print(f"Error occurred adding student {nm}\n Error Code: {e}")
        finally:
            choice = input("\nWould you like to enter another student?[y/n]  ")
            if choice.lower() == 'n':
                is_active = False






if __name__ == "__main__":
    main()

