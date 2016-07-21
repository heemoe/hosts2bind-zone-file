#!/usr/bin/python3
import re
import datetime
#Files Involved
hostsFile="/etc/hosts"
outputZoneFile="/Users/user/Desktop/hosts.zone"
nameServer="ns1"
# I don't know what the means of following fields. Just copied from others.
domainName="xxx.com"
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

# Variables
ipaddresses=list()
zones=dict()
def createZonesHeader():
    zonesHeader = str("$TTL 1D\n"
                        "@    IN SOA "+nameServer+"."+domainName+". root."+domainName+".(\n"
                        ""+SOA[0]+"\n"
                        ""+SOA[1]+"\n"
                        ""+SOA[2]+"\n"
                        ""+SOA[3]+"\n"
                        ""+SOA[4]+"\n"
                        "@  IN NS "+nameServer+"."+domainName+".\n"
                      )
    return zonesHeader

createZonesHeader()
FILE = open(hostsFile,'r')
WriteFILE = open(outputZoneFile,'w+')
WriteFILE.write(createZonesHeader())
for line in FILE:
    tmp=line.rstrip('|n')
    tmp=re.sub('\s+',' ',tmp)
    tmp=tmp.split(' ')
    ipaddress=tmp[0]
    ipname=tmp[1]
    # ipv6
    if ":" in ipaddress: continue
    # hosts comments replace to ;
    oneZone = str()
    try:
        if '#' in line[0]:
            line = line.replace('#',';',1)
            oneZone = line
        else:
            oneZone = ipname + '    IN A    ' + ipaddress
    except:
        if line == '\n':
            oneZone = ''
# output zone file
    print(oneZone)
    WriteFILE.write(oneZone+'\n')
FILE.close()
WriteFILE.close()


        