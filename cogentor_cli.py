"""
Command Line Interface for Cogentor System
"""

import argparse
from decision_engine import HumanDecisionModel, AIAnalyzer
from scenarios import load_scenario, generate_report

def main():
    # CLI Configuration
    parser = argparse.ArgumentParser(
        description="Cogentor: AI-Human Cybersecurity Decision System",
        epilog="Example: python cogentor_cli.py analyze --scenario=phishing --expertise=expert"
    )
    parser.add_argument("action", choices=["analyze", "report"], help="Operation mode")
    parser.add_argument("-s", "--scenario", required=True, help="Scenario filename")
    parser.add_argument("-e", "--expertise", choices=["novice", "expert"], default="expert", help="Analyst skill level")
    
    args = parser.parse_args()
    
    try:
        # Load Scenario
        scenario_data = load_scenario(args.scenario)
        
        # Initialize Models
        ai_engine = AIAnalyzer()
        human_model = HumanDecisionModel(args.expertise)
        
        # Process Request
        ai_result = ai_engine.evaluate_threat(scenario_data)
        human_score = human_model.adjust_risk(ai_result["risk_score"])
        
        if args.action == "analyze":
            print(f"\n🔍 Threat Analysis Report")
            print(f"- Scenario: {scenario_data['name']}")
            print(f"- AI Risk Level: {ai_result['risk_level']} ({ai_result['risk_score']:.2f})")
            print(f"- Human Adjusted Score: {human_score:.2f}")
            print(f"- Final Recommendation: {ai_result['recommendation'].upper()}")
            
        elif args.action == "report":
            generate_report(scenario_data, ai_result, human_model.final_decision(human_score))
            print(f"Report generated in outputs/ directory")
            
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()