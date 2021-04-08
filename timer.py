import os
import sys
from time import sleep
from tqdm import tqdm
from terminalsize import get_terminal_size

DEFAULT_DURATION_MINUTES = 25

def set_timer():
    """ Sets the timer provided from args if possible,
    default value if not """
    
    try: 
        minutes = int(sys.argv[1])
        return minutes
    except: 
        print(f'Timer set to {DEFAULT_DURATION_MINUTES} minutes')
    return DEFAULT_DURATION_MINUTES

def _get_finish_text(x, y):
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
    if y < 10:
        txt = 'Time is up!'
    return txt

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

def start_countdown(seconds):
    #print('Starting countdown... See you in {seconds} seconds!')
    clear_terminal()
    for i in range(seconds):
        sys.stdout.write("\r{0}>".format("="*i))
        sys.stdout.flush()
        sleep(0.5)
    """
    for i in tqdm(range(seconds*10)):
        #print(get_terminal_size())
        sleep(0.1)
    """



minutes = set_timer()
seconds = minutes * 60
start_countdown(seconds)
finished()



