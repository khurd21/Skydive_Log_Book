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
    '''
    
    # Windows
    if name == 'nt':
        _ = system('cls')
        
    # MacOS and Linux
    else:
        _ = system('clear')
        
    return


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
        tot_belly, tot_freefly, tot_canopy, tot_wing, tot_time = fm.get_total_jumps(log_book)
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
        print( '# Total WingSuit:', str(tot_freefly).ljust(43,' '),          '#')
        print( '# Time [min]:    ', str(tot_time).ljust(43,' '),             '#')
        print( '#                                                             #')
        print( '# [r - return]          [q - quit]                            #')
        print( '###############################################################')
        print()
        
        ans = input('-> ').strip()
        if ans == 'q':
            quit()
        elif ans == 'r':
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
        print( '# [ n - next]           [ p - previous]                    #')
        print( '# [ r - return]         [ q - quit]                        #')
        print( '############################################################')
        print()
        print(f'{info[0]:8} -> {info[1]:10} {info[3]:15} {info[7]:10} ')
        print( '------------------------------------------------------------')
        for k in range(j,i+1):
            log = log_book[k]
            print(f'{log[0]:8} -> {log[1]:10} {log[3]:15} {log[7]:10} ')
        
        print()
        while True:
            ans = input('-> ').strip()
            if ans == 'p':
                i -= 10
                if i < 1:
                    i = num_elements
                j = i - 9
                if j < 1:
                    j = 1
                break
                    
            elif ans == 'n':
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
            
            elif ans == 'q':
                quit()
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
    print(f'[r - return, q - quit, 1:{log_book[-1][0]} - jump #]')
    flag = False
    
    while True:
        ans = input('-> ').strip()
        if ans == 'q':
            quit()
        elif ans == 'r':
            return
            
        try:
            num = int(ans)
        except:
            print('Invalid response. Is not an int')
            
        if int(log_book[-1][0]) < num < 1:
            print('Invalid response.')
        else:
            break
            
    # Displaying Jump Number
    while not flag:
        clear()
        info = log_book[num]
    
        if info[6] == 'w':
            info[6] = 'Wingsuit'
        elif info[6] == 'b':
            info[6] = 'Belly'
        elif info[6] == 'f':
            info[6] = 'Freefly'
        elif info[6] == 'c':
            info[6] = 'Canopy'
        
        print( '############################################################')
        print( '# Jumper:     ', name.ljust(43,' '),                      '#')
        print( '# Total Jumps:', log_book[-1][0].ljust(43,' '),           '#')
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
        print( '[n - next, p - prev, r - return, q - quit]')
    
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
            elif ans == 'q':
                quit()
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
    print( '# [d - display jump num]     [q - quit]                    #')
    print( '# [s - display stats]                                      #')
    print( '#                                                          #')
    print( '############################################################')
    print()
    
    while True:
        ans = input('-> ')
        if ans == 'q' or ans == 'd' or \
            ans == 'v' or ans == 'a' or ans == 's':
            break
    return ans
