"""
CNC Speeds & Feeds Manager
Unit Conversion Module

Handles metric and imperial conversions
used by the CNC router calculation engine.

Python Version:
3.12+

Author:
TreySeesU
"""


# ==========================================================
# CONSTANTS
# ==========================================================

MM_PER_INCH = 25.4

INCH_PER_MM = 1 / MM_PER_INCH


METER_PER_FOOT = 0.3048

FOOT_PER_METER = 1 / METER_PER_FOOT


# ==========================================================
# DISTANCE CONVERSIONS
# ==========================================================

def mm_to_inches(
    millimeters: float
) -> float:

    """
    Convert millimeters to inches.

    Example:
        25.4 mm = 1 inch
    """

    return millimeters / MM_PER_INCH



def inches_to_mm(
    inches: float
) -> float:

    """
    Convert inches to millimeters.
    """

    return inches * MM_PER_INCH



# ==========================================================
# FEED RATE CONVERSIONS
# ==========================================================

def mm_min_to_in_min(
    feed_rate: float
) -> float:

    """
    Convert mm/min to inch/min.
    """

    return feed_rate / MM_PER_INCH



def in_min_to_mm_min(
    feed_rate: float
) -> float:

    """
    Convert inch/min to mm/min.
    """

    return feed_rate * MM_PER_INCH



# ==========================================================
# SURFACE SPEED CONVERSIONS
# ==========================================================

def meters_min_to_sfm(
    meters_per_minute: float
) -> float:

    """
    Convert meters/minute to surface feet/minute.

    Formula:
        m/min × 3.28084
    """

    return meters_per_minute * 3.28084



def sfm_to_meters_min(
    sfm: float
) -> float:

    """
    Convert surface feet/minute
    to meters/minute.
    """

    return sfm / 3.28084



# ==========================================================
# DIAMETER CONVERSIONS
# ==========================================================

def diameter_to_metric(
    value: float,
    unit: str
) -> float:

    """
    Convert diameter to millimeters.

    Accepted units:

        mm
        inch
    """

    unit = unit.lower()


    if unit in (
        "mm",
        "millimeter",
        "millimeters"
    ):

        return value


    if unit in (
        "inch",
        "in",
        "inches"
    ):

        return inches_to_mm(value)


    raise ValueError(
        f"Unknown diameter unit: {unit}"
    )



def diameter_to_imperial(
    value: float,
    unit: str
) -> float:

    """
    Convert diameter to inches.
    """

    unit = unit.lower()


    if unit in (
        "inch",
        "in",
        "inches"
    ):

        return value


    if unit in (
        "mm",
        "millimeter",
        "millimeters"
    ):

        return mm_to_inches(value)


    raise ValueError(
        f"Unknown diameter unit: {unit}"
    )



# ==========================================================
# FEED RATE NORMALIZATION
# ==========================================================

def normalize_feed_rate(
    value: float,
    unit: str
) -> float:

    """
    Convert any feed rate into mm/min.

    The calculation engine uses
    mm/min internally.
    """

    unit = unit.lower()


    if unit in (
        "mm/min",
        "mm/minute"
    ):

        return value


    if unit in (
        "in/min",
        "inch/min"
    ):

        return in_min_to_mm_min(value)


    raise ValueError(
        f"Unknown feed unit: {unit}"
    )



# ==========================================================
# OUTPUT FORMATTING
# ==========================================================

def format_distance(
    value_mm: float,
    system: str
) -> str:

    """
    Formats a distance for display.
    """

    if system.lower() == "metric":

        return (
            f"{value_mm:.3f} mm"
        )


    return (
        f"{mm_to_inches(value_mm):.4f} in"
    )



def format_feed_rate(
    value_mm_min: float,
    system: str
) -> str:

    """
    Formats feed rate for display.
    """

    if system.lower() == "metric":

        return (
            f"{value_mm_min:.0f} mm/min"
        )


    return (
        f"{mm_min_to_in_min(value_mm_min):.1f} in/min"
    )



def format_surface_speed(
    value_m_min: float,
    system: str
) -> str:

    """
    Formats surface speed.
    """

    if system.lower() == "metric":

        return (
            f"{value_m_min:.1f} m/min"
        )


    return (
        f"{meters_min_to_sfm(value_m_min):.0f} SFM"
    )



# ==========================================================
# UNIT VALIDATION
# ==========================================================

def validate_unit_system(
    system: str
) -> str:

    """
    Ensures a valid unit system.
    """

    system = system.lower()


    if system in (
        "metric",
        "imperial"
    ):

        return system


    raise ValueError(
        "Unit system must be metric or imperial"
    )



# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":

    print(
        "25.4 mm =",
        mm_to_inches(25.4),
        "in"
    )


    print(
        "1 inch =",
        inches_to_mm(1),
        "mm"
    )


    print(
        "10000 mm/min =",
        mm_min_to_in_min(10000),
        "in/min"
    )


    print(
        "500 m/min =",
        meters_min_to_sfm(500),
        "SFM"
    )
