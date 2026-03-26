# Knights and Knaves Puzzle Solver

A small Python project that solves classic **Knights and Knaves** logic puzzles using **propositional logic** and **model checking**.

In these puzzles:
- **Knights** always tell the truth.
- **Knaves** always lie.

This repo encodes each puzzle as a logical knowledge base and then uses entailment checks to determine which characters are knights/knaves.

## Repository contents

- `puzzle.py` — defines 4 Knights-and-Knaves puzzles (0–3), builds the knowledge base for each, and prints which symbols are entailed.
- `logic.py` — a minimal propositional-logic engine (Symbols, Not/And/Or/Implication/Biconditional) plus a `model_check` function that performs truth-table style entailment checking.

## How it works (high level)

1. Each character is represented with logical symbols like:
   - `"A is a Knight"`, `"A is a Knave"`, etc.
2. Constraints are added so each person is **either** a knight **or** a knave (but not both).
3. Each spoken statement is encoded so that:
   - If the speaker is a **knight**, the statement must be **true**.
   - If the speaker is a **knave**, the statement must be **false**.
4. The solver uses `model_check(knowledge, query)` to test whether the knowledge base *entails* a given query (symbol).

## Requirements

- Python 3.x  
No external dependencies.

## Run

```bash
python puzzle.py
```

## Output

For each puzzle, the program prints the symbols that are logically entailed by the knowledge base, e.g. which of:

- `A is a Knight` / `A is a Knave`
- `B is a Knight` / `B is a Knave`
- `C is a Knight` / `C is a Knave`

must be true.

## Puzzles included

- **Puzzle 0**: A says: *"I am both a knight and a knave."*
- **Puzzle 1**: A says: *"We are both knaves."* (B says nothing)
- **Puzzle 2**: A says: *"We are the same kind."* B says: *"We are of different kinds."*
- **Puzzle 3**: A says either *"I am a knight."* or *"I am a knave."* (unknown which).  
  B says: *"A said 'I am a knave'."* and *"C is a knave."*  
  C says: *"A is a knight."*

## Notes / limitations

- The model checker in `logic.py` explores possible truth assignments (truth-table style). This is fine for small puzzles but will not scale well to large knowledge bases.
- Puzzle statements are manually encoded in `puzzle.py`.
