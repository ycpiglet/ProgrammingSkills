def my_decorator(func):
    def wrapper():
        print(func.__name__, "기능을 추가합니다.") # __name__으로 함수 이름도 같이 출력
        func()  # 원래 함수를 호출
        print(func.__name__, "기능을 마쳤습니다.")
    return wrapper

@my_decorator # 데코레이터(Decorator)
def say_hello():
    print("Hello!")

say_hello()
