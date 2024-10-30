import unittest
from run_tests import check_output

class TestGrewChallenge(unittest.TestCase):
    def test_output(self):
        expected_outputs = ["Hello World", "True", "True", "False"]
        results = check_output(expected_outputs)
        
        # 모든 결과를 출력합니다.
        print("테스트 결과:")
        for msg in results["passed"]:
            print(f"[✓] {msg}")
        for msg in results["failed"]:
            print(f"[✗] {msg}")

        # 테스트 통과 여부를 확인합니다.
        self.assertTrue(len(results["failed"]) == 0)

if __name__ == '__main__':
    unittest.main()
