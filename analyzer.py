import json
from pathlib import Path
from ollama import chat


class RequirementAnalysisAgent:
    def __init__(self, model="qwen2.5-coder:7b"):
        self.model = model

    def read_requirement(self, file_name):
        path = Path(file_name)
        if not path.exists():
            raise FileNotFoundError(file_name)

        requirement = path.read_text(encoding="utf-8").strip()

        if not requirement:
            raise ValueError("The requirement file is empty.")

        return requirement

    def build_prompt(self, requirement):
        return f"""
You are an experienced Quality Engineering Requirement Analyzer.

Analyze the following software requirement from a QE perspective.

REQUIREMENT:
{requirement}

Return ONLY valid JSON with exactly these top-level fields:

{{
  "requirement_summary": "",
  "actors": [],
  "functional_requirements": [],
  "business_rules": [],
  "acceptance_criteria": [],
  "ambiguities": [],
  "missing_information": [],
  "negative_scenarios": [],
  "boundary_conditions": [],
  "testability_score": 0,
  "testability_reason": "",
  "risk_level": "Low|Medium|High",
  "qe_recommendation": ""
}}

Rules:
- Do not invent facts that are not supported by the requirement.
- If something is unclear, put it under ambiguities or missing_information.
- Acceptance criteria should be measurable and testable.
- Negative scenarios should identify realistic failure conditions.
- Boundary conditions should identify limits, minimums, maximums, empty/null cases, and invalid values when applicable.
- testability_score must be an integer from 1 to 10.
- Keep the response concise but useful for a QE team.
"""

    def analyze(self, requirement):
        prompt = self.build_prompt(requirement)

        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            format="json"
        )

        content = response["message"]["content"]
        return json.loads(content)
    def validate_analysis_result(self, result):
        required_fields = [
        "requirement_summary",
        "actors",
        "functional_requirements",
        "business_rules",
        "acceptance_criteria",
        "ambiguities",
        "missing_information",
        "negative_scenarios",
        "boundary_conditions",
        "testability_score",
        "testability_reason",
        "risk_level",
        "qe_recommendation"
        ]

        for field in required_fields:
            if field not in result:
                return False

        return True

    def analyze_file(self, file_name):
        requirement = self.read_requirement(file_name)
        return self.analyze(requirement)

    def save_result(self, result, output_file):
        path = Path(output_file)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(
            json.dumps(result, indent=2, ensure_ascii=False),
            encoding="utf-8"
        )

    def print_report(self, result):
        print("\n" + "=" * 70)
        print("REQUIREMENT ANALYSIS")
        print("=" * 70)

        print("\nSummary:")
        print(result.get("requirement_summary", ""))

        print("\nActors:")
        for item in result.get("actors", []):
            print(f"  - {item}")

        print("\nFunctional Requirements:")
        for item in result.get("functional_requirements", []):
            print(f"  - {item}")

        print("\nBusiness Rules:")
        for item in result.get("business_rules", []):
            print(f"  - {item}")

        print("\nAcceptance Criteria:")
        for item in result.get("acceptance_criteria", []):
            print(f"  - {item}")

        print("\nAmbiguities:")
        for item in result.get("ambiguities", []):
            print(f"  - {item}")

        print("\nMissing Information:")
        for item in result.get("missing_information", []):
            print(f"  - {item}")

        print("\nNegative Scenarios:")
        for item in result.get("negative_scenarios", []):
            print(f"  - {item}")

        print("\nBoundary Conditions:")
        for item in result.get("boundary_conditions", []):
            print(f"  - {item}")

        print(f"\nTestability Score: {result.get('testability_score', '')}/10")
        print(f"Reason: {result.get('testability_reason', '')}")
        print(f"Risk Level: {result.get('risk_level', '')}")

        print("\nQE Recommendation:")
        print(result.get("qe_recommendation", ""))

        
