import json
# import random



def get_data():
    apperentice_file_path ='Apprentices.json'
    with open(apperentice_file_path, 'r') as f:
        details = json.load(f)
    return details

'''
#To shuffle the keys
keys = list(data["Apprentices"].keys())
random.shuffle(keys)
# print(keys)
shuffled_dict = {key: data["Apprentices"][key] for key in keys}
print(shuffled_dict)'''

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


if __name__ == "__main__":
    
    data = get_data()
    # print(data)
    name_of_apprentice = input("Enter name of apprentice: ").lower()
    search_name_from_data(name_of_apprentice)


