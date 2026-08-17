from analyzer import RequirementAnalysisAgent
from planner import QEAgentPlanner
from risk_agent import QERiskAgent


class AgenticQE:

    def __init__(self, model="qwen2.5-coder:7b"):

        self.analyzer = RequirementAnalysisAgent(model)
        self.planner = QEAgentPlanner()
        self.risk_agent = QERiskAgent(model)

    def run(self, requirement_file):

        print("\n" + "=" * 70)
        print("AGENTIC QE")
        print("=" * 70)

        # --------------------------------------------------
        # STEP 1: READ REQUIREMENT
        # --------------------------------------------------

        print("\n[AGENT 1] Reading requirement...")

        requirement = self.analyzer.read_requirement(
            requirement_file
        )

        print("Requirement loaded.")

        # --------------------------------------------------
        # STEP 2: ANALYZE REQUIREMENT
        # --------------------------------------------------

        print("\n[AGENT 1] Analyzing requirement...")

        analysis = self.analyzer.analyze(
            requirement
        )

        print("Requirement analysis completed.")

        # Validate LLM output
        if not self.analyzer.validate_analysis_result(analysis):
            raise ValueError(
                "Requirement analysis failed validation."
            )

        print("Analysis validation: PASSED")

        # --------------------------------------------------
        # STEP 3: PLANNER DECIDES NEXT ACTION
        # --------------------------------------------------

        print("\n[PLANNER] Deciding next action...")

        next_action = self.planner.decide_next_step(
            analysis
        )

        print(f"Planner decision: {next_action}")

        # --------------------------------------------------
        # STEP 4: EXECUTE QE RISK AGENT
        # --------------------------------------------------

        if next_action == "ANALYZE_QE_RISK":

            print("\n[RISK AGENT] Analyzing QE risks...")

            risk_result = self.risk_agent.analyze_risk(
                analysis
            )

            print("Risk analysis completed.")

            return {
                "requirement_analysis": analysis,
                "planner_decision": next_action,
                "risk_analysis": risk_result
            }

        # --------------------------------------------------
        # STEP 5: NO SPECIALIST AGENT REQUIRED
        # --------------------------------------------------

        return {
            "requirement_analysis": analysis,
            "planner_decision": next_action
        }