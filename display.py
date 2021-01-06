#############################
# Name:        Kyle Hurd
# Project:     Virtual Log Book
# Description: Functions to display each scene and data from
#              the skydiver's log history.
############################


# Modules
############################

from os import system, name
import datetime
import file_manip as fm


# Functions
############################


def clear():
    ''' Allows program to clear the page of the terminal.
        Works for Windows, MacOS and Linux
    '''
    
    # Windows
    if name == 'nt':
        _ = system('cls')
        
    # MacOS and Linux
    else:
        _ = system('clear')
        
    return


# For the edit.py Module
###################################


def edit_display_home():
    ''' Returns the selection type to edit for the user's stats
    
    :param: None
    :rtype: char
    '''
    clear()
    print( '############################################################')
    print( '# Select what you wish edit:                               #')
    print( '# [j - jump info]         [s - user stats]                 #')
    print( '# [r - return]                                             #')
    print( '#                                                          #')
    print( '############################################################')
    
    while True:
        ans = input('-> ').strip()
        chars = 'jsr'
        if len(ans) == 1 and any((c in chars) for c in ans):
            break
            
    return ans
  
    
def edit_user_stats(info):
    ''' Displays the user's info to terminal screen
    
    :param info: a list of the jumper's info
    :type info: list
    :rtype: None
    '''
    clear()
    print( '###############################################################')
    print( '#                                                             #')
    print(f'# Name:                     {info[0]:12}                      #')
    print(f'# Current Parachute:        {info[2]:12}                      #')
    print(f'# DOM:                      {info[3]:12}                      #')
    print(f'# Weight [lbs]:             {info[4]:12}                      #')
    print(f'# Parachute Size [sq. ft.]: {info[5]:12}                      #')
    print( '###############################################################')
    print()
    print( '[n - name,   c - current parachute, d - DOM   ]')
    print( '[w - weight, s - parachute size   , r - return]')
    print()
    return
    

def edit_jump_info(info):
    ''' Displays the jump info to edit
    
    :param info: the log of the jump
    :type  info: list
    :rtype: list
    :rformat: same as parameter, list of jump info
    '''
    flag = False
    while not flag:
        clear()
        print( '############################################################')
        print( '#                                                          #')
        print( '# Jump Number:', info[0].ljust(43,' '),                   '#')
        print( '# Date:       ', info[1].ljust(43,' '),                   '#')
        print( '# Location:   ', info[3].ljust(43,' '),                   '#')
        print( '# Aircraft:   ', info[4].ljust(43,' '),                   '#')
        print( '# Altitude:   ', info[2].ljust(43,' '),                   '#')
        print( '# Equipment:  ', info[5].ljust(43,' '),                   '#')
        print( '# Type:       ', info[6].ljust(43,' '),                   '#')
        print( '#                                                          #')
        print( '# Signed by:  ', info[7].ljust(43,' '),                   '#')
        print( '############################################################')
        print()
        print( 'Description:', info[8])
        print()
        print( '[d - date,      l - location, a - aircraft,  t - alitude    ]')
        print( '[e - equipment, y - type,     s - signed by, c - description]')
        print( '[r - return                                                 ]')
    
        while True:
            ans = input('-> ').strip()
            if ans == 'd':
                info[1] = fm.get_date()
                break
            elif ans == 'l':
                info[3] = fm.get_location()
                break
            elif ans == 'a':
                info[4] = fm.get_aircraft()
                break
            elif ans == 't':
                info[2] = str(fm.get_altitude())
                break
            elif ans == 'e':
                info[5] = str(fm.get_equipment())
                break
            elif ans == 'y':
                info[6] = fm.get_type_of_jump()
                break
            elif ans == 's':
                info[7] = fm.get_signature()
                break
            elif ans == 'c':
                info[8] = fm.get_notes()
                break
            elif ans == 'r':
                flag = True
                break
            
    return
    
    
# General Display Functions
#####################################


