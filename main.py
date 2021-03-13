from retrieve import get_country_data
from retrieve import get_asn_data
from retrieve import get_city_data

if __name__ == '__main__':
    get_country_data()   # retrieves GeoLite2-Country
    get_asn_data()       # retrieves GeoLite2-ASN
    get_city_data()      # retrieves GeoLite2-City