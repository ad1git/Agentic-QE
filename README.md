# Agentic-QE

Agentic AI-based Quality Engineering solution that analyzes software requirements, makes QE decisions based on the analysis, and invokes a specialized QE Risk Agent when required.

> This is a hands-on project demonstrating Agentic AI and Quality Engineering capabilities.

## Key Capabilities

- Read software requirements from text files
- Analyze requirements using a local LLM
- Identify functional requirements, actors, and business rules
- Identify acceptance criteria, negative scenarios, and boundary conditions
- Assess requirement testability
- Assess requirement risk
- Generate QE recommendations
- Validate the AI response structure
- Use a QE Planner for decision-making
- Invoke a specialized QE Risk Agent when required
- Produce structured JSON output
- Save analysis results
- Automated testing using pytest

## Agentic Behavior

## Architecture


                         Agentic-QE
                              │
                              ▼
                     Requirement Input
                              │
                              ▼
               ┌──────────────────────────┐
               │ Requirement Analysis     │
               │ Agent                    │
               └────────────┬─────────────┘
                            │
                            ▼
                    Prompt Engineering
                            │
                            ▼
               ┌──────────────────────────┐
               │ Ollama                   │
               │ Qwen2.5-Coder 7B        │
               │ Local LLM                │
               └────────────┬─────────────┘
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
                            ▼
                      QE Planner
                            │
                            ▼
                       Decision
                            │
                 ┌──────────┴──────────┐
                 ▼                     ▼
             High Risk           Low / Medium
                 │                     │
                 ▼                     ▼
           QE Risk Agent        No Specialist
                 │                  Action
                 ▼
           Risk Analysis

## Technology Stack

| Technology | Purpose |
|---|---|
| Python 3.14 | Application development |
| Ollama | Local LLM runtime |
| Qwen2.5-Coder 7B | Local LLM used for requirement analysis |
| pytest | Automated testing |
| JSON | Structured AI output |
| pathlib | File handling and path management |
| VS Code | Development environment |

## Project Structure

```text
Agentic-QE/
│
├── agent.py
├── analyzer.py
├── planner.py
├── risk_agent.py
├── main.py
├── app.py
├── README.md
├── LICENSE
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

## Purpose

This project demonstrates how Generative AI, structured output validation, and decision-driven agent execution can be applied to practical Quality Engineering workflows.

A hands-on project demonstrating Agentic AI and Quality Engineering capabilities.

## Author

Developed by Amardeep Sangwan — AI-QE project for intelligent Quality Engineering.


