''' 
configFile.txt format
[DatabaseSection]
database.dbname=unitTest
database.user=root
database.password=**** 
'''

import ConfigParser
config = ConfigParser.RawConfigParser()
config.read('ConfigFile.properties')
print config.get('DatabaseSection', 'database.dbname');
