import praw
import time

class bot:
    """
        A basic stalker bot that will follow a specified user
    """
    def __init__(self, userName, password, stalk, quote):
        # Constant.
        self.COOLDOWN = 180

        # Quote.
        self.quote = quote

        # User Data.
        self.username = userName
        self.password = password

        # Follow /u/lynchkin.
        self.stalk = stalk

        # Preliminary Setup.
        self.user = praw.Reddit(user_agent="DESCRIPTIVE PHRASE HERE")
        self.check = []

    def run(self):
        """
            Bot's primary function.
        """
        self.user.login(self.username, self.password)
        follow = self.user.get_redditor(self.stalk)
        limit = 3
        counter = 1
        generator = follow.get_comments(sort='new', limit=limit)

        for comment in generator:

            try:
                if comment.id not in self.check:
                    comment.reply(self.quote)
                    # Requires link karma of x > 2.
#                     self.user.send_message(self.stalk, "Deez Nuts " + str(self.replyCounter),
#                                             "You have received " + str(self.replyCounter) + " messages")
#                     self.replyCounter = self.replyCounter + 1
                    print('Done ', counter)
                    self.check.append(comment.id)
                else:
                    print('Pass ', counter)
                    counter = counter + 1
                    continue

                time.sleep(self.COOLDOWN)
                counter = counter + 1
            except praw.errors.RateLimitExceeded:
                print("Rate Cooldown")
                return

    def populateCheck(self):
        """
            Populates the check list.
        """
        checkInput = open('check.txt', 'r')
        for line in checkInput:
            self.check.append(line.strip('\n'))

        checkInput.close()

    def writeCheck(self):
        """
            Overwrites the check.txt file with data within the check list.
        """
        checkInput = open('check.txt', 'w')
        for k in range(len(self.check)):
            writeValue = self.check[k] + ''
            checkInput.write(writeValue + '\n')

        checkInput.close()

    def setReplyCounter(self):
        """
            Set Reply Counter value.
        """
        replyCounterFile = open('replyCounter.txt', 'r')
        self.replyCounter = replyCounterFile.readline()
        replyCounterFile.close()

    def writeReplyCounter(self):
        """
            Write to replyCounter.txt
        """
        replyCounterFile = open('replyCounter.txt', 'w')
        replyCounterFile.write(str(self.replyCounter))
        replyCounterFile.close()

    def clearCheck(self):
        """
            Clear self.check
        """
        self.check.clear()


