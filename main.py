from logic_engine import fatigue_rules

# Simulated mission input
mission_state = {
    "elapsed_time": 10,  # hours
    "planned_duration": 8,
    "operator": "A",
    "role": "navigation",
    "time_in_role": 110,  # minutes
    "sleep_quality": "low",
    "RPE": 8
}

recommendations = fatigue_rules.evaluate_state(mission_state)

print("RECOMMENDATIONS:\n")
for r in recommendations:
    print(f"- {r}")
