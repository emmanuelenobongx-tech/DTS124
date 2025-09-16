# DTS124 Test Simulator (Python CLI version)
# 20 Multiple-choice questions (A/B/C), grouped into 2 sets of 10.

questions = [
    # --- Set 1: Q1 - Q10 ---
    {
        "q": "Which of the following is NOT a primitive data type?",
        "choices": ["A: String", "B: Boolean", "C: Byte"],
        "correct": "A",
        "feedback": "Boolean and byte are primitive; string is not a primitive in the slides."
    },
    {
        "q": "A data item is best described as:",
        "choices": ["A: A collection of records", "B: The smallest unit of data with meaning", "C: A file on disk"],
        "correct": "B",
        "feedback": "A data item is the smallest unit of data with meaning."
    },
    {
        "q": "Which structure groups multiple data items of different types under one name?",
        "choices": ["A: Array", "B: Record", "C: Stack"],
        "correct": "B",
        "feedback": "A record groups multiple fields of potentially different types."
    },
    {
        "q": "What stores the memory address of another variable?",
        "choices": ["A: Index", "B: Pointer", "C: Element"],
        "correct": "B",
        "feedback": "A pointer stores the memory address of another variable."
    },
    {
        "q": "Which is an example of a file?",
        "choices": ["A: students.txt", "B: An array in memory", "C: A pointer value"],
        "correct": "A",
        "feedback": "students.txt with each line as a record was the example in the slides."
    },
    {
        "q": "An attribute relates to:",
        "choices": ["A: Operation", "B: Property of an entity", "C: Memory address"],
        "correct": "B",
        "feedback": "An attribute is a property or characteristic of an entity."
    },
    {
        "q": "Which is NOT a primitive type?",
        "choices": ["A: Double", "B: Character", "C: LinkedList"],
        "correct": "C",
        "feedback": "LinkedList is a non-primitive data structure."
    },
    {
        "q": "Which primitive has an 8-bit signed two’s complement range?",
        "choices": ["A: Short", "B: Byte", "C: Integer"],
        "correct": "B",
        "feedback": "Byte is an 8-bit signed two’s complement integer (-128 to 127)."
    },
    {
        "q": "Which primitive stores floating values with more precision?",
        "choices": ["A: Float", "B: Double", "C: Byte"],
        "correct": "B",
        "feedback": "Double allows more precision than float."
    },
    {
        "q": "Index (or subscript) is used to:",
        "choices": ["A: Access array elements", "B: Link nodes", "C: Store files"],
        "correct": "A",
        "feedback": "Indexes are used to access elements in arrays."
    },

    # --- Set 2: Q11 - Q20 ---
    {
        "q": "Which is a NON-primitive data structure?",
        "choices": ["A: Integer", "B: Array", "C: Boolean"],
        "correct": "B",
        "feedback": "Arrays are non-primitive (user-defined) data structures."
    },
    {
        "q": "Which classification separates linear and non-linear?",
        "choices": ["A: Primitive vs Non-primitive", "B: Static vs Dynamic Only", "C: Linear vs Non-linear divides non-primitive"],
        "correct": "C",
        "feedback": "Non-primitive structures are divided into linear and non-linear."
    },
    {
        "q": "Which is a reason to use good data structures?",
        "choices": ["A: Slower execution", "B: Efficient memory/time usage", "C: Harder to implement"],
        "correct": "B",
        "feedback": "Good structures reduce space/time complexity."
    },
    {
        "q": "Which is a linear data structure example?",
        "choices": ["A: Graph", "B: Tree", "C: Queue"],
        "correct": "C",
        "feedback": "Queue is linear; trees/graphs are non-linear."
    },
    {
        "q": "Which is NOT an explicit need for data structures?",
        "choices": ["A: Fast searching", "B: Provide operations on groups", "C: Ensure no memory is used"],
        "correct": "C",
        "feedback": "They don’t eliminate memory usage; they manage it efficiently."
    },
    {
        "q": "What are the two complementary goals of data structures?",
        "choices": ["A: Correctness and Efficiency", "B: Speed and Size", "C: Security and Portability"],
        "correct": "A",
        "feedback": "Correctness and efficiency are the main goals."
    },
    {
        "q": "Which is a non-linear data structure?",
        "choices": ["A: Stack", "B: Tree", "C: Array"],
        "correct": "B",
        "feedback": "Tree is a non-linear data structure."
    },
    {
        "q": "Which application uses queues?",
        "choices": ["A: Undo in editors", "B: BFS in graph algorithms", "C: Function call stack"],
        "correct": "B",
        "feedback": "BFS in graphs is a queue application."
    },
    {
        "q": "Which property belongs to linked lists?",
        "choices": ["A: Fixed size", "B: Dynamic size", "C: Constant-time random access"],
        "correct": "B",
        "feedback": "Linked lists grow/shrink dynamically."
    },
    {
        "q": "Which is a disadvantage of linked lists?",
        "choices": ["A: Slow random access", "B: Wasted contiguous memory", "C: No pointers required"],
        "correct": "A",
        "feedback": "Linked lists have slow random access and pointer overhead."
    }
]

def run_set(set_index, qset):
    print(f"\n--- Set {set_index+1} ---")
    user_answers = []
    for i, item in enumerate(qset):
        print(f"\nQ{set_index*10 + i + 1}: {item['q']}")
        for c in item['choices']:
            print("   ", c)
        ans = input("Your answer (A/B/C): ").strip().upper()
        user_answers.append(ans if ans in ['A','B','C'] else None)

    # Grade
    score = 0
    print("\nResults:")
    for i, (ans, item) in enumerate(zip(user_answers, qset)):
        correct = item['correct']
        if ans == correct:
            score += 1
            print(f"Q{i+1}: Correct ✓")
        else:
            print(f"Q{i+1}: Incorrect ✗ — Your answer: {ans}, Correct: {correct}")
            print("   Feedback:", item['feedback'])
    print(f"\nSet {set_index+1} Score: {score}/10")
    return score

def main():
    total_score = 0
    for si in range(2):  # two sets
        start = si*10
        end = start+10
        set_qs = questions[start:end]
        total_score += run_set(si, set_qs)

    print("\n=== Overall Progress ===")
    print(f"Total Correct: {total_score}/20")

if __name__ == "__main__":
    main()