import pytest
from decision_engine import AIAnalyzer, HumanDecisionModel

def test_ai_analysis():
    
    analyzer = AIAnalyzer()
    scenario = {"severity": 0.9, "complexity": 0.7, "urgency": 0.8}
    result = analyzer.evaluate_threat(scenario)
    
    assert result["risk_score"] >= 0, "Risk score cannot be negative"
    assert result["recommendation"] in ["Contain", "Monitor"]

def test_human_bias():
    
    human_model = HumanDecisionModel("novice")
    adjusted_score = human_model.adjust_risk(0.85)
    
    assert adjusted_score <= 0.85 * 0.6, "Novice overconfidence not applied correctly"