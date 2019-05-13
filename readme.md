## Setup

```pip install -r requirements.txt```

```./manage.py migrate```

# Populate DB from csv
```./manage.py import_sampledataset [file_path]```
`

#### Run server
``` ./manage.py runserver```

### Usage`

###### Listing
``` GET /api/sampledata/ ```
###### Filtering
```GET /api/sampledata/?date=2017-05-17&channel=facebook&country=US&os=android&date_from=2017-05-17&date_to=2017-05-17```
##### Grouping
```GET /api/sampledata/?group_by=os,channel```
##### Ordering
``` GET /api/sampledata/?ordering=-impressions ```