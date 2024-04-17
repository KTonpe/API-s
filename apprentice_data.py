import json
import random



def get_data():
    apperentice_file_path ='Apprentices.json'
    with open(apperentice_file_path, 'r') as f:
        details = json.load(f)
    return details

def shuffle_keys():
    #To shuffle the keys
    keys = list(data["Apprentices"].keys())
    random.shuffle(keys)
    # print(keys)
    shuffled_dict = {key: data["Apprentices"][key] for key in keys}
    print(shuffled_dict)

# print(data["Apprentices"])



#To print the names of people in Hyderabad only
def display_data_of_hyd():
    #hyd = data["Apprentices"]["Hyderabad"]
    for members in data["Apprentices"]["Hyderabad"]:
        print(members["name"])

def display_genral_details(member):
    print("Name:", member["name"])
    print("Employee ID:", member["employee_id"])
    print("Email:", member["email"])
    print("Contact:", member["contact"])
    print()
def search_name_from_data(name):
    for location, members in data["Apprentices"].items():
        for member in members:
            if name == member["name"]:
                print(f'{name} works at {location}')
                display_genral_details(member)
                # else: print('Not fnd')

def get_employee_details():
    new_member_name = input('Enter a name of new employee: ').lower()
    email_list = new_member_name.strip().split()
    email = f'{email_list[0]}.{email_list[1]}@jda.com'
    employee_id = (input('Enter employee ID: '))
    contact = input('Enter a contact of new employee: ')
    while len(contact) != 10:
        contact = input('Enter a 10 digit contact number of new employee: ')
        if len(contact) != 10:
            contact = input('Please enter a 10 digit contact number of new employee: ')

    new_member = {
    "name": new_member_name,
    "employee_id": employee_id,
    "email": email,
    "contact": contact }
    return new_member

def update_data(data,place):
        new_member = get_employee_details()
        data["Apprentices"][place].append(new_member)
        updated_json_data = json.dumps(data, indent=4)
        return updated_json_data

def write_to_file(updated_json_data):
    with open('Apprentices.json', 'w') as file:
        file.write(updated_json_data)


if __name__ == "__main__":
    
    data = get_data()
    # print(data)
    # name_of_apprentice = input("Enter name of apprentice: ").lower()
    # search_name_from_data(name_of_apprentice)
    # print(update_data())

    place = input('Enter a place to a new employee: ').lower()
    while place not in data["Apprentices"].keys():
        place =input(f'Enter a valid location from {data["Apprentices"].keys()} : ').lower()
        if place not in data["Apprentices"].keys():
            place = input((f'Enter a valid location from {data["Apprentices"].keys()} : '))



    updated_json_data = update_data(data,place)
    write_to_file(updated_json_data)
 

