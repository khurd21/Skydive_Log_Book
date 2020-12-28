#############################
# Name:        Kyle Hurd
# Project:     Virtual Log Book
# Description: Manages manipulation of data typically requested from the
#              display module.
############################


# Modules
############################


from csv import reader, writer
import display as d
import datetime
import os, sys


# Functions
############################


def app_path(path):
    '''
    Borrowed from StackOverflow. Allows program to locate a dependent file
    when being placed into an executable file
    
    :param path: the local path to file
    :type path: string
    :rtype: string
    :rformat: full path to the project
    '''
    frozen = 'not'
    if getattr(sys, 'frozen', False):
            # we are running in executable mode
            frozen = 'ever so'
            app_dir = sys._MEIPASS
    else:
            # we are running in a normal Python environment
            app_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(app_dir, path)
    
    
def get_log_data(file_name):
    ''' Returns .csv data in the form of a list
    
    :param file_name: the full path to the csv file
    :type file_name: string
    :rtype: 2D list
    :return: csv data from file_name
    '''
    with open(file_name, 'r') as infile:
        csv_reader = reader(infile)
        csv_list = list(csv_reader)
    return csv_list
    
    
def get_info_data(file_name):
    ''' Returns personalized data of the skydiver [equipment, weight, ...]
    
    :param file_name: the full path to the csv file
    :type file_name: string
    :rtype: list
    '''
    with open(file_name, 'r') as infile:
        items = []
        for line in infile:
            temp = line.split(':')
            items.append(temp[1].strip())
        return items
        

def save_info_file(file_name, info_list):
    ''' Writes user's specs to the info.txt
    
    :param file_name: the full path to the .txt file
           info_list: the user's specs to be written
    :type file_name:  string
          info_list:  list of strings
    :rtype: N/A
    '''
    with open(file_name, 'w' as outfile):
        print(f'name: {info_list[0]}')
        print(f'filename: {info_list[1]}')
        print(f'current parachute: {info_list[2]}')
        print(f'DOM: {info_list[3]')
        print(f'weight [lbs]: {info_list[4]}')
        print(f'parachute size [sq. ft.]: {info_list[5]}')
        
    return
    
    
def save_csv_file(file_name, csv_list):
    ''' Writes jump information to the csv log
    
    :param file_name: the full path to the csv file
           csv_list:  the 2d csv list to be written
    :type file_name:  string
          csv_list:   list of strings
    :rtype: N/A
    '''
    with open(file_name, 'w') as outfile:
        csv_writer = writer(outfile)
        for row in csv_list:
            csv_writer.writerow(row)
    return


# Setting Log Info
#######################################

def get_total_jumps(log_book):
    ''' Returns the amount of belly, freefly, canopy jumps, and
        estimated freefall time in the air.
    
    :param log_book: the entire log of the user's jumps
    :type log_book:  2d list
    :rtype: ints [belly, freefly, wingsuit, canopy jumps and total freefall]
    '''
    b = f = c = t = w = 0.0
    for item in log_book:
        if item[6].lower() == 'b':
            t += (int(item[2]) - 3000) * ( 1 / 12000)
            b += 1
        elif item[6].lower() == 'f':
            t += (int(item[2]) - 3000) * (1 / 13500)
            f += 1
        elif item[6].lower() == 'c':
            c += 1
        elif item[6].lower() == 'w':
            w += 1
    return int(b), int(f), int(c), int(w), int(t)
     

def get_date():
    ''' Returns the date of jump inputted by user
    
    :param None:
    :rtype: string
    :rformat: 'xx/xx/xxxx'
    '''
    while True:
        print('Enter date or press [t] for today')
        date = input('-> Date [mm/dd/yyyy]: ')
        
        if date == 't':
            now = datetime.datetime.now()
            date = now.strftime('%m/%d/%Y')
            
        date = date.replace(',', '').strip()
        
        if len(date) == 10:
            if date[2] == '/' and date[5] == '/':
                break
            else:
                print('Invalid format.')
        else:
            print('Invalid format.')
        
    return date


def get_altitude():
    ''' Returns the altitude inputted by the user.
    
    :param None:
    :rtype: int
    '''
    while True:
        altitude = input('-> Altitude: ')
        altitude = altitude.replace(',', '').strip()
        
        try:
            altitude = int(altitude)
            if altitude > 15000:
                print(f'{altitude} feet seems a bit high. Is this correct? [Y/N]')
                ans = input('-> ').strip().lower()
                if ans == 'y':
                    break
            else:
                break
        except:
            print('Invalid format. Cannot be converted to integer')
            
    return altitude


def get_location():
    ''' Returns the location inputted by the user
    
    :param None:
    :rtype: string
    '''
    location = input('-> Location: ')
    location = location.strip().replace(',', '')
    return location
        

def get_aircraft():
    ''' Returns the aircraft type selected by the user
    
    :param None:
    :rtype: string
    '''
    print('Type in aircraft or select from list below:')
    print('[1 - Otter, 2 - Caravan, 3 - King Air, 4 - Cessna 182]')
    aircraft = input('-> ')
    aircraft = aircraft.replace(',','').strip()
    
    if aircraft == '1':
        return 'Otter'
    elif aircraft == '2':
        return 'Caravan'
    elif aircraft == '3':
        return 'King Air'
    elif aircraft == '4':
        return 'Cessna 182'
        
    return aircraft
  
  
def get_equipment():
    ''' Returns the size of parachute inputted by the user.
    
    :param None:
    :rtype: int
    '''
    while True:
        try:
            equipment = int(input('-> Equipment: ').strip())
            if equipment < 100:
                print('Compensating?')
            elif equipment >= 200:
                print('Consider downsizing')
            break
        except:
            print('Invalid format. Please make sure it is an integer.')
    return equipment


def get_type_of_jump():
    ''' Returns the type of jump inputted by user. Jump types include
        belly jumps, freefly jumps, wingsuit jumps, or canopy.
        
    :param None:
    :rtype: string/char
    '''
    while True:
        print('[b - belly, f - freefly, w - wingsuit, c - canopy]')
        type = input('-> Type of jump: ').strip()
        if type == 'b' or type == 'f' or type == 'w' or type == 'c':
            break
        else:
            print('Invalid format.')
    return type
    

def get_signature():
    ''' Returns the license number of another skydiver. Must
        be of a specific format shown as :rformat:
    
    :param None:
    :rtype: string
    :rformat: '<A,B,C,orD>-<five digit number>' ex. 'C-12345'
    '''
    while True:
        signature = input('-> Signature [ex. C-12345]: ').strip()
        if (len(signature) == 7) and \
                    (signature[0] == 'A' or \
                        signature[0] == 'B' or \
                            signature[0] == 'C' or \
                                signature[0] == 'D') and \
                                    signature[1] == '-':
            break
        else:
            print('Invalid format')
            
    return signature
        

def get_notes():
    ''' Returns the user's description of the jump. Character limit
        set at 300.
        
    :param None:
    :rtype: string
    '''
    while True:
        note = input('-> Description: ').replace(',','').strip()
        if len(note) > 300:
            print('Cannot exceed 300 characters.')
        else:
            break
        
    return note
    
    
def add_jumps(log_book, skydiver_info):
    ''' Driver for logging jumps and saving the new info into
        the csv file / log book.
    
    :param log_book:      Entire log of the user's jumps
           skydiver_info: Personal info about the user
    type   log_book:      2d list
           skydiver_info: list
    :rtype: None
    '''
    print('How many jumps?')
    while True:
        try:
            num_jumps = int(input('-> ').strip())
            break
        except:
            print('Enter a valid number')
    
    for i in range(0,num_jumps):
        jump =  []
        d.clear()
        d.display_add_jumps(log_book, skydiver_info[0])
        print(f'{i+1} of {num_jumps}')
        jump.append(str(int(log_book[-1][0]) + 1))
        jump.append(str(get_date()))
        jump.append(str(get_altitude()))
        jump.append(str(get_location()))
        jump.append(str(get_aircraft()))
        jump.append(str(get_equipment()))
        jump.append(str(get_type_of_jump()))
        notes = str(get_notes()) # Not ideal, wanted to get description
                                 # before getting signature
        jump.append(str(get_signature()))
        jump.append(notes)
        log_book.append(jump)
        save_csv_file(app_path(skydiver_info[1], log_book))
    return
