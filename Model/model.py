class BookEntity:
    def __init__(self, id: int, title: str, author: str, price: float, internal_code: str):
        self.id = id
        self.title = title
        self.author = author
        self.price = price
        self.internal_code = internal_code
class BookDTO:
    def __init__(self, id: int, title: str, author: str):
        self.id = id
        self.title = title
        self.author = author
class BookMapper:
    @staticmethod
    def to_dto(entity: BookEntity):
        return BookDTO(id=entity.id, title=entity.title, author=entity.author)
    @staticmethod
    def to_dto_list(entities: list[BookEntity]):
        return [BookMapper.to_dto(e) for e in entities]