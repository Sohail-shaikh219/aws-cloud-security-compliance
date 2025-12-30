from config import RISK_LEVELS


def calculate_risk_score(findings):
    score = 0
    for finding in findings:
        risk_level = finding[2]
        score += RISK_LEVELS.get(risk_level, 0)
    return score
