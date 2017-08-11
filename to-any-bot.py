
import logging
import time
import datetime

import praw


reddit = praw.Reddit(
	'posttypebot', 
	user_agent='Python3:Change post type bot - any v1.1 (by /u/_ihavemanynames)')

logging.basicConfig(filename='posttype.log',level=logging.DEBUG) # Get file to log to

def authenticate():
    logging.info("Authenticated as {}".format(reddit.user.me()))
    return reddit  

def main():
    reddit=authenticate()
    # Specify subreddit
    sub=reddit.subreddit('samstestingsub')    
    # Get current time in UTC and make it into a string    
    current_time=str(datetime.datetime.utcnow())     
    logging.info('Current time in UTC:' + current_time)
    
    for a in range(10):     # Try 10 times
        try: 
            logging.info('Trying to change settings...')
            # Change subreddit settings to post type: any
            sub.mod.update(link_type='any')    
            logging.info('Changed settings')   
            # If this was successful, stop trying to change the settings (exit loop)
            break      
        except RequestException:
            # If the servers are too busy, log the exception. Then wait 2 minutes and try again (go to top of the loop).
            logging.exception('Servers are too busy. Sleeping for 2 minutes.')
            time.sleep(60*2)
            continue
        except Exception as e:  
            # If attempt wasn't successful for some other reason, log the exception and try again.
            logging.exception('Unable to change settings. Trying again...')
	    time.sleep(10)
            
            
if __name__ == "__main__":
    main()
