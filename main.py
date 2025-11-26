from Controller.controller import BookController
from View.view import BookView

controller=BookController()
dtos=controller.get_all_books()

view=BookView()
view.render_books(dtos)