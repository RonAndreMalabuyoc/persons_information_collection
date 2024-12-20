def collect_information():
    return {
        "Full name": input("Please put in your full name: ").strip(),
        "Address": input("Please put in your address: ").strip(),
        "Phone number": input("Please put in your phone number: ").strip(),
        "Email address": input("Please put your email address: ").strip(),
        "Date of birth": input("Please put in your date of birth: ").strip(),
    }

def write_to_file(file_name, data):
    try:
        with open(file_name, "a") as file:
            for key, value in data.items():
                file.write(f"{key}: {value}\n")
            file.write("-" * 40 + "\n")
    except Exception as e:
        print(f"Error: {e}")

def main():
    file_name = "writable.txt"
    while True:
        user_info = collect_information()
        write_to_file(file_name, user_info)
        print(f"Information saved to {file_name}!")

        new_person = input("Will you input a new person (yes/no): ").strip()
        if new_person != "yes":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()