"""
CNC Speeds & Feeds Manager
Warning and Safety Analysis Module

Evaluates calculated CNC router parameters
and generates safety warnings.

Python Version:
3.12+

Author:
TreySeesU
"""


# ==========================================================
# WARNING LEVELS
# ==========================================================

WARNING_LEVELS = {

    "INFO": 1,

    "CAUTION": 2,

    "WARNING": 3,

    "CRITICAL": 4

}



# ==========================================================
# WARNING CREATION
# ==========================================================

def create_warning(
    level: str,
    message: str
) -> dict:

    """
    Creates a standardized warning object.
    """

    return {

        "level": level,

        "severity": WARNING_LEVELS.get(
            level,
            1
        ),

        "message": message

    }



# ==========================================================
# RPM CHECKS
# ==========================================================

def check_rpm(
    rpm: float,
    machine_max_rpm: float,
    tool_max_rpm: float | None = None
) -> list:

    """
    Checks spindle speed limits.
    """

    warnings = []


    if rpm > machine_max_rpm:

        warnings.append(
            create_warning(
                "CRITICAL",
                (
                    f"Calculated RPM ({rpm:.0f}) "
                    f"exceeds machine maximum "
                    f"RPM ({machine_max_rpm:.0f})."
                )
            )
        )


    if tool_max_rpm:

        if rpm > tool_max_rpm:

            warnings.append(
                create_warning(
                    "WARNING",
                    (
                        f"Calculated RPM ({rpm:.0f}) "
                        f"exceeds tool maximum RPM "
                        f"({tool_max_rpm:.0f})."
                    )
                )
            )


    return warnings



# ==========================================================
# FEED RATE CHECKS
# ==========================================================

def check_feed_rate(
    feed_rate: float,
    machine_max_feed: float
) -> list:

    """
    Checks machine feed limitations.
    """

    warnings = []


    if feed_rate > machine_max_feed:

        warnings.append(
            create_warning(
                "CRITICAL",
                (
                    f"Calculated feed rate "
                    f"({feed_rate:.0f}) exceeds "
                    f"machine maximum feed rate "
                    f"({machine_max_feed:.0f})."
                )
            )
        )


    if feed_rate < 100:

        warnings.append(
            create_warning(
                "CAUTION",
                (
                    "Feed rate is very low. "
                    "Tool rubbing and heat buildup "
                    "may occur."
                )
            )
        )


    return warnings



# ==========================================================
# CHIPLOAD CHECKS
# ==========================================================

def check_chipload(
    chipload: float,
    minimum: float,
    maximum: float
) -> list:

    """
    Checks chipload against material/tool
    recommendations.
    """

    warnings = []


    if chipload < minimum:

        warnings.append(
            create_warning(
                "WARNING",
                (
                    f"Chipload ({chipload:.3f}) "
                    f"is below recommended minimum "
                    f"({minimum:.3f}). "
                    "Possible tool rubbing or burning."
                )
            )
        )


    if chipload > maximum:

        warnings.append(
            create_warning(
                "WARNING",
                (
                    f"Chipload ({chipload:.3f}) "
                    f"exceeds recommended maximum "
                    f"({maximum:.3f}). "
                    "Possible tool overload."
                )
            )
        )


    return warnings



# ==========================================================
# DEPTH OF CUT CHECKS
# ==========================================================

def check_depth_of_cut(
    depth_of_cut: float,
    tool_diameter: float,
    depth_factor: float
) -> list:

    """
    Checks axial depth of cut.
    """

    warnings = []


    recommended_depth = (
        tool_diameter *
        depth_factor
    )


    if depth_of_cut > recommended_depth:

        warnings.append(
            create_warning(
                "WARNING",
                (
                    f"Depth of cut ({depth_of_cut:.2f} mm) "
                    f"exceeds recommended depth "
                    f"({recommended_depth:.2f} mm)."
                )
            )
        )


    return warnings



# ==========================================================
# STEPOVER CHECKS
# ==========================================================

def check_stepover(
    stepover: float,
    tool_diameter: float
) -> list:

    """
    Checks radial engagement.
    """

    warnings = []


    percentage = (
        stepover /
        tool_diameter
    ) * 100


    if percentage > 75:

        warnings.append(
            create_warning(
                "CAUTION",
                (
                    f"Large stepover detected "
                    f"({percentage:.0f}% of tool diameter). "
                    "Consider reducing engagement."
                )
            )
        )


    return warnings



# ==========================================================
# PLUNGE CHECKS
# ==========================================================

def check_plunge_rate(
    plunge_rate: float,
    feed_rate: float
) -> list:

    """
    Checks plunge rate compared to cutting feed.
    """

    warnings = []


    if plunge_rate > feed_rate:

        warnings.append(
            create_warning(
                "WARNING",
                (
                    "Plunge rate exceeds cutting "
                    "feed rate."
                )
            )
        )


    if plunge_rate > (
        feed_rate * 0.75
    ):

        warnings.append(
            create_warning(
                "CAUTION",
                (
                    "Plunge rate is high. "
                    "Verify tool geometry and "
                    "material."
                )
            )
        )


    return warnings



# ==========================================================
# COMPLETE ANALYSIS
# ==========================================================

def analyze_cut(
    rpm,
    machine_max_rpm,
    feed_rate,
    machine_max_feed,
    chipload=None,
    chipload_min=None,
    chipload_max=None,
    depth_of_cut=None,
    tool_diameter=None,
    depth_factor=None,
    stepover=None,
    plunge_rate=None,
    tool_max_rpm=None
) -> list:

    """
    Runs all safety checks.

    Returns:
        List of warning dictionaries.
    """

    warnings = []


    warnings.extend(
        check_rpm(
            rpm,
            machine_max_rpm,
            tool_max_rpm
        )
    )


    warnings.extend(
        check_feed_rate(
            feed_rate,
            machine_max_feed
        )
    )


    if (
        chipload is not None
        and
        chipload_min is not None
        and
        chipload_max is not None
    ):

        warnings.extend(
            check_chipload(
                chipload,
                chipload_min,
                chipload_max
            )
        )


    if (
        depth_of_cut is not None
        and
        tool_diameter is not None
        and
        depth_factor is not None
    ):

        warnings.extend(
            check_depth_of_cut(
                depth_of_cut,
                tool_diameter,
                depth_factor
            )
        )


    if (
        stepover is not None
        and
        tool_diameter is not None
    ):

        warnings.extend(
            check_stepover(
                stepover,
                tool_diameter
            )
        )


    if (
        plunge_rate is not None
        and
        feed_rate is not None
    ):

        warnings.extend(
            check_plunge_rate(
                plunge_rate,
                feed_rate
            )
        )


    return warnings



# ==========================================================
# WARNING SUMMARY
# ==========================================================

def summarize_warnings(
    warnings: list
) -> str:

    """
    Converts warnings into a database-friendly
    text summary.
    """

    if not warnings:

        return "No warnings."


    messages = []


    for warning in warnings:

        messages.append(

            f"{warning['level']}: "
            f"{warning['message']}"

        )


    return "\n".join(messages)



# ==========================================================
# TEST
# ==========================================================

if __name__ == "__main__":


    results = analyze_cut(

        rpm=28000,

        machine_max_rpm=24000,

        feed_rate=16000,

        machine_max_feed=12000,

        chipload=0.45,

        chipload_min=0.15,

        chipload_max=0.30

    )


    for item in results:

        print(
            item["level"],
            "-",
            item["message"]
        )
