# AI QE Requirement Analyzer Agent

An AI-powered Quality Engineering tool that analyzes software requirements using a local Large Language Model (LLM) and produces a structured QE analysis.

The agent identifies functional requirements, actors, business rules, acceptance criteria, ambiguities, missing information, negative scenarios, boundary conditions, testability, risk, and QE recommendations.

The project uses Python, Ollama, and Qwen2.5-Coder 7B to demonstrate how Generative AI can support requirement analysis and Quality Engineering activities.

> This is a demo project designed to demonstrate AI + QE engineering capabilities.

## Key Capabilities

- Read software requirements from text files
- Analyze requirements using a local LLM
- Generate structured QE analysis in JSON
- Identify ambiguities and missing information
- Identify negative scenarios and boundary conditions
- Assess requirement testability
- Assess requirement risk
- Generate QE recommendations
- Validate the AI response structure
- Save analysis results as JSON
- Automated testing using pytest

## Architecture

The agent follows a simple requirement-to-QE-analysis pipeline:

```text
Requirement Input
       ↓
RequirementAnalyzer (Python)
       ↓
Prompt Engineering
       ↓
Ollama + Qwen2.5-Coder 7B
       ↓
Structured JSON Response
       ↓
AI Output Validation
       ↓
QE Analysis
       ↓
Console Report + JSON Output

Technology Stack
 
Technology	              Purpose
Python 3.14	       Application development
Ollama	           Local LLM runtime
Qwen2.5-Coder 7B   Local LLM used for requirement analysis
pytest	           Automated testing
JSON	           Structured AI output and result storage
pathlib	           File handling and path management
VS Code	           Development environment

Project Structure
AI-QE-Requirement-Analyzer-Agent/
│
├── analyzer.py
├── main.py
├── README.md
│
├── data/
│   ├── sample_requirement.txt
│   └── empty_requirement.txt
│
├── tests/
│   └── test_analyzer.py
│
└── output/
    ├── .gitkeep
    └── requirement_analysis.json


QE Analysis Demonstration

Requirement:
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
Testability Score
Risk Level
QE Recommendation