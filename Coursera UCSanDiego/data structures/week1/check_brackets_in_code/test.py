# test check_brackets.py
import os
from check_brackets import find_mismatch

def main():
    directory = "./tests/"
    current_directory = os.listdir(directory)
    test_result = []
    for current_file in current_directory:
        # filter out answer files
        # read test problems
        if (".a" not in current_file):
            with open(directory + current_file, mode="r") as problem_file:
                problem = problem_file.readline()
                mismatch = find_mismatch(problem)
                # read test answer and check with result we just computed
                with open(directory + current_file + ".a", mode="r") as answer_file:
                    answer = answer_file.readline()
                    if set(str(mismatch).split()) != set(answer.split()):
                        test_result.append(problem)
                        test_result.append("our answer: " + str(mismatch))
                        test_result.append("answer: " + str(answer))
    
    if not test_result:
        print("Testing is finished! 0 errors found!")
    else:
        print(test_result)                

if __name__ == "__main__":
    main()