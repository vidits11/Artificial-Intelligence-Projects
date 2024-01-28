Project  - Forward Chaining Chatbot
CIS561: Artificial Intelligence (F23)

Submitted by: Vidit Shrivastava 
Student ID(02049294)

Code files
1. Task_3.py: Implements the core forward chaining logic. Reads the KB and queries, performs inference to answer queries, and outputs results.
2. KB.txt - Contains the knowledge base facts and rules in first-order logic format.
3. queries.txt - Contains sample queries to answer, also in first-order logic.
4. output.txt - Generated file containing the answers to the input queries after inference.

Usage
The program requires Python 3.x. 

To run:
1. Ensure KB.txt, queries.txt and the Python files are in the same directory
2. Run 'python Task_3.py' 
3. The output answers will be written to output.txt
4. Examine output.txt to see the query answers determined through forward chaining

Code Overview
## Overview
This Python script implements a simple forward chaining algorithm on a given knowledge base (KB). It reads facts and rules from a file, processes queries, and logs the results.

## Files
- `KB.txt`: Contains the knowledge base with facts and rules.
- `queries.txt`: Contains queries to be processed against the knowledge base.
- `output.txt`: Logs the results of the queries.

## Functions
- `loadKnowledgeBase()`: Reads and returns the content of `KB.txt`.
- `loadQuestions()`: Reads and returns the queries from `queries.txt`.
- `resetOutputFile()`: Clears/creates an empty `output.txt` file for logging results.
- `logResult(question, answer)`: Logs the results of each query in `output.txt`.
- `findVariableMapping(rule, fact)`: Matches a rule with a fact and returns variable mappings.
- `replaceVariables(original_fact, left_side, right_side, var_mapping)`: Applies variable mappings to a rule's conclusion.
- `applyForwardChaining(knowledgeBase, question)`: Implements the forward chaining algorithm to derive answers to queries.
- Main Execution Block: Runs the forward chaining on the loaded knowledge base and logs the results.

## Usage
1. Ensure `KB.txt` and `queries.txt` are properly formatted and placed in the same directory as the script.
2. Run the script.
3. Check `output.txt` for the results of the queries.

Customizing
To use a different KB or queries:
- Replace the contents of KB.txt and queries.txt respectively
- Re-run `python Task_3.py` to perform inference on the new inputs.
