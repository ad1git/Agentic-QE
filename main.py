from analyzer import RequirementAnalysisAgent


def main():
    print("\n" + "=" * 70)
    print("AI QE REQUIREMENT ANALYZER")
    print("=" * 70)

    requirement_file = "data/sample_requirement.txt"
    output_file = "output/requirement_analysis.json"

    print(f"\nRequirement: {requirement_file}")
    print("Analyzing requirement with local AI...\n")

    analyzer = RequirementAnalysisAgent()

    result = analyzer.analyze_file(requirement_file)

    if analyzer.validate_analysis_result(result):
        print("AI output validation: PASSED")
    else:
        print("AI output validation: FAILED")
        return

    analyzer.print_report(result)

    analyzer.save_result(result, output_file)

    print(f"\nAnalysis saved to: {output_file}")
    print("\nAnalysis completed successfully.")
    print("=" * 70)


if __name__ == "__main__":
    main()