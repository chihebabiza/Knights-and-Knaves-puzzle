from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
A_statement = And(AKnight, AKnave)
knowledge0 = And(
    # Each character is either a knight or a knave, but not both
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    # What A says is true if A is a knight, false if A is a knave
    Implication(AKnight, A_statement),
    Implication(AKnave, Not(A_statement))
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
A_statement = And(AKnave, BKnave)
knowledge1 = And(
    # Rules for A and B
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # A's statement
    Implication(AKnight, A_statement),
    Implication(AKnave, Not(A_statement))
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
A_statement = Or(
    And(AKnight, BKnight),
    And(AKnave, BKnave)
)
B_statement = Or(
    And(AKnight, BKnave),
    And(AKnave, BKnight)
)
knowledge2 = And(
    # Rules for A and B
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    # Statements
    Implication(AKnight, A_statement),
    Implication(AKnave, Not(A_statement)),
    Implication(BKnight, B_statement),
    Implication(BKnave, Not(B_statement))
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave." (unknown which)
# B says "A said 'I am a knave.'" and "C is a knave."
# C says "A is a knight."
# A's statement unknown → could be either AKnight or AKnave
# So we model A's statement as either being AKnight or AKnave
A_statement1 = AKnight
A_statement2 = AKnave
B_statement1 = A_statement2  # B claims "A said 'I am a knave'"
B_statement2 = CKnave
C_statement = AKnight

knowledge3 = And(
    # Rules for A, B, C
    Or(AKnight, AKnave),
    Not(And(AKnight, AKnave)),
    Or(BKnight, BKnave),
    Not(And(BKnight, BKnave)),
    Or(CKnight, CKnave),
    Not(And(CKnight, CKnave)),
    # Statements
    # A's statement: he says either AKnight or AKnave
    Implication(AKnight, Or(A_statement1, A_statement2)),
    Implication(AKnave, Not(Or(A_statement1, A_statement2))),
    # B's statements
    Implication(BKnight, And(B_statement1, B_statement2)),
    Implication(BKnave, Not(And(B_statement1, B_statement2))),
    # C's statement
    Implication(CKnight, C_statement),
    Implication(CKnave, Not(C_statement))
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
