import csv

# Models
#from .persons.models import Address
#from apps.users.models import User, Profile

def load_data_addresses(csv_filename):
    """Load data for file .csv."""

    with open(csv_filename, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)

    for row in reader:
        address = Address(**row)
        address.save()
        print(address)

def load_data_states(csv_filename):
    """Load data for file .csv."""

    with open(csv_filename, mode='r') as csvfile:
        reader = csv.DictReader(csvfile)
        
        for row in reader:
            state = State(**row)
            #state.save()
            print(state)

def main():
    load_data_states('data/states.csv')

if __name__ == '__main__':
    main()