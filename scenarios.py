"""
Scenario Management Module
"""

import json
from pathlib import Path

def load_scenario(scenario_name: str) -> dict:
    """Loads JSON scenario file"""
    scenarios_dir = Path(__file__).parent / "scenarios"
    target_file = scenarios_dir / f"{scenario_name}.json"
    
    if not target_file.exists():
        raise FileNotFoundError(f"Scenario file '{scenario_name}' not found")
    
    with open(target_file, 'r') as f:
        return json.load(f)

def generate_report(scenario: dict, ai_data: dict, human_decision: str) -> None:
    """Generates text report"""
    report_content = f"""=== Cybersecurity Decision Report ===
Scenario: {scenario['name']}
--------------------------------------
AI Analysis:
- Risk Score: {ai_data['risk_score']:.2f}
- Threat Level: {ai_data['risk_level']}
- Recommended Action: {ai_data['recommendation']}

Human Adjustment:
- Final Decision: {human_decision}"""
    
    reports_dir = Path(__file__).parent / "outputs"
    reports_dir.mkdir(exist_ok=True)
    
    with open(reports_dir / f"{scenario['name']}_report.txt", 'w') as f:
        f.write(report_content)