########################################################################
#
# Parameter file for Temboz
#
########################################################################

# TCP port to use for the web server
port = 9999
# uncomment this if you want Temboz to bind to a specific IP address
#
# bind_address = 'localhost'
# bind_address = '192.168.1.9'

# number of RSS feeds fetched in parallel 
feed_concurrency = 10

# Maximum number of articles shown
overload_threshold = 200

# feed polling interval in seconds
refresh_interval = 3600

# Whether "catch-up" links require user confirmation (default is yes)
catch_up_confirm = True
hard_purge_confirm = True

# Should the "thumbs up" and "thumbs down" icons be shown at the bottom
# of long articles? False by default as this can slow down page rendering
# with certain browsers as they have to wait for all the images to be loaded
# on a page before they can determine whether an article is long enough to
# require the links at the bottom
#thumbs_bottom = True
thumbs_bottom = False

# automatic backups
# stream compression utility to use for backups
backup_compressor = ('gzip -9c', '.gz')
#backup_compressor = ('bzip2 -9c', '.bz2)
# number of daily backups to keep
daily_backups = 7
# at what time should the backup be made (default: between 3 and 4 AM)
backup_hour = 3

# garbage collection - articles flagged as "uninteresting" will have their
# content automatically dumped after this interval (but not their title or
# permalink) to make room. If this parameter is set to None or False, this
# garbage-collection will not occur
garbage_contents = 7
# garbage_contents = None

# after a longer period of time, the articles themselves are purged, assuming
# they are no longer in the feed files (otherwise they would reappear the next
# time the feed is loaded)
garbage_items = 180
# garbage_items = None

# URL to use as the User-Agent when downloading feeds
temboz_url = 'http://www.temboz.com/'
# user agent shown when fetching the feeds
user_agent = 'Temboz (%s)' % temboz_url

# page unauthenticated users should see
# the most common case is people checking the referrer logs on their web server
unauth_page = temboz_url

# dictionary of login/password
try:
  from private import auth_dict
except:
  auth_dict = {'majid': 'sopo'}

# maximum number of errors, after this threshold is reached,
# the feed is automatically suspended. -1 to unlimit
max_errors = 100

#debug = True
debug = False

# logging
import sys, os
if '--server' in sys.argv:
  log_filename = 'temboz.log'
  # if you modify mode and buffer size, see also update.py:cleanup
  # for the code that rotates this file daily
  log = open(log_filename, 'a', 0)
  os.dup2(log.fileno(), 1)
  os.dup2(log.fileno(), 2)
else:
  log = sys.stderr
# redirect stout and stderr to the log file
