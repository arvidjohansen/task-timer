import os
import sys
from time import sleep
from tqdm import tqdm
from terminalsize import get_terminal_size

DEFAULT_DURATION_MINUTES = 25
DEBUG = False

def set_timer():
    """ Sets the timer provided from args if possible,
    default value if not """
    
    try: 
        minutes = int(sys.argv[1])
        return minutes
    except: 
        print(f'Timer set to {DEFAULT_DURATION_MINUTES} minutes')
    return DEFAULT_DURATION_MINUTES

def _get_finish_text():
    """ Returns suitable text based on window-size """
    txt = """
    /        |/      |/  \     /  |/        |      /      | /      \       /  |  /  |/       \ 
   $$$$$$$$/ $$$$$$/ $$  \   /$$ |$$$$$$$$/       $$$$$$/ /$$$$$$  |      $$ |  $$ |$$$$$$$  |
    $$ |     $$ |  $$$  \ /$$$ |$$ |__            $$ |  $$ \__$$/       $$ |  $$ |$$ |__$$ |
    $$ |     $$ |  $$$$  /$$$$ |$$    |           $$ |  $$      \       $$ |  $$ |$$    $$/ 
    $$ |     $$ |  $$ $$ $$/$$ |$$$$$/            $$ |   $$$$$$  |      $$ |  $$ |$$$$$$$/  
    $$ |    _$$ |_ $$ |$$$/ $$ |$$ |_____        _$$ |_ /  \__$$ |      $$ \__$$ |$$ |      
    $$ |   / $$   |$$ | $/  $$ |$$       |      / $$   |$$    $$/       $$    $$/ $$ |      
    $$/    $$$$$$/ $$/      $$/ $$$$$$$$/       $$$$$$/  $$$$$$/         $$$$$$/  $$/  
    Press CTRL + C to exit
    """
    x, y = get_terminal_size()

    if y > 9 and x > 94:
        return txt
    
    txt = """
 _______  _                       _                        
(__ _ __)(_)             ____    (_) ____                  
   (_)    _   __   __   (____)    _ (____)    _   _  ____  
   (_)   (_) (__)_(__) (_)_(_)   (_)(_)__    (_) (_)(____) 
   (_)   (_)(_) (_) (_)(__)__    (_) _(__)   (_)_(_)(_)_(_)
   (_)   (_)(_) (_) (_) (____)   (_)(____)    (___) (____) 
                                                    (_)    
                                                    (_)
    """    
    if y > 9 and x > 58:
        return txt
    
    txt = """
       ╔╦╗┬┌┬┐┌─┐  ┬┌─┐  ┬ ┬┌─┐
        ║ ││││├┤   │└─┐  │ │├─┘
        ╩ ┴┴ ┴└─┘  ┴└─┘  └─┘┴  
    """
    if y > 4 and x > 25:
        return txt

    return 'Time is up!'

def _finish_flash():
    """ Flashes finish message on screen """
    
    clear_terminal()
    
    while True:
        txt = _get_finish_text()
        print(txt)
        sleep(0.1)
        clear_terminal()
        sleep(0.1)
    
def finished():
    """ Called when timer is finished """
    try:
        _finish_flash()
    except KeyboardInterrupt:
        clear_terminal()

def clear_terminal():
    try: os.system('cls'); return # Windows
    except: pass
    try: os.system('clear'); return # Linux / Mac
    except: pass

def time_remaining_str(sec):
    """ Returns a string containing how many min
    and sec remining e.g: 1m 23s """
    m = int(sec / 60)
    s = sec % 60
    return f'{m}m {s}s'

def start_countdown(seconds):
    """ Starts countdown using tqdm progress bars """
    clear_terminal()
    if DEBUG:
        seconds = int(seconds/60)
    for i in tqdm(
        range(seconds),
        desc='Progress',
        bar_format='{l_bar}{bar}{remaining}'):

        sleep(1)

def start_countdown_v2(seconds):
    """ Starts countdown using no external modules """
    clear_terminal()
    remaining = seconds
    count = 0
    for i in range(seconds):
        clear_terminal()
        prog = '=' * count
        prog += '>'
        whspace = ' ' * remaining
        end = f'|{time_remaining_str(remaining)}|'
        sys.stdout.write(f'{prog}{whspace}{end}')
        sys.stdout.flush()
        count += 1
        remaining -= 1
        sleep(1)
    

if __name__ == '__main__':
    minutes = set_timer()
    seconds = minutes * 60
    start_countdown_v2(seconds)
    finished()



