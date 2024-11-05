import random
import unittest

# 모스 부호 딕셔너리 정의
morse_code = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F",
    "--.": "G", "....": "H", "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
    "--": "M", "-.": "N", "---": "O", ".--.": "P", "--.-": "Q", ".-.": "R",
    "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
    "-.--": "Y", "--..": "Z",
    ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5",
    "-....": "6", "--...": "7", "---..": "8", "----.": "9", "-----": "0",
    "--..--": ",", ".-.-.-": ".", "..--..": "?", "---...": ":", "-....-": "-",
    ".--.-.": "@"
}

# 모스 부호를 알파벳으로 변환하는 함수
def decode_morse(morse_list):
    return "".join(morse_code.get(ch, "") for ch in morse_list)

# 유닛 테스트 클래스 정의
class TestMorseDecoder(unittest.TestCase):
    def test_random_morse_code(self):
        # 테스트 케이스를 무작위로 생성
        for _ in range(10):  # 원하는 만큼 반복하여 여러 케이스 생성
            # 모스 부호 딕셔너리의 키들 중 임의의 모스 부호 선택
            morse_keys = random.choices(list(morse_code.keys()), k=5)
            # 기대 결과: 임의의 모스 부호를 해독한 문자들
            expected_output = decode_morse(morse_keys)
            # 테스트 수행
            self.assertEqual(decode_morse(morse_keys), expected_output)

# 테스트 실행
if __name__ == '__main__':
    unittest.main()