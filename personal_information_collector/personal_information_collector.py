#Create a program that ask user for personal information. Minimum of 5 information per person, more info the better. eg. Fullname, Address, etc. Write the collected information in a txt file. It's up to you on how you'd like to format the information in the file. The program should ask user if want to input another person or exit.

personal_info = {

    "name_info_inputs": input("Please put in you're full name: "),
    "address_info_inputs": input("Please put in you're address: "),
    "phone_number_info_inputs": input("Please put in you're phone number: "),
    "marital_status_info_inputs": input("Please put m for married, s for single, u for rather not say: "),
    "gender_info_inputs": input("Please put in you're g for girl, b for boy, and u for rather not say: "),

}
    
print(personal_info)