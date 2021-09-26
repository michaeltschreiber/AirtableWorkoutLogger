import sys
from AirtableHelper import airtable_upload
import datetime
from datetime import timezone

with open("api_key.txt") as f:
    api_key = f.readline().rstrip()

with open("base_id.txt") as f:
    base_id = f.readline().rstrip()

with open("table.txt") as f:
    table = f.readline().rstrip()

datestring = datetime.datetime.now(tz=timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
activity = sys.argv[1]
reps = int(sys.argv[2])
weight = int(sys.argv[3])

upload_data = {
    "Activity" : activity,
    "Date" : datestring,
    "Reps" : reps,
    "Weight" : weight
}

airtable_upload(table, upload_data, False, api_key, base_id, None)
