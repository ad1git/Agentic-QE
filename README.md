# Agentic-QE

AI-driven Quality Engineering agent that analyzes software requirements using a local LLM and produces structured QE insights.

The agent analyzes requirements for functional expectations, actors, business rules, acceptance criteria, ambiguities, missing information, negative scenarios, boundary conditions, testability, risk, and QE recommendations.

The project uses Python, Ollama, and Qwen2.5-Coder 7B to demonstrate how AI agents can support Quality Engineering activities.

> This is a hands-on project to demonstrate AI + QE engineering capabilities.

## Key Capabilities

- Read software requirements from text files
- Analyze requirements using a local LLM
- Identify ambiguities and missing information
- Identify negative scenarios and boundary conditions
- Assess requirement testability
- Assess requirement risk
- Generate QE recommendations
- Produce structured JSON output
- Validate the AI response structure
- Save analysis results
- Automated testing using pytest

## Architecture

                         Agentic-QE
                             │
                             ▼
                    Requirement Input
                             │
                             ▼
                ┌────────────────────────┐
                │ RequirementAnalysisAgent     │
                │        Agent            │
                └───────────┬────────────┘
                            │
                            ▼
                    Prompt Engineering
                            │
                            ▼
                ┌────────────────────────┐
                │ Ollama                  │
                │ Qwen2.5-Coder 7B       │
                │ Local LLM               │
                └───────────┬────────────┘
                            │
                            ▼
                    Structured JSON
                            │
                            ▼
                AI Output Validation
                            │
                            ▼
                     QE Analysis
                            │
          ┌─────────────────┼─────────────────┐
          ▼                 ▼                 ▼
      Testability          Risk          Ambiguities
          │                 │                 │
          └─────────────────┼─────────────────┘
                            ▼
                    QE Recommendation

## Technology Stack

| Technology       | Purpose                                 |
| ---------------- | --------------------------------------- |
| Python 3.14      | Application development                 |
| Ollama           | Local LLM runtime                       |
| Qwen2.5-Coder 7B | Local LLM used for requirement analysis |
| pytest           | Automated testing                       |
| JSON             | Structured AI output                    |
| pathlib          | File handling and path management       |
| VS Code          | Development environment                 |

## Project Structure
```text
Agentic-QE/
│
├── analyzer.py
├── main.py
├── app.py
├── README.md
├── requirements.txt
│
├── data/
│   ├── sample_requirement.txt
│   └── empty_requirement.txt
│
├── tests/
│   └── test_analyzer.py
│
└── output/
    └── .gitkeep

## QE Analysis Demonstration

Requirement

"The customer should be able to reset their password."

The agent analyzes the requirement from a QE perspective and produces structured insights covering:

Functional Requirements
Actors
Business Rules
Acceptance Criteria
Ambiguities
Missing Information
Negative Scenarios
Boundary Conditions
Testability
Risk
QE Recommendation

## Purpose

This project is being developed to demonstrate practical experience in applying Generative AI and agent-based approaches to Quality Engineering.

---

### Author

Developed by **ad1git** — AI-QE project for intelligent Quality Engineering. (Amardeep Sangwan)
