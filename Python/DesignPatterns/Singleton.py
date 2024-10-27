class Singleton:
    _instance = None  # 클래스 변수: 인스턴스를 저장하기 위한 변수(모든 인스턴스가 공유)

    def __new__(cls):
        # 인스턴스가 없을 때만 새로 생성
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            cls._instance.config = {}  # 멤버 변수 초기 설정 값으로 빈 딕셔너리 초기화
            cls._instance.data = {}
            print("새로운 Singleton 인스턴스 생성됨")
        else:
            print("기존 Singleton 인스턴스 반환됨")
        return cls._instance
    
    def __init__(self):
        self.state = "초기 상태"  # 클래스의 멤버 변수
    
    def set(self, key, value):
        """설정 값을 저장하는 메서드"""
        self.config[key] = value

    def get(self, key):
        """저장된 설정 값을 반환하는 메서드"""
        return self.config.get(key, None)  # 값이 없으면 None 반환

    def print_config(self):
        """현재 설정 값을 출력하는 메서드"""
        print(f"현재 설정 값: {self.config}")

    @staticmethod
    def initialize_resources():
        """리소스를 초기화하는 함수 (자주 쓰이는 패턴)"""
        print("리소스 초기화 중...")

    @staticmethod
    def release_resources():
        """리소스를 해제하는 함수 (자주 쓰이는 패턴)"""
        print("리소스 해제 중...")

# 싱글톤 테스트
s1 = Singleton()  # 새로운 인스턴스 생성
s1.set("db_host", "localhost")
s1.set("db_port", 3306)
s1.print_config()

s2 = Singleton()  # 기존 인스턴스 반환
print(f"s1의 메모리 주소: {id(s1)}") # 123456 (예시)
print(f"s2의 메모리 주소: {id(s2)}") # 123456 (예시, s1과 동일한 주소)

# s1과 s2는 같은 인스턴스이므로 상태를 공유함
# 같은 인스턴스를 참조하므로 s1에서 값을 변경하면 s2에서도 반영됨
s1.set("key", "value")  # 설정값 변경
print(s2.get("key"))    # "value" 출력

s1.data["key1"] = "value1"  # s1에 데이터 추가
print(s2.data["key1"])      # s2도 동일한 데이터를 볼 수 있음, 'value1'

# 같은 설정 값을 s2에서도 접근 가능
print(f"s2에서 db_host 가져오기: {s2.get('db_host')}")

# 리소스 초기화 및 해제 (필요 시 사용)
Singleton.initialize_resources()
Singleton.release_resources()
