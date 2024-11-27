#Create a program that ask user for personal information. Minimum of 5 information per person, more info the better. eg. Fullname, Address, etc. Write the collected information in a txt file. It's up to you on how you'd like to format the information in the file. The program should ask user if want to input another person or exit.

amount_of_inputs = []

while len(amount_of_inputs) < 5:

    name_info_inputs = input("Please put in you're full name: ")
    amount_of_inputs.append(name_info_inputs)
    address_info_inputs = input("Please put in you're address: ")
    amount_of_inputs.append(address_info_inputs)
    phone_number_info_inputs = input("Please put in you're phone number: ")
    amount_of_inputs.append(phone_number_info_inputs)
    marital_status_info_inputs = input(bool("Please put m for married, s for single, u for rather not say: "))
    amount_of_inputs.append(marital_status_info_inputs)
    gender_info_inputs = input("Please put in you're g for girl, b for boy, and u for rather not say: ")
    amount_of_inputs.append(gender_info_inputs)
