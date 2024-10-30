import nbformat
import subprocess

def run_notebook_and_get_output(notebook_path):
    # Jupyter Notebook을 읽어온다.
    with open(notebook_path, 'r', encoding='utf-8') as f:
        notebook_content = nbformat.read(f, as_version=4)

    # 모든 셀을 실행하고 출력 결과를 저장한다.
    output = []
    for cell in notebook_content.cells:
        if cell.cell_type == 'code':
            # subprocess를 사용해 코드를 실행
            result = subprocess.run(['python', '-c', cell.source], capture_output=True, text=True)
            output.append(result.stdout.strip())

    return output

def check_output(expected_output):
    # 예상 출력과 비교하여 결과를 체크한다.
    output = run_notebook_and_get_output('grew_challenge.ipynb')
    for expected, actual in zip(expected_output, output):
        if expected != actual:
            print(f"Expected: '{expected}' but got: '{actual}'")
            return False
    return True

if __name__ == '__main__':
    expected_output = ["Hello World"]
    if check_output(expected_output):
        print("Test Passed!")
    else:
        print("Test Failed!")