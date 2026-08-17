import json
from ollama import chat


class QERiskAgent:

    def __init__(self, model="qwen2.5-coder:7b"):
        self.model = model

    def analyze_risk(self, analysis):

        prompt = f"""
You are a Quality Engineering Risk Analysis Agent.

Review the following requirement analysis.

REQUIREMENT ANALYSIS:
{json.dumps(analysis, indent=2)}

Identify the most important QE risks.

Return ONLY valid JSON with exactly these fields:

{{
  "risk_level": "Low|Medium|High",
  "key_risks": [],
  "risk_reason": "",
  "recommended_qe_actions": []
}}

Rules:
- Base the analysis only on the supplied requirement analysis.
- Do not invent facts.
- Focus on practical software quality risks.
- Keep the response concise.
"""

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