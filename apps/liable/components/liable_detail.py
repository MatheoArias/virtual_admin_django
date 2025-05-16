from django_unicorn.components import UnicornView
from ..models import Liable


class LiableDetailView(UnicornView):
    liable:Liable = None
              
    def empty_liable(self):
        self.liable = None