def display_stats(log_book, info):
    ''' Displays the full statistic information of the user's jump
        log to the terminal page.
    
    :param log_book: the entire log book of the user
           info: the skydiver's personalized info and equipment
    :type log_book: 2d list
          info: list
    :rtype: None
    '''
    while True:
        clear()
        wing_load = float(info[4]) / float(info[5])
        tot_belly, tot_freefly, tot_canopy, \
        tot_wing, tot_coach, tot_tandem, tot_time = fm.get_total_jumps(log_book)
        print( '###############################################################')
        print( '# Jumper:        ', info[0].ljust(43,' '),                   '#')
        print( '# Total Jumps:   ', log_book[-1][0].ljust(43,' '),           '#')
        print( '#                                                             #')
        print( '# Parachute:     ', info[2].ljust(43,' '),                   '#')
        print( '# DOM:           ', info[3].ljust(43,' '),                   '#')
        print( '# Wing Load:     ', str(wing_load).ljust(43,' '),            '#')
        print( '#                                                             #')
        print( '# Number of Jumps by Classification                           #')
        print( '# Total Belly:   ', str(tot_belly).ljust(43,' '),            '#')
        print( '# Total FreeFly: ', str(tot_freefly).ljust(43,' '),          '#')
        print( '# Total Canopy:  ', str(tot_canopy).ljust(43,' '),           '#')
        print( '# Total WingSuit:', str(tot_wing).ljust(43,' '),             '#')
        print( '# Total Coach:   ', str(tot_coach).ljust(43,' '),            '#')
        print( '# Total Tandem:  ', str(tot_tandem).ljust(43,' '),           '#')
        print( '# Time [min]:    ', str(tot_time).ljust(43,' '),             '#')
        print( '#                                                             #')
        print( '# [r - return]                                                #')
        print( '###############################################################')
        print()
        
        ans = input('-> ').strip()
        if ans == 'r':
            break
    return


def display_add_jumps(log_book, name):
    ''' Simple program to display the user's name and total jump.
    
    :param log_book: the entire log book [to get the last jump number]
           name:     user's name
    :type  log_book: 2d list
           name:     string
    :rtype: None
    '''
    print( '############################################################')
    print( '# Jumper:     ', name.ljust(43,' '),                      '#')
    print( '# Total Jumps:', log_book[-1][0].ljust(43,' '),           '#')
    print( '#                                                          #')
    print(f'############################################################')
    print()
    return


def display_jumps(log_book, name):
    ''' Displays a condensed version of the user's jump history.
        Up to 10 jumps displayed per page witht the ability to
        scroll through all the jumps.
    
    :param log_book: the entire user's log history
           name: the user's name
    :type log_book: 2d list
          name: string
    :rtype: None
    '''
    num_elements = len(log_book) - 1
    i = len(log_book) - 1
    if i - 9 < 1:
        j = 1
    else:
        j = i - 9
        
    info = log_book[0]
    info[0] = 'jump no.'
    while True:
        clear()
        print( '############################################################')
        print( '# Jumper:     ', name.ljust(43,' '),                      '#')
        print( '# Total Jumps:', log_book[-1][0].ljust(43,' '),           '#')
        print( '#                                                          #')
        print( '# [ n - next]    [ p - previous]    [ r - return]          #')
        print( '#                                                          #')
        print( '############################################################')
        print()
        print(f'{info[0]:8} -> {info[1]:10} {info[3]:15} type       {info[7]:10} ')
        print( '------------------------------------------------------------')
        
        # i - last element displayed, j - first element displayed
        # k - iterator for the for-loop
        for k in range(j,i+1):
            log = log_book[k]
            type = ''
            if 'b' in log[6]:
                type = 'Belly'
            elif 'w' in log[6]:
                type = 'Wingsuit'
            elif 'f' in log[6]:
                type = 'Freefly'
            elif 'c' in log[6]:
                type = 'Canopy'
            elif 'a' in log[6]:
                type = 'Coach'
            elif 't' in log[6]:
                type = 'Tandem'
                
            # The condensed log of each jump
            print(f'{log[0]:8} -> {log[1]:10} {log[3]:15} {type:10} {log[7]:10} ')
        
        print()
        while True:
            ans = input('-> ').strip()
            if 'p' in ans:
                i -= 10
                if i < 1:
                    i = num_elements
                j = i - 9
                if j < 1:
                    j = 1
                break
                    
            elif 'n' in ans:
                i += 10
                if i > num_elements:
                    i %= 10
                    if i == 0:
                        i += 10
                j = i - 9
                if j < 1:
                    j = 1
                break
            
            elif ans == 'r':
                return
            
    return


