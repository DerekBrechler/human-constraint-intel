def evaluate_state(state):
    output = []

    if state["elapsed_time"] > state["planned_duration"]:
        output.append("Mission exceeded planned time — drift detected.")

    fatigue_modifier = 1.25 if state["sleep_quality"] == "low" else 1.0
    adjusted_time = state["time_in_role"] * fatigue_modifier

    if adjusted_time > 90:
        output.append("Operator fatigue risk high due to poor sleep + time in role.")

    if state["RPE"] >= 8:
        output.append("High perceived exertion — consider rotating roles or pausing.")

    if not output:
        output.append("No fragility indicators triggered.")

    return output
