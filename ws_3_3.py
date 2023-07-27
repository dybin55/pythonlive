import book


def rental_book(numbers, name):
    book_left = book.decrease_book(numbers)
    print(f"남은 책의 수 : {book_left}")
    print(f"{name}님이 {numbers}권의 책을 대여하였습니다")

rental_book(3, '홍길동')
    