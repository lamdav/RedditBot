import time
import bot

def main():
    """
        Main loop.
    """
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    stalk = input("Enter user to follow: ")
    message = input("Enter message to reply with: ")

    stalkerBot = bot.bot(username, password, stalk, message)
    try:
        while (True):
            print('Press CTRL + C to quit')  # Works when ran from command line.
            stalkerBot.populateCheck()
            stalkerBot.setReplyCounter()
            stalkerBot.run()
            stalkerBot.writeCheck()
            stalkerBot.writeReplyCounter()
            print(stalkerBot.check)  # Console Feedback of check list.
            stalkerBot.clearCheck()
            time.sleep(180)  # Wait 3 minutes.
    except KeyboardInterrupt:
        pass

#-----------------------------------------------------------------------
# If this module is running at the top level (as opposed to being
# imported by another module), then call the 'main' function.
#-----------------------------------------------------------------------
if __name__ == '__main__':
    main()
