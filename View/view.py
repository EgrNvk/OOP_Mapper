from Model.model import BookDTO

class BookView:
    def render_books(self, dtos: list[BookDTO]):
        print("Список книг:")
        for dto in dtos:
            print(f"{dto.id}. {dto.title} - {dto.author}")