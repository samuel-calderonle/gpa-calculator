# gpa_engine.py

grade_values = {
    "A": 4.0,
    "B": 3.0,
    "C": 2.0,
    "D": 1.0,
    "F": 0.0
}

weight_boost = {
    "Regular": 0.0,
    "Honors": 0.04,
    "AP / DE": 0.08
}


def calculate_gpa(courses: list[dict]) -> tuple[float, float]:
    """
    Takes a list of course dicts and returns (unweighted_gpa, weighted_gpa).
    Weighted GPA = Unweighted GPA + sum(weight_boost * credits) for non-F grades.
    """
    if not courses:
        return (0.0, 0.0)

    total_quality_points = 0.0
    total_credits = 0.0
    add_on_points = 0.0

    for course in courses:
        credits = float(course["credits"])
        grade = course["grade"]
        level = course["level"]

        total_credits += credits
        total_quality_points += grade_values[grade] * credits

        if grade != "F":
            add_on_points += weight_boost[level] * credits

    if total_credits == 0:
        return (0.0, 0.0)

    unweighted_gpa = total_quality_points / total_credits
    weighted_gpa = unweighted_gpa + add_on_points

    return (round(unweighted_gpa, 3), round(weighted_gpa, 3))
