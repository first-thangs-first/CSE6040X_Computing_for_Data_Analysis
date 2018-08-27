def in2m(inches):
    """Convert inches to meters according to convsersion rule 1m == 39.3701in

    Parameters:
    inches: float

    Return:
    float

    Usage examples:
    >>> abs(in2m(39.3701) - 1) < .01
    True
    """
    METER_IN_INCHES = 39.3701
    return inches / METER_IN_INCHES


def lb2kg(pounds):
    """Convert pounds to kilograms according to convsersion rule 1kg == 2.2lb

    Parameters:
    pounds: float

    Usage examples:
    >>> abs(lb2kg(2.2) - 1) < .01
    1
    """
    KG_IN_LBS = 2.2
    return pounds / KG_IN_LBS


def bmi(weight, height):
    """Calculate body mass index (BMI) for given weight and height.

    Paramters:
    weight: float -- weight in kilograms
    height: float -- height in meters

    Return:
    float -- BMI calculated by weight / (height **2)

    Usage examples:
    >>> abs(bmi(66, 1.72) - 22.309) < .01
    True
    """
    return weight / (height ** 2)


def is_overwieght(weight, height):
    """Answer whether the given weight and height is considered overweight
    by government standards (BMI > 25).

    Paramters:
    weight: float -- weight in kilograms
    height: float -- height in meters

    Return:
    bool: True if BMI for weight and height is greater than 25, False otherwise

    Usage examples:
    >>> is_overwieght(74, 1.72)
    True
    >>> is_overwieght(73, 1.72)
    False
    """
    return bmi(weight, height) > 25.0


def is_underweight(weight, height):
    """Answer whether the given weight and height is considered underweight
    by government standards (BMI < 18.5).

    Paramters:
    weight: float -- weight in kilograms
    height: float -- height in meters

    Return:
    bool: True if BMI for weight and height is less than 18.5, False otherwise

    Usage examples:
    >>> is_underweight(54, 1.72)
    True
    >>> is_underweight(55, 1.72)
    False
    """
    return bmi(weight, height) < 18.5


def split(text, delim=","):
    """Return a list of fields in text separated by delim.

    Parameters:
    text: str -- the string to split into fields

    Return:
    list[str]

    Usage examples:
    >>> split("foo, bar, baz")
    ['foo', ' bar', ' baz']
    """
    return text.split(delim)


def zip(xs, ys):
    """Return [(x0, y0), ..., (xn, yn)] where n is 1 - min(len(xs), len(ys))

    Parameters:
    xs: Sequence -- the "left" list
    ys: Sequence -- the "right list

    Return:
    list[tuple]

    Usage examples:
    >>> zip(['a', 'b', 'c', 'd'], [1,2,3])
    [('a', 1), ('b', 2), ('c', 3)]
    """
    return [(xs[index], ys[index]) for index in range(min(len(xs), len(ys)))]


def zip_with_indexes(xs):
    """Return [(0, x0), ..., (n, xn)] where n is 1 - len(xs)

    Parameters:
    xs: Sequence -- a sequence

    Return:
    list[tuple]

    Usage examples:
    >>> zip_with_indexes(['a', 'b', 'c', 'd'])
    [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
    """
    return [(index, xs[index]) for index in range(len(xs))]


def lookup_key(v, d):
    """Return a key in dict d which maps to v, or None if v isn't present

    Parameters:
    v: Any -- a value which may be in dictionary d
    d, : dict -- a dictionary which may contain the value v

    Return:
    Any

    Usage examples:
    >>> lookup_key(1, {'a': 1, 1: 'b', 'c': 2})
    'a'
    """
    result = None
    for key, value in d.items():
        if value == v:
            result = key
    return result


def lookup_keys(v, d):
    """Return list of keys in dict d which map to value

    Parameters:
    v: Any -- a value which may be in dictionary d
    d, : dict -- a dictionary which may contain the value v

    Return:
    list[Any]

    Usage examples:
    >>> lookup_keys(1, {'a': 1, 1: 'b', 'c': 2, 'd': 1})
    ['a', 'd']
    """
    result = []
    for key, value in d.items():
        if value == v:
            result.append(key)
    return result
