def validate_input(scenario, tone, reason):
    if not scenario or not tone or not reason:
        return False
    if len(reason) < 3:
        return False
    return True
