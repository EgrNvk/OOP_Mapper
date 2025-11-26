class UserEntity:
    def __init__(self, id: int, username: str, email: str, password_hash: str):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash

class UserDTO:
    def __init__(self, id: int, username: str, email: str):
        self.id = id
        self.username = username
        self.email = email

class UserMapper:
    @staticmethod
    def to_dto(entity: UserEntity):
        return UserDTO(id=entity.id, username=entity.username, email=entity.email)
    @staticmethod
    def to_entity(dto: UserDTO, password_hash: str):
        return UserEntity(id=dto.id, username=dto.username, email=dto.email, password_hash=password_hash)
    @staticmethod
    def to_dto_list(entities: list[UserEntity]):
        return [UserMapper.to_dto(e) for e in entities]

entity=UserEntity(id=1, username="michael", email="text@example.com", password_hash="abc123hash")

dto=UserMapper.to_dto(entity)
print(dto.__dict__)

new_entity=UserMapper.to_entity(dto, "abc123hash")
print(new_entity.__dict__)
