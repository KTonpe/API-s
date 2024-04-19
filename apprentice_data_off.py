import json
import string
import random

def get_data():
    apperentice_file_path ='Apprentices.json'
    with open(apperentice_file_path, 'r') as f:
        details = json.load(f)
    # print(json.dumps(details, indent=4))
    return details

data = get_data()

def display_all_data():
    with open("Apprentices.json", 'r') as f:
        data = json.load(f)
    print(json.dumps(data, indent=4))
    

def display_name_of_apperentice_of_location():
    #hyd = data["Apprentices"]["Hyderabad"]

    location_user = input(f"Please enter location only from {list(data['Apprentices'].keys())} : ").lower()
    while location_user not in data["Apprentices"].keys():
        location_user =input(f'Enter a valid location from {data["Apprentices"].keys()} : ').lower()
        continue
    else:
        for members in data["Apprentices"][location_user]:
            print(members["name"])

def display_genral_details(member):
    print("Name:", member["name"])
    print("Employee ID:", member["employee_id"])
    print("Email:", member["email"])
    print("Contact:", member["contact"])
    print()


def details_by_only_name_from_data():
    name_by_user = input('Enter name of apprentice : ')
    # print(f'{name_by_user} works at {location_by_user}')
    while True:
        found = False
        for location, members in data["Apprentices"].items():
            for member in members:
                if name_by_user == member["name"]:
                    print(f'{name_by_user.upper()} works at {location}')
                    display_genral_details(member)
                    found = True
                    break  # Exit the inner loop once the member is found
            if found:
                break  # Exit the outer loop once the member is found
        if found:
            break  # Exit the while loop once the member is found

def details_of_name_from_data(name_by_user,location_by_user):
    # print(f'{name_by_user} works at {location_by_user}')

    for members in data["Apprentices"][location_by_user]:
        for member in members:
            if name_by_user == member[0]:
                display_genral_details(member)
            
    # while True:
    #     found = False
    #     for members in data["Apprentices"][location_by_user]:
    #         for member in members:
    #             if name_by_user == member["name"]:
    #                 print(f'{name_by_user.upper()} works at {location_by_user}')
    #                 display_genral_details(member)
    #                 found = True
    #                 break  # Exit the inner loop once the member is found
    #         if found:
    #             break  # Exit the outer loop once the member is found
    #     if found:
    #         break  # Exit the while loop once the member is found

def genereate_employee_id():
    random_digits = ''.join(random.choices(string.digits, k=7))
    new_employee_id = 'a'+ random_digits

    for locations,members in data["Apprentices"].items():
       for member in members:
         if new_employee_id != member['employee_id']:  
             return new_employee_id 
    else : genereate_employee_id()

    

def get_employee_details():
    new_member_name = input('Enter a name of new employee: ').lower()
    email_list = new_member_name.strip().split()
    email = f'{email_list[0]}.{email_list[1]}@jda.com'
    employee_id = genereate_employee_id()
    contact = input('Enter a contact of new employee: ')
    while len(contact) != 10:
        contact = input('Enter a 10 digit contact number of new employee: ')
        continue
        # if len(contact) != 10:
        #     contact = input('Please enter a 10 digit contact number of new employee: ')
    else: 
        new_member_details = {
        "name": new_member_name,
        "employee_id": employee_id,
        "email": email,
        "contact": contact }
        return new_member_details

def write_to_file(updated_json_data):
    with open('Apprentices.json', 'w') as file:
        file.write(updated_json_data)

def update_into_excicting():
    #check location
    location_by_user = input(f'Enter a location: from {list(data["Apprentices"].keys())} : ')
    while location_by_user not in data["Apprentices"].keys():
        location_user =input(f'Enter a valid location from {list(data["Apprentices"].keys())} : ').lower()
        continue
    else: 
        new_member = get_employee_details()
        data["Apprentices"][location_by_user].append(new_member)
        updated_json_data = json.dumps(data, indent=2)
        write_to_file(updated_json_data)

def delete_employee_by_id():
    #check location
    location_by_user = input(f'Enter a location: from {list(data["Apprentices"].keys())} : ')
    while location_by_user not in data["Apprentices"].keys():
        location_user =input(f'Enter a valid location from {list(data["Apprentices"].keys())} : ').lower()
        continue
    else:
    #check employee id
        apprentice_ID = {}
        for member in data["Apprentices"][location_by_user]:
            apprentice_ID.update({member["name"]:member["employee_id"]})
        employee_id_by_user = input(f'Enter an employee ID: from {list(apprentice_ID.items())} : ')
        while employee_id_by_user not in apprentice_ID.values():
            employee_id_by_user = input(f'Enter an employee ID: from {list(apprentice_ID.items())} : ')
            continue
        else:
            for member in data["Apprentices"][location_by_user]:
                if employee_id_by_user == member["employee_id"]:
                    data["Apprentices"][location_by_user].remove(member)
                    updated_json_data = json.dumps(data, indent=2)
                    write_to_file(updated_json_data)
                    break

def search_name_from_data():
    apprenitce_name_at =[]
    location_by_user = input(f'Enter location from {list(data["Apprentices"].keys())} : ').lower()
    while location_by_user not in data["Apprentices"].keys():
        location_by_user =input(f'Enter a valid location from {list(data["Apprentices"].keys())} : ').lower()
        continue
    else: 
        for members in data["Apprentices"][location_by_user]:
            apprenitce_name_at.append(members["name"]) 
        # print(apprenitce_name_at)

        name_by_user = input(f'Enter the name from the list {apprenitce_name_at}: ')
        while name_by_user not in apprenitce_name_at:
            name_by_user = input(f'Enter the name from the list {apprenitce_name_at}: ')
            continue
        else: 
            return details_of_name_from_data(name_by_user,location_by_user)



        # name_by_user = input('Enter a name of employee')
        # for location, members in data["Apprentices"].items():
        #     for member in members:
        #         if name == member["name"]:
        #             print(f'{name} works at {location}')
        #             display_genral_details(member)

if __name__ == '__main__':
    # details_by_only_name_from_data('narendra modi')
    # search_name_from_data()

    menu = {
    '1': display_all_data,
    '2': display_name_of_apperentice_of_location,
    '3': update_into_excicting,
    '4': delete_employee_by_id,
    '5': search_name_from_data,
    '6': details_by_only_name_from_data,
    '7': exit     #builtin function
    }

    while True:
        print('''
                Menu:
                       1. Display all details
                       2. Get details of working member by location 
                       3. Update / add member in location
                       4. Delete a member
                       5. get details of a specific member
                       6. get details only by name of the  member
                       7. Exit
                    
                    ''')
        choice = input('Enter your choice: ')
        if choice in menu:
            menu[choice]()
        else:
            print('Invalid choice')

    # data = json.dumps(get_data(), indent=2)
    # print(data['Apprentices'].keys()) #to print the locations from json data
    # display_name_of_apperentice_of_location(data)
    # details_of_name_from_data(input("Enter the name of the apprentice : ").lower())
    # updated_json_data = update_into_excicting()
    # print(updated_json_data)
    # print(genereate_employee_id())
    # update_into_excicting()
    # delete_employee_by_id()