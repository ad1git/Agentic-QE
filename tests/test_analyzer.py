from analyzer import RequirementAnalyzer


def test_read_requirement():
    analyzer = RequirementAnalyzer()

    requirement = analyzer.read_requirement(
        "data/sample_requirement.txt"
    )

    assert requirement
    assert "reset their password" in requirement


def test_read_requirement_file_not_found():
    analyzer = RequirementAnalyzer()

    try:
        analyzer.read_requirement("data/does_not_exist.txt")
        assert False, "Expected FileNotFoundError"
    except FileNotFoundError:
        pass


def test_read_requirement_empty_file():
    analyzer = RequirementAnalyzer()

    try:
        analyzer.read_requirement("data/empty_requirement.txt")
        assert False, "Expected ValueError"
    except ValueError:
        pass

def test_validate_analysis_result():
    analyzer = RequirementAnalyzer()

    result = {
        "requirement_summary": "Customer can reset their password.",
        "actors": ["Customer"],
        "functional_requirements": ["Customer can reset their password."],
        "business_rules": [],
        "acceptance_criteria": [],
        "ambiguities": [],
        "missing_information": [],
        "negative_scenarios": [],
        "boundary_conditions": [],
        "testability_score": 8,
        "testability_reason": "The requirement is reasonably clear.",
        "risk_level": "Medium",
        "qe_recommendation": "Clarify password reset behavior."
    }

    assert analyzer.validate_analysis_result(result) is True