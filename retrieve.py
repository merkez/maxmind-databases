import os
from util import MaxMindDB

def get_license_key(license_key='MAXMIND_LICENSE_KEY'):
    """
    @param license_key: Name of environment variable
    @return: license of MaxMindDB from environent variables as string
    @return: in case of error, returns Exception, more specifically KeyError
    """
    try:
        maxmind_db_license = os.environ[license_key]
        return maxmind_db_license
    except Exception:
        print("\nWARNING: No MAXMIND LICENSE KEY Found in environment variables")
        print("Proceeding anyway...")
        return 'NOLICENSEKEYFOUND'


def get_country_data():
    """
    Download GeoLite2-Country data from MaxMind

    """
    _ = MaxMindDB((
        "https://download.maxmind.com/app/geoip_download?"
        "edition_id=GeoLite2-Country&"
        "license_key={license_key}&"
        "suffix=tar.gz"
    ).format(
        license_key=get_license_key(),
        ), "cc"
    )

def get_asn_data():
    """
    Download ASN data from MaxMind
    """
    _ = MaxMindDB((
            "https://download.maxmind.com/app/geoip_download?"
            "edition_id=GeoLite2-ASN&"
            "license_key={license_key}&"
            "suffix=tar.gz"
    ).format(
            license_key=get_license_key(),
    ), "asn"
    )


def get_city_data():
    """
    Download GeoLiteCity data from Maxmind DB
    """
    _ = MaxMindDB((
            "https://download.maxmind.com/app/geoip_download?"
            "edition_id=GeoLite2-City&"
            "license_key={license_key}&"
            "suffix=tar.gz"
    ).format(
            license_key=get_license_key(),
    ), "city"
    )
