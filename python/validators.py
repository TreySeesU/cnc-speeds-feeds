"""
CNC Speeds & Feeds Manager
Validation Module

Validates input data before calculations
are performed.

Python Version:
3.12+

Author:
TreySeesU
"""


# ==========================================================
# GENERIC VALIDATORS
# ==========================================================

def is_positive_number(value) -> bool:

    """
    Checks if a value is a positive number.
    """

    try:

        return float(value) > 0

    except (TypeError, ValueError):

        return False



def is_non_negative(value) -> bool:

    """
    Checks if a value is zero or positive.
    """

    try:

        return float(value) >= 0

    except (TypeError, ValueError):

        return False



def is_positive_integer(value) -> bool:

    """
    Checks for positive integers.
    """

    try:

        return int(value) > 0

    except (TypeError, ValueError):

        return False



# ==========================================================
# TOOL VALIDATION
# ==========================================================

def validate_tool(tool: dict) -> list:

    """
    Validates CNC tool information.

    Returns:
        List of validation errors.

    Empty list means valid.
    """

    errors = []


    if not tool.get("name"):

        errors.append(
            "Tool name is required."
        )


    if not is_positive_number(
        tool.get("diameter")
    ):

        errors.append(
            "Tool diameter must be greater than zero."
        )


    if not is_positive_integer(
        tool.get("flute_count")
    ):

        errors.append(
            "Flute count must be greater than zero."
        )


    if tool.get("max_rpm"):

        if not is_positive_integer(
            tool.get("max_rpm")
        ):

            errors.append(
                "Maximum RPM must be positive."
            )


    return errors



# ==========================================================
# MATERIAL VALIDATION
# ==========================================================

def validate_material(material: dict) -> list:

    """
    Validates material information.
    """

    errors = []


    if not material.get("name"):

        errors.append(
            "Material name is required."
        )


    if material.get("chipload_min"):

        if not is_positive_number(
            material.get("chipload_min")
        ):

            errors.append(
                "Minimum chipload must be positive."
            )


    if material.get("chipload_max"):

        if not is_positive_number(
            material.get("chipload_max")
        ):

            errors.append(
                "Maximum chipload must be positive."
            )


    if (

        material.get("chipload_min")
        and
        material.get("chipload_max")

    ):

        if (

            material["chipload_min"]
            >
            material["chipload_max"]

        ):

            errors.append(
                "Minimum chipload cannot exceed maximum chipload."
            )


    return errors



# ==========================================================
# MACHINE VALIDATION
# ==========================================================

def validate_machine(machine: dict) -> list:

    """
    Validates CNC machine settings.
    """

    errors = []


    if not machine.get("name"):

        errors.append(
            "Machine name is required."
        )


    if not is_positive_integer(
        machine.get("spindle_max_rpm")
    ):

        errors.append(
            "Maximum spindle RPM must be positive."
        )


    if not is_positive_number(
        machine.get("max_feed_rate")
    ):

        errors.append(
            "Maximum feed rate must be positive."
        )


    if machine.get("max_depth"):

        if not is_positive_number(
            machine.get("max_depth")
        ):

            errors.append(
                "Maximum depth must be positive."
            )


    return errors



# ==========================================================
# CALCULATION INPUT VALIDATION
# ==========================================================

def validate_calculation_input(
    calculation: dict
) -> list:

    """
    Validates calculation parameters.
    """

    errors = []


    required_fields = [

        "material_id",

        "tool_id",

        "machine_id",

        "depth_of_cut"

    ]


    for field in required_fields:

        if field not in calculation:

            errors.append(
                f"Missing required field: {field}"
            )


    if "depth_of_cut" in calculation:


        if not is_positive_number(
            calculation["depth_of_cut"]
        ):

            errors.append(
                "Depth of cut must be positive."
            )


    if "spindle_rpm" in calculation:


        if not is_positive_integer(
            calculation["spindle_rpm"]
        ):

            errors.append(
                "Spindle RPM must be positive."
            )


    return errors



# ==========================================================
# UNIT VALIDATION
# ==========================================================

def validate_unit_system(
    system: str
) -> bool:

    """
    Validates metric/imperial selection.
    """

    if not isinstance(
        system,
        str
    ):

        return False


    return system.lower() in (

        "metric",

        "imperial"

    )



# ==========================================================
# RANGE VALIDATION
# ==========================================================

def validate_rpm(
    rpm: int
) -> list:

    """
    General spindle RPM validation.
    """

    errors = []


    if rpm < 100:

        errors.append(
            "RPM value appears too low."
        )


    if rpm > 60000:

        errors.append(
            "RPM exceeds typical CNC router limits."
        )


    return errors



def validate_feed_rate(
    feed_rate: float
) -> list:

    """
    General feed rate validation.
    """

    errors = []


    if feed_rate <= 0:

        errors.append(
            "Feed rate must be greater than zero."
        )


    if feed_rate > 50000:

        errors.append(
            "Feed rate exceeds typical CNC router limits."
        )


    return errors



# ==========================================================
# VALIDATION SUMMARY
# ==========================================================

def validate_all(
    tool=None,
    material=None,
    machine=None,
    calculation=None
) -> list:

    """
    Runs all available validation checks.
    """

    errors = []


    if tool:

        errors.extend(
            validate_tool(tool)
        )


    if material:

        errors.extend(
            validate_material(material)
        )


    if machine:

        errors.extend(
            validate_machine(machine)
        )


    if calculation:

        errors.extend(
            validate_calculation_input(
                calculation
            )
        )


    return errors



# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":


    example_tool = {

        "name": "6mm Compression",

        "diameter": 6,

        "flute_count": 2,

        "max_rpm": 24000

    }


    print(
        validate_tool(example_tool)
    )
