def loadKnowledgeBase():
    with open("KB.txt", "r") as file:
        return [line.rstrip('\n') for line in file]

def loadQuestions():
    with open("queries.txt", "r") as file:
        return [line.rstrip('\n') for line in file]

def resetOutputFile():
    open("output.txt", "w").close()

def logResult(question, answer):
    with open("output.txt", "a") as file:
        file.write(f"Question: {question}; Answer: {answer}\n")

def findVariableMapping(rule_expression, fact_expression):
    rule_pred, rule_args = rule_expression.split("(")
    fact_pred, fact_args = fact_expression.split("(")

    if rule_pred != fact_pred:
        return None

    rule_vars = rule_args[:-1].split(',')
    fact_vars = fact_args[:-1].split(',')

    if len(rule_vars) != len(fact_vars):
        return None

    return {rv.strip(): fv.strip() for rv, fv in zip(rule_vars, fact_vars)}

def replaceVariables(original_fact, left_side, right_side, var_mapping):
    if "(y)" in right_side:
        return right_side.split("y")[0] + var_mapping['y'] + ")"
    else:
        return right_side.split("x")[0] + var_mapping['x'] + ")"

def applyForwardChaining(knowledgeBase, question):
    known_facts = set(filter(lambda x: "=>" not in x, knowledgeBase))

    while True:
        new_facts = set()
        for rule in knowledgeBase:
            if "=>" in rule:
                left, right = rule.split("=>")
                for fact in known_facts:
                    variable_map = findVariableMapping(left.strip(), fact.strip())
                    if variable_map:
                        new_fact = replaceVariables(fact, left.strip(), right.strip(), variable_map)
                        new_facts.add(new_fact.strip())

        if new_facts.issubset(known_facts):
            break

        known_facts.update(new_facts)

    return question.strip() in known_facts

# Running the forward chaining
knowledgeBase = loadKnowledgeBase()
questions = loadQuestions()
resetOutputFile()

for q in questions:
    answer = applyForwardChaining(knowledgeBase, q)
    logResult(q, answer)