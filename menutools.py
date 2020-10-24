#if __name__ == "__main__":
#    raise RuntimeError("This is a librairy, don't run this as __main__")


import blessed
from math import floor,ceil
from time import sleep
term = blessed.Terminal()

def prompt(message, title=None, height=term.height - 2, width=term.width - 2):
    if height > term.height or width > term.width:
        raise RuntimeError("the menu is larger than the terminal emulator. ")
    if height <= 0  or width <= 0:
        raise RuntimeError("the menu size can not be 0 or smaller")
    with term.fullscreen(), term.cbreak():
        if not isinstance(title, str) and title != None:
            raise TypeError("the title argument must be a string. ")
        titlebar_x_start_pos = floor((term.width - width) / 2)
        titlebar_y_start_pos = floor((term.height - height) / 2)
        if title != None:
            title_start_pos = floor((width - len(title))/2)
            title_end_pos = title_start_pos + len(title)

        #title bar
        to_print = ""
        if title == None:
            for x in range(width):
                to_print += " "
        else:
            for x in range(width):
                if x >= title_start_pos and x < title_end_pos:
                    to_print += title[x-title_start_pos]
                else:
                    to_print += " "
        print(f"{term.move_xy(titlebar_x_start_pos, titlebar_y_start_pos)}{term.black_on_yellow}{to_print}")
        
        #content
        letters_printed = 0
        new_line = False
        for row in range(height-3):
            to_print = ""
            for _ in range(width-2):
                if letters_printed <= len(message)-1:
                    if message[letters_printed] == "\n":
                        new_line = True
                        letters_printed += 1
                    if not new_line:
                        to_print += message[letters_printed]
                        letters_printed += 1
                    else:   to_print += " "
                else:   to_print += " "
            print(f"{term.move_xy(titlebar_x_start_pos, titlebar_y_start_pos+row+1)}{term.black_on_yellow} {term.black_on_grey}{to_print}{term.black_on_yellow} ")
            new_line = False
        #ok prompt
        
        ok_text = "<ok>"
        ok_start_pos = floor(((width-2) - len(ok_text))/2)
        ok_end_pos = ok_start_pos + len(ok_text)
        to_print = ""
        for x in range(width-2):
            if x >= ok_start_pos and x < ok_end_pos:
                if x == ok_start_pos:
                    to_print += term.white_on_red
                to_print += ok_text[x-ok_start_pos]
            else:
                if x == ok_end_pos:
                    to_print += term.black_on_grey
                to_print += " "
        print(f"{term.move_xy(titlebar_x_start_pos, titlebar_y_start_pos + height-2)}{term.black_on_yellow} {term.black_on_grey}{to_print}{term.black_on_yellow} ")

        #bottom bar
        to_print = ""
        for x in range(width):
            to_print += " "
        print(f"{term.move_xy(titlebar_x_start_pos, titlebar_y_start_pos + height-1)}{term.black_on_yellow}{to_print}")

        
        sleep(3)



prompt("world",title="hello ")