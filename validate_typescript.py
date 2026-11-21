#!/usr/bin/env python
# Simple script to validate TypeScript support in CodeBLEU

from codebleu import calc_codebleu

# Simple TypeScript function with type annotations
reference = """function greet(name: string): string {
    return `Hello, ${name}!`;
}"""

# Same function with different variable names
prediction = """function sayHello(person: string): string {
    return `Hello, ${person}!`;
}"""

# Calculate CodeBLEU score for TypeScript code
result = calc_codebleu([reference], [prediction], lang="typescript")

print("TypeScript CodeBLEU Results:")
print(f"CodeBLEU Score: {result['codebleu']:.4f}")
print(f"N-gram Match Score: {result['ngram_match_score']:.4f}")
print(f"Weighted N-gram Match Score: {result['weighted_ngram_match_score']:.4f}")
print(f"Syntax Match Score: {result['syntax_match_score']:.4f}")
print(f"Dataflow Match Score: {result['dataflow_match_score']:.4f}")