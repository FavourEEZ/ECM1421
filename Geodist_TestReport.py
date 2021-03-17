# Script to verify the function within geordist.py works as expected
import math

def accurate_distance( latlngA, latlngB):
    '''
    Function to test if the distance produced from the geodist.py script is accurate
    Allowing a 10% deviation range 
    '''
    R = 6371.009 # approximate radius of earth surface (radius from center
                 # of the sphere in km)

    latA, lngA = latlngA
    lngA = math.radians(lngA)
    latA = math.radians(latA)
    latB, lngB = latlngB
    lngB = math.radians(lngB)
    latB = math.radians(latB)
    x = ( lngB - lngA ) * math.cos( (latA + latB) / 2 )
    y = latB - latA
    d = math.sqrt( x*x + y*y ) * R

    # We would expect the Distance to be 170 km, allowing a 10% deviation
    # Result, makes sure that d should be withtin the range specified
    result = 160 < d < 180
    assert result, 'Distance should be greater than 160 km, and less than 180 km'
    return d

accurate_distance((50.0678,5.7097),(50.7365,3.5344))
# Lat and Long for Land's end, Cornwall: 50.0678,5.7097
# Lat and Long for Exeter Uni: 50.7365,3.5344

def swapped_distance( latlngA, latlngB):
    '''
    Function to test if we swap latlngA and latlngB, we still get the same distance
    '''
    R = 6371.009 # approximate radius of earth surface (radius from center
                 # of the sphere in km)

    latA, lngA = latlngA
    lngA = math.radians(lngA)
    latA = math.radians(latA)
    latB, lngB = latlngB
    lngB = math.radians(lngB)
    latB = math.radians(latB)
    x = ( lngB - lngA ) * math.cos( (latA + latB) / 2 )
    y = latB - latA
    d = math.sqrt( x*x + y*y ) * R

    # We would expect the Distance to be the same as distance from accurate_distance()
    assert d == 171.16866697877865, 'Distance should be 171.16866697877865 km'
    return d

swapped_distance((50.7365,3.5344),(50.0678,5.7097))
# Lat and Long for Exeter Uni: 50.7365,3.5344
# Lat and Long for Land's end, Cornwall: 50.0678,5.7097

def smaller_distance( latlngA, latlngB):
    '''
    Function to test if the distance produced from the geodist.py script is accurate
    when using a smaller distance range (allowing 10% deviation) 
    '''
    R = 6371.009 # approximate radius of earth surface (radius from center
                 # of the sphere in km)

    latA, lngA = latlngA
    lngA = math.radians(lngA)
    latA = math.radians(latA)
    latB, lngB = latlngB
    lngB = math.radians(lngB)
    latB = math.radians(latB)
    x = ( lngB - lngA ) * math.cos( (latA + latB) / 2 )
    y = latB - latA
    d = math.sqrt( x*x + y*y ) * R

    # We would expect the Distance to be 1 km, allowing a 10% deviation
    # Result variable checks that d is within the specified range 
    result = 0.9 < d < 1.1
    assert result, 'Distance should be greater than 0.9 km, and less than 1.1 km'
    return d

smaller_distance((50.7365,3.5344),(50.728,3.5322))
# Lat and Long for Exeter Uni: 50.7365,3.5344
# Lat and Long for HM Prsion Exeter: 50.728,3.5322

