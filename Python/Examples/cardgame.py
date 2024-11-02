class Card:
    def __init__(self, type, num):
        self.type = type
        self.num = num

# 카드 종류와 번호를 정의
types = ["Spades", "Hearts", "Diamonds", "Clubs"]
numbers = range(1, 14)  # 1~13까지 카드 번호

# 클래스 인스턴스를 생성하여 덱을 구성
deck = [Card(type, num) for type in types for num in numbers]