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
minutes = int(sys.argv[2])
resistance = float(sys.argv[3])
minpermile = float(sys.argv[4])

upload_data = {
    "Activity" : activity,
    "Date" : datestring,
    "Minutes" : minutes,
    "Resistance" : resistance,
    "MinPerMile" : minpermile
}

airtable_upload(table, upload_data, False, api_key, base_id, None)
