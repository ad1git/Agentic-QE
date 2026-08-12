import json
from ollama import chat


class TCGenerationAgent:

    def __init__(self, model="qwen2.5-coder:7b"):
        self.model = model

    def build_prompt(self, qe_analysis):
        return f"""
You are a Test Case Generation Agent.

Use the QE analysis below to generate concise software test cases.

QE Analysis:
{json.dumps(qe_analysis, indent=2)}

Generate test cases covering the identified scenarios.

Return ONLY valid JSON in this format:

{{
  "test_cases": [
    {{
      "test_case_id": "TC001",
      "scenario": "...",
      "test_type": "Positive",
      "precondition": "...",
      "test_steps": [
        "...",
        "..."
      ],
      "expected_result": "...",
      "priority": "High"
    }}
  ]
}}

Rules:
- test_type must be Positive, Negative, or Boundary.
- priority must be High, Medium, or Low.
- Keep the test cases concise.
"""

    def generate_test_cases(self, qe_analysis):
        response = chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": self.build_prompt(qe_analysis)
                }
            ],
            format="json"
        )

        return json.loads(response["message"]["content"])

    def validate_test_cases(self, result):
        required_fields = {
            "test_case_id",
            "scenario",
            "test_type",
            "precondition",
            "test_steps",
            "expected_result",
            "priority"
        }

        if "test_cases" not in result:
            return False

        if not isinstance(result["test_cases"], list):
            return False

        for test_case in result["test_cases"]:
            if not required_fields.issubset(test_case.keys()):
                return False

        return True