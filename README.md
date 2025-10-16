
HILDE Constraint Layer: Dynamic Security Validation
This project is an extension of the HILDE (Human-in-the-Loop Decoding) concept, implementing a dynamic security and quality constraint layer for LLM-generated code.

The original HILDE system focuses on real-time interactive decision-making by highlighting critical tokens and offering secure alternatives to the user. This extension adds a post-generation validation system that automatically checks the completed code snippet against a set of dynamic, user-defined rules to ensure compliance with security policies and coding standards. It closes the loop by automatically validating the output of the completion model before the code is finalized and accepted.

Key Features
Dynamic Constraint Translation: Converts natural language constraints (e.g., "don't allow while loops," "no function calls," "no imports") into formal, machine-readable rule specifications (JSON format) using a separate Large Language Model (LLM) for high-accuracy translation.

Static Code Analysis: Utilizes Python's native Abstract Syntax Tree (AST) module to perform fast and reliable static analysis on the generated code against the dynamically created rules.

Flexible Rule Engine: Rules can be defined to check for specific AST node types (While, For, Call, Import, ClassDef) and can include granular checks for banned functions (eval) or modules (requests).

Code Generation Integration: Includes a simplified HiLDeLiteCompletionEngine using Qwen2.5-Coder-7B-Instruct for demonstration of the end-to-end code generation and validation pipeline.

Architecture and Flow
The system is composed of four main components that work together to enforce constraints:

HiLDeLiteCompletionEngine: A simplified LLM-based engine (Here it's Qwen2.5-Coder-7B) that generates the initial code completion from a given prompt.

DynamicRuleTranslator: An LLM-powered component (GPT-4-nano in the notebook example) that takes a list of natural language constraints from the user and translates them into a structured JSON format suitable for static analysis.

CodeAnalyzer: The core validation component. It takes the generated code's AST and the list of formal rule specifications. It then traverses the AST to check for and report any rule violations.

DynamicConstraintSystem: The orchestrator. It receives the user prompt and constraints, calls the Rule Translator, calls the Completion Engine, passes the resulting code to the Code Analyzer, and finally compiles and presents the summary of violations.

Usage Example
This project is implemented as a Python application, typically run within a Jupyter/Colab environment.

Prerequisites
An OpenAI API Key is required for the DynamicRuleTranslator component to function, as it relies on a powerful LLM to translate natural language constraints into structured rules.

Workflow
Initialize Engines (Requires API keys and GPU for the completion model)

completion_engine = HiLDeLiteCompletionEngine()
analysis_engine = CodeAnalyzer() # or a Mock for testing
constraint_system = DynamicConstraintSystem(completion_engine, analysis_engine)
Define the Code Prompt


prompt = "def process_data():"

Define the User's Security/Style Constraints in natural language

user_constraints = ["dont allow for loops"]
Process the Code with Constraints


result = constraint_system.process_code_with_constraints(prompt, user_constraints)


Review the Results


print("=== RESULT ===")
print(f"Generated Code:\n{result['completion']}\n")
print(f"Rules Generated: {len(result['rule_specifications'])}")
for spec in result['rule_specifications']:
    print(f" - {spec['rule_name']}: {spec['ast_node_type']}")
print(f"Violations Found: {result['violation_count']}")
print(f"Summary:\n{result['summary']}"
