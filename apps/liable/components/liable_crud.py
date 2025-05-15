from django_unicorn.components import UnicornView, QuerySetType
from django.db.models import Q
from typing import Optional
from apps.liable.models import Liable


class LiableCrudView(UnicornView):
    liable: Optional[Liable] = None
    liables: QuerySetType[Liable] = Liable.objects.none()
    search: str = ""

    def mount(self):
        if not self.liables:
            self.get_all_liables()

    def get_all_liables(self):
        self.liables = list(Liable.objects.all())

    def get_liable(self, liable_id: str):
        try:
            self.liable = Liable.objects.get(id=liable_id)
        except Liable.DoesNotExist:
            self.liable = None
            print("Liable not found")

    def search_liable(self):
        if self.search == "":
            self.get_all_liables()
        else:
            liables_query = Liable.objects.filter(
                Q(position__name__icontains=self.search) |
                Q(code__icontains=self.search) |
                Q(name__icontains=self.search) |
                Q(lastName__icontains=self.search) |
                Q(email__icontains=self.search) |
                Q(telephone__icontains=self.search) |
                Q(workstation__icontains=self.search)
            )
            self.liables = list(liables_query)

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
