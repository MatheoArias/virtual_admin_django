from django_unicorn.components import UnicornView
from apps.liable.models import Liable

class LiableCrudView(UnicornView):
    new_liable=""
    liables = []
    select_liable = None
    
    def mount(self):
        self.liables=Liable.objects.all()

    
    def get_liable(self, liable_id):
        try:
            self.select_liable=Liable.objects.get(id=liable_id)
            print(self.select_liable)
                        
        except Liable.DoesNotExist:
            self.select_liable=None
    
    # def crear_libro(self):
    #     if self.nuevo_libro.strip():
    #         Book.objects.create(title=self.nuevo_libro)
    #         self.nuevo_libro = ""  # Limpiamos el input
    #         self.libros = Book.objects.all()  # Actualizamos la lista

    # # Eliminar un libro
    # def eliminar_libro(self, libro_id):
    #     Book.objects.get(id=libro_id).delete()
    #     self.libros = Book.objects.all()  # Actualizamos la lista

    # # Actualizar un libro
    # def actualizar_libro(self, libro_id, nuevo_titulo):
    #     libro = Book.objects.get(id=libro_id)
    #     libro.title = nuevo_titulo
    #     libro.save()
    #     self.libros = Book.objects.all()  # Actualizamos la list
    