class QEAgentPlanner:

    def decide_next_step(self, analysis):

        if not analysis:
            return "ANALYZE_REQUIREMENT"

        risk_level = analysis.get("risk_level", "Low")

        # High-risk requirements require
        # specialized QE risk analysis.
        if risk_level == "High":
            return "ANALYZE_QE_RISK"

        # No specialist agent required.
        return "NO_SPECIALIST_ACTION"