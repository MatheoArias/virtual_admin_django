from django_unicorn.components import UnicornView, QuerySetType
from django.db.models import Q
from apps.liable.models import Liable
from apps.position.models import Position


class LiableListView(UnicornView):

    liable: Liable
    liables: list[Liable]
    search: str
    
    modal_state: bool = False

    def mount(self):
        self.liable=None
        self.liables=[]
        self.search=""

        if not self.liables:
            self.get_all_liables()

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
        search_term = self.search.strip().lower()
       
        if search_term == "":
            self.get_all_liables()
        else:
            liables_query = Liable.objects.select_related("position").filter(
                Q(position__code__icontains=search_term) |
                Q(position__name__icontains=search_term) |
                Q(code__icontains=search_term) |
                Q(name__icontains=search_term) |
                Q(lastName__icontains=search_term) |
                Q(email__icontains=search_term) |
                Q(telephone__icontains=search_term) |
                Q(workstation__icontains=search_term)
            ).distinct()
            self.liables = list(liables_query)


    def delete_liable(self, liable_id):
        if liable_id:
            Liable.objects.filter(id=liable_id).delete()
        self.get_all_liables()