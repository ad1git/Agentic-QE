from analyzer import RequirementAnalysisAgent

def main():
    print("=" * 70)
    print("AI QE - Requirement Analyzer Agent")
    print("=" * 70)

    file_name = input("Enter requirement file name [requirement.txt]: ").strip()
    if not file_name:
        file_name = "requirement.txt"

    analyzer = RequirementAnalysisAgent()

    try:
        result = analyzer.analyze_file(file_name)
        analyzer.save_result(result, "output/requirement_analysis.json")
        analyzer.print_report(result)
    except FileNotFoundError:
        print(f"\nERROR: Could not find '{file_name}'.")
        print("Place the requirement file in the project folder and try again.")
    except Exception as exc:
        print(f"\nERROR: {exc}")

if __name__ == "__main__":
    main()
