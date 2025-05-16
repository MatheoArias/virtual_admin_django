from django_unicorn.components import UnicornView, QuerySetType
from django.db.models import Q
from apps.liable.models import Liable


class LiableListView(UnicornView):
    liable: Liable = None
    liables: QuerySetType[Liable] = Liable.objects.none()
    search: str = ""
    modal_state: bool = False

    def mount(self):
        if not self.liables:
            self.get_all_liables()
    
    def close_modal(self):
        self.modal_state = False
        self.liable=None
    
    def get_all_liables(self):
        self.liables = list(Liable.objects.all())

    def get_liable(self, liable_id: str):
        try:
            if str(self.liable.id) == str(liable_id) and self.liable:
                self.modal_state = True
                return self.liable

            self.liable = Liable.objects.get(id=liable_id)
            self.modal_state = True
            
        except Liable.DoesNotExist:
            self.liable = None
            self.modal_state = False
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