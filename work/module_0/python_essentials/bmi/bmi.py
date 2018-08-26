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