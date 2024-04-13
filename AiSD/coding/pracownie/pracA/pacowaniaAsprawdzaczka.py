import subprocess
import os

failed = 0
script_directory = os.path.dirname(os.path.realpath(__file__))
os.chdir(script_directory)

input_file_range = range(1, 1921)

for input_number in input_file_range:
    input_file_path = f"/Users/szymon/Documents/Studia-UWr/AiSD/coding/in/in{input_number}.txt"
    output_file_path = os.path.join(r"/Users/szymon/Documents/Studia-UWr/AiSD/coding/out/",
                                    f"out{input_number}.txt")

    with open(input_file_path, "r") as input_file:
        input_data = input_file.read()

    process = subprocess.run(["./pA.out"], input=input_data, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                             text=True)

    with open(output_file_path, "r") as output_file:
        expected_output = output_file.read()

    if process.stdout == expected_output:
        print(f"Test {input_number}: PASSED")
    else:
        failed += 1
        print(f"Test {input_number}: FAILED")
        print("Actual Output:")
        print(process.stdout)
        print("Expected Output:")
        print(expected_output)

    print(process.stderr)
    print(f"Exit Code: {process.returncode}")
    print("=" * 50)

print("Failed:")
print(failed)