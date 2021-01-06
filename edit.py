#############################
# Name:        Kyle Hurd
# Project:     Virtual skydiving log book.
# Description: This file controls the content of log.csv and
#              info.txt, updating the information when requested
#              by the user and ensuring the files do not become
#              corrupted.
############################


# Modules
############################

import display as d
import file_manip as fm


# Functions
############################


def edit_jumps(log_book):
    ''' Edits the contents of any jump record within the
        skydiver log.
        
    :param log_book: the entire log of jumps
    :type log_book: 2d list
    :rtype: None
    '''
    d.clear()
    print(f'What jump do you wish to edit? [1:{log_book[-1][0]}]')
    while True:
        ans = input('-> ').strip()
        try:
            ans = int(ans)
            if ans >= 1 and ans <= int(log_book[-1][0]):
                d.edit_jump_info(log_book[ans])
                fm.save_csv_file(fm.app_path('assets/log.csv'), log_book)
                break
        except:
            print('Not a valid response.')
    
    return
    

def edit_stats(info):
    ''' Edits the contents of user's info within the info.txt
    
    :param info: the user's personalized data (name, weight,etc.)
    :type info: list
    :rtype: None
    '''
    while True:
        d.edit_user_stats(info)
        ans = input('-> ').strip()
        
        if ans == 'n': #name
            info[0] = fm.get_name()
        elif ans == 'c': # Current Parachute
            info[2] = fm.get_parachute_brand()
        elif ans == 'd': # DOM
            info[3] = fm.get_dom()
        elif ans == 'w': # Weight
            info[4] = fm.get_weight()
        elif ans == 's': # parachute size
            info[5] = fm.get_parachute_size()
        elif ans == 'r': # return
            break
        fm.save_info_file(fm.app_path('assets/info.txt'), info)
        
    return
    

def edit_home(log_book, info):
    ''' Controls which edit page is to be displayed.
    
    :param log_book: the entire log of jumps
           info: the info about the user
    :type log_book: 2d list
          info: list
    :rtype: None
    '''
    while True:
        ans = d.edit_display_home()
        if ans == 'j':
            edit_jumps(log_book)
        elif ans == 's':
            edit_stats(info)
        elif ans == 'r':
            break
        elif ans == 'q':
            quit()
        
    return
