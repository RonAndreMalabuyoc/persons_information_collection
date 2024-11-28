#Create a program that ask user for personal information. Minimum of 5 information per person, more info the better. eg. Fullname, Address, etc. Write the collected information in a txt file. It's up to you on how you'd like to format the information in the file. The program should ask user if want to input another person or exit.
def collect_information():

    persons_information = {
        "Full name": input("Please put in you're full name: ").strip(),
        "Full address": input("Please put in you're address: ").strip(),
        "Phone number": input("Please put in you're phone number: ").strip(),
        "Email_address": input("Please put your email address: ").strip(),
        "Date of birth": input("Please put in you're date of birth: ").strip(),
}
    return persons_information

def write_to_file(file_name, data):
    with open(file_name, 'a') as file:
        for key, value in data.items():
            file.write(f"{key}: {value}\n")
        file.write("\n")  

def main():
    file_name = "writable.txt"  
    user_info = collect_information() 
    write_to_file(file_name, user_info)  
    print(f"Information saved to {file_name}!")

if __name__ == "__main__":
    main()