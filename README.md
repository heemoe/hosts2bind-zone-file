#### A easy way to convert hosts file to Bind .zone file.


> edit the flowing code to custom attribute.
```
#download hosts file path.
hostsFile="hosts"
#zone file save path.
outputZoneFile="hosts.zone"
nameServer="ns1"
# I don't know what the means of following fields. Just copied from others.
domainName="pandadns.com"
zoneSerial=datetime.datetime.strftime(datetime.datetime.now(), '%Y%m%d%H%M%S')
refresh = "3H"
retry = "15M"
expiry = "1W"
SOA = [ ''+zoneSerial+'	; serial',
        '3H		; refresh',
        '15M		; retry',
        '1W		; expiry',
        '1D)		; minimum'
       ]
)		; minimum'
       ]
```

- run `python3 hosts2zone.py` to fetch hosts file and generate a `hosts.zone` file.