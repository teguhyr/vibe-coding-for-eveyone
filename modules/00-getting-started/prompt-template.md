# Prompt Template (R-C-T-C-O)

Copy this, fill in each part, and paste it into Claude Code.

```
ROLE:
You are a <type of developer> helping a <team/function> team. Explain your code simply.

CONTEXT:
I have a file <file name> with these columns: <column1>, <column2>, ...
Here are 3 example rows (made-up data):
<row 1>
<row 2>
<row 3>

TASK:
Build a <Python script / small app> that <what it should calculate or do>.

CONSTRAINTS:
- Use only the Python standard library (no extra installs).
- <business rule 1, e.g. "a line is over budget if actual > budget by more than 10%">
- <business rule 2>
- Handle bad input with a clear error message.
- Add tests with pytest.

OUTPUT:
<what the result looks like: a printed table, a CSV file, a summary>.
Afterwards, explain how to run it and how the key parts work.
```

## Useful follow-up prompts

- "Explain this code to me like I am new to programming."
- "Run the tests and fix anything that fails."
- "What edge cases could break this? Add tests for them."
- "Add an option to export the result to CSV."
- "Show me how to check this result by hand."
