import os
from retrieve import get_country_data
from retrieve import get_asn_data

if __name__ == '__main__':
    get_country_data()   # retrieves GeoLite2-Country
    get_asn_data()       # retrieves GeoLite2-ASN