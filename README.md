## Data collection
- top instances: https://instances.social/list/advanced#lang=&allowed=&prohibited=&min-users=&max-users=

## requirements
Python:
- Pandas

R:
- [HTTR]()
- [rtoot]()
- [readr]()

## How to run:
python collect_mastodon.py


### collect_mastodon.py
This code does the following:
- Run collect_mastodon.r for each of the most popular instances, which collects toots for each instances and saves it into a file
- At regular intervals, open each instance's associated file, check if this file is stale
- If the file is stale, then the R program ran into a rare failure, in which case we restart the collection if there are not too many R programs running and we have collected toots from this instance before
- The latter condition is only true when we do not run into an issue with the R program rtoot whereby the instance data cannot be collected

### collect_mastodon.r
This is the workhorse. The code does the following:
- Get public authentication tokens
- begin collecting toots and save them within a folder 'mastodon_data' with a file name: instances (replacing '.' with '-' in the instance name) as well as the time the instance was first collected

