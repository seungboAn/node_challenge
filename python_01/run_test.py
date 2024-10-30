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

def check_output(expected_outputs):
    # 예상 출력과 비교하여 결과를 체크한다.
    output = run_notebook_and_get_output('grew_challenge.ipynb')
    results = {"passed": [], "failed": []}

    for i, (expected, actual) in enumerate(zip(expected_outputs, output)):
        if expected == actual:
            results["passed"].append(f"문제 {i + 1}: 통과")
        else:
            results["failed"].append(f"문제 {i + 1}: 실패 (예상: '{expected}', 실제: '{actual}')")

    return results

if __name__ == '__main__':
    expected_outputs = ["Hello World", "True", "True", "False"]  # 예상 출력값
    results = check_output(expected_outputs)
    
    print("테스트 결과:")
    for msg in results["passed"]:
        print(f"[✓] {msg}")
    for msg in results["failed"]:
        print(f"[✗] {msg}")