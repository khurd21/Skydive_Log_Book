#!/usr/bin/python3.7

#############################
# Name:    Kyle Hurd
# Project: Virtual skydiving log book.
#          When using a new file, csv file needs to have
#          at least one jump logged to run properly. I might change
#          that in the future but I am lazy. When adding jumps, it
#          will add the jump according to the last jump logged in the
#          file.
############################


# Modules
############################

import file_manip as fm
import display as d
from csv import reader, writer


# Main
############################

def main():
    
    skydiver_info = fm.get_info_data(fm.app_path('assets/info.txt'))
    skydiver_info[1] = 'assets/' + skydiver_info[1]
    log_book = fm.get_log_data(fm.app_path(skydiver_info[1]))
    
   # d.display_jump_number(log_book, name, 200)
    while True:
        ans = d.display_menu(log_book, skydiver_info[0])
        
        if ans == 'q':
            quit()
        elif ans == 'd':
            d.display_jump_number(log_book, skydiver_info[0])
        elif ans == 'a':
            fm.add_jumps(log_book, skydiver_info)
        elif ans == 'v':
            d.display_jumps(log_book, skydiver_info[0])
        elif ans == 's':
            d.display_stats(log_book, skydiver_info)
            
    return

if __name__ == '__main__':
    main()
