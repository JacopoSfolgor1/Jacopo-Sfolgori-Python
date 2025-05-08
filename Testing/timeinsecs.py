def seconds_since_noon(ore: int, mins: int, secs: int) -> int:
    return (ore * 3600 + mins * 60 + secs) - (12 * 3600)

def time_difference(ore1: int, mins1: int, secs1: int, ore2: int, mins2: int, secs2: int) -> int:
    return abs(seconds_since_noon(ore1, mins1, secs1) - seconds_since_noon(ore2, mins2, secs2))
