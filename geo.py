import math

def haversine(coord1, coord2):
    sin = math.sin
    cos = math.cos
    arctan = math.atan2
    RAD = math.pi / 180
    lat1 = coord1[0] * RAD
    lat2 = coord2[0] * RAD
    long1 = coord1[1] * RAD
    long2 = coord2[1] * RAD
    R = 3959

    a = sin((lat2 - lat1) / 2) ** 2 + cos(lat1) * cos(lat2) * sin((long2 - long1) / 2) ** 2
    return 2 * R * arctan(math.sqrt(a), math.sqrt(1 - a))
