class VitalSign:
    def __init__(self, systolic, diastolic, heart_rate):
        self.systolic = systolic
        self.diastolic = diastolic
        self.heart_rate = heart_rate

class Condition:
    def __init__(self, name, severity):
        self.name = name
        self.severity = severity

class HeartFailure:
    def __init__(self, stage, condition):
        self.stage = stage  # e.g., A, B, C, D
        self.condition = condition  # instance of Condition

class Treatment:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Score:
    def __init__(self, value, patient):
        self.value = value
        self.patient = patient  # Reference to a Patient class

# Relationships
# - VitalSign can be linked to multiple Conditions
a_condition = Condition("Hypertension", "Moderate")
vital_sign = VitalSign(120, 80, 75)  # Sample vital sign

# - HeartFailure may involve multiple Conditions and their Severity
heart_failure = HeartFailure("B", a_condition)

# - Treatment can be related to HeartFailure

# - Score may relate to Treatment and HeartFailure instances
