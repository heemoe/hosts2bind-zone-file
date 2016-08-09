#!/usr/bin/python3
import re
import datetime
import os
#download hosts file path.
hostsFile="hosts"
#zone file save path.
outputZoneFile="hosts.zone"
#target named zone file path
targetZoneFile="/usr/local/named/var/rpz.zone"
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

os.system('rm hosts')
#your hosts file url. default save to current path.
os.system('wget https://coding.net/u/scaffrey/p/hosts/git/raw/master/hosts')

createZonesHeader()
FILE = open(hostsFile,'r')
WriteFILE = open(outputZoneFile,'w+')
WriteFILE.write(createZonesHeader())
# count = 0
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
        elif len(line) == 0 and len(line) == 1:
            print('blank line')
            oneZone = '\n'
        else:
            oneZone = ipname + '    IN A    ' + ipaddress
    except:
        print('error line')
# output zone file
    if len(oneZone) == 12 and not ';' in line:
        # count += 1
        # print(oneZone + str(count))
        continue
    WriteFILE.write(oneZone+'\n')
FILE.close()
WriteFILE.close()
getChar = raw_input('Enter Y to replace named file, Enter other finish')
if getChar == 'Y' or 'y' or '':
    os.system('echo ------ start replace named file -----')
    os.system('mv' + ' ' + targetZoneFile + ' ' + targetZoneFile + '.bak')
    os.system('mv' + ' ' + outputZoneFile + ' ' + targetZoneFile)
    os.system('replace done. :) ')
    os.system('service named restart')
else:
    os.system('echo process done. Please check your hosts.zone file.  :) ')
