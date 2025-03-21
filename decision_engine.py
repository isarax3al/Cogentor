"""
AI-Human Collaborative Decision Engine
"""

from sklearn.ensemble import RandomForestClassifier
import numpy as np

class HumanDecisionModel:
    """Simulates human analyst decision patterns"""
    
    def __init__(self, expertise: str):
        self.bias_profile = {
            "novice": {"overconfidence": 0.4, "risk_aversion": 0.6},
            "expert": {"overconfidence": 0.1, "risk_aversion": 0.2}
        }[expertise]
    
    def adjust_risk(self, raw_score: float) -> float:
        """Applies human bias to AI risk score"""
        return raw_score * (1 - self.bias_profile["overconfidence"])
    
    def final_decision(self, adjusted_score: float) -> str:
        """Generates human-readable decision"""
        if adjusted_score > 0.8:
            return "Immediate Isolation Required"
        elif adjusted_score > 0.6:
            return "Enhanced Monitoring Recommended"
        else:
            return "Normal Operations"

class AIAnalyzer:
    """Machine Learning Threat Evaluation"""
    
    def __init__(self):
        self.model = RandomForestClassifier()
        self._train_model()
    
    def _train_model(self):
        """Trains ML model on historical data"""
        X_train = np.array([
            [0.9, 0.7, 0.8],  # Severity, Complexity, Urgency
            [0.6, 0.8, 0.9],
            [0.7, 0.6, 0.7]
        ])
        y_train = ["Critical", "High", "Medium"]
        self.model.fit(X_train, y_train)
    
    def evaluate_threat(self, scenario: dict) -> dict:
        """Generates AI threat assessment"""
        features = np.array([
            scenario["severity"],
            scenario["complexity"],
            scenario["urgency"]
        ]).reshape(1, -1)
        
        risk_level = self.model.predict(features)[0]
        return {
            "risk_score": self._calculate_score(features),
            "risk_level": risk_level,
            "recommendation": "Contain" if risk_level in ["Critical", "High"] else "Monitor"
        }
    
    def _calculate_score(self, features) -> float:
        """Calculates normalized risk score"""
        return np.dot(features, [0.6, 0.3, 0.1]).item()