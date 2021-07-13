import pdb
from models.tome import Tome
from models.author import Author

import repositories.tome_repository as tome_repository
import repositories.author_repository as author_repository

tome_repository.delete_all()
author_repository.delete_all()

author1 = Author("Gerald", "Gardner")
author_repository.save(author1)
author2 = Author("Abdul", "Alhazred")
author_repository.save(author2)
author3 = Author("Sir Walter", "Scott")
author_repository.save(author3)

tome_1 = Tome("The Book of Shadows", "Shadow Magic", 15, 3, author1, 30)
tome_repository.save(tome_1)

tome_2 = Tome("The Necronomicon", "Death Magic", 25, 2, author2, 50) 
tome_repository.save(tome_2)

tome_3 = Tome("Demonology & Witchcraft", "Demonology", 15, 4, author3, 30)
tome_repository.save(tome_3)



