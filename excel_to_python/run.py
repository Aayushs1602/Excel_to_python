import schedule
import time
from mail_with_attachment import sendmail
from xlswritter import createfile


# For checking
def done():
    print("done")


# Runs the code every hour
# schedule.every(1).hour.do(done)
# schedule.every(1).hour.do(createfile)
# schedule.every(1).hour.do(sendmail)

schedule.every(2).minutes.do(done)
schedule.every(2).minutes.do(createfile)
schedule.every(2).minutes.do(sendmail)

while True:
    # Checks for pending jobs
    schedule.run_pending()
    time.sleep(1)