def display_jump_number(log_book, name):
    ''' Displays the full specs of each jump one by one. User can
        cycle through each jump by pressing 'n' or 'p'
        
    :param log_book: the entire user's log of jumps
           name: the user's name
    :type  log_book: 2d list
           name: string
    :rtype: None
    '''

    # Getting Jump Number
    clear()
    print(f'[r - return, 1:{log_book[-1][0]} - jump #]')
    flag = False
    
    while True:
        ans = input('-> ').strip()
        if ans == 'r':
            return
            
        try:
            num = int(ans)
            max = int(log_book[-1][0])
        except:
            print('Invalid response. Not an int or out of range.')
            
        if max < num or num < 1:
            print('Invalid response.')
        else:
            break
            
    # Displaying Jump Number
    while not flag:
        clear()
        info = log_book[num]
        type = ''
        if 'w' in info[6]:
            type = 'Wingsuit'
        elif 'b' in info[6]:
            type = 'Belly'
        elif 'f' in info[6]:
            type = 'Freefly'
        elif 'c' in info[6]:
            type = 'Canopy'
        elif 'a' in info[6]:
            type = 'Coach'
        elif 't' in info[6]:
            type = 'Tandem'
        
        print( '############################################################')
        print( '# Jumper:     ', name.ljust(43,' '),                      '#')
        print( '# Total Jumps:', log_book[-1][0].ljust(43,' '),           '#')
        print( '############################################################')
        print()
        print()
        print( '############################################################')
        print( '# Jump Number:', info[0].ljust(43,' '),                   '#')
        print( '# Date:       ', info[1].ljust(43,' '),                   '#')
        print( '# Location:   ', info[3].ljust(43,' '),                   '#')
        print( '# Aircraft:   ', info[4].ljust(43,' '),                   '#')
        print( '# Altitude:   ', info[2].ljust(43,' '),                   '#')
        print( '# Equipment:  ', info[5].ljust(43,' '),                   '#')
        print( '# Type:       ', type.ljust(43,' '),                      '#')
        print( '#                                                          #')
        print( '# Signed by:  ', info[7].ljust(43,' '),                   '#')
        print( '############################################################')
        print()
        print( 'Description:', info[8])
        print()
        print( '[n - next, p - prev, r - return]')
    
        # Waiting for input to leave function
        flag = False
        while not flag:
            ans = input('-> ').strip()
            if ans == 'n':
                num += 1
                if num > int(log_book[-1][0]):
                    num = 1
                break
            elif ans == 'p':
                num -= 1
                if num < 1:
                    num = int(log_book[-1][0])
                break
            elif ans == 'r':
                flag = True
            else:
                flag = False
    return


def display_menu(log_book, name):
    ''' The main menu for the program. Displays options available and
        returns the selection given by the user.
    
    :param log_book: the entire log jump history of the user
           name: the user's name
    :type  log_book: 2d list
           name: string
    :rtype: char
    '''
    clear()
    print( '############################################################')
    print( '# Jumper:     ', name.ljust(43,' '),                      '#')
    print( '# Total Jumps:', log_book[-1][0].ljust(43,' '),           '#')
    print( '#                                                          #')
    print( '# Select an option below:                                  #')
    print( '#                                                          #')
    print( '# [a - add jumps]            [v - view jumps]              #')
    print( '# [d - display jump num]     [e - edit]                    #')
    print( '# [s - display stats]        [q - quit]                    #')
    print( '#                                                          #')
    print( '############################################################')
    print()
    
    while True:
        ans = input('-> ').strip()
        chars = 'avdesqg'
        if len(ans) == 1 and any((c in chars) for c in ans):
            break
            
    return ans
