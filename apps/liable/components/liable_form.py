from django_unicorn.components import UnicornView
from apps.liable.forms import LiableForm
from apps.position.models import Position
from apps.liable.models import Liable


class LiableFormView(UnicornView):

    positions=list[Position]()
    form_errors = {}
    liable:Liable=None
    
    code:str = ""
    name:str = ""
    lastName:str = ""
    email:str = ""
    telephone:str = ""
    workstation:str = ""
    active:bool = False
    position:str = ""


    def mount(self):
        self.get_all_positions()
        self.position = '0'
        print('desde el hijo',self.liable)

        if self.liable:
            try:
                self.liable = Liable.objects.get(id=self.liable.id)
                self.code = self.liable.code
                self.name = self.liable.name
                self.lastName = self.liable.lastName
                self.email = self.liable.email
                self.telephone = self.liable.telephone
                self.workstation = self.liable.workstation
                self.active = self.liable.active
                self.position = str(self.liable.position.id) if self.liable.position else '0'

            except Liable.DoesNotExist:
                self.liable = None

    def get_all_positions(self):
        self.positions = list(Position.objects.all())

    def submit(self):
        try:
            position_obj = Position.objects.get(id=self.position) if self.position != '0' else None 
            image_file = self.request.FILES.get("image")
            data = {
                "code": self.code,
                "name": self.name.strip(",."),
                "lastName": self.lastName.strip(",."),
                "email": self.email,
                "telephone": self.telephone.strip(",.,-"),
                "workstation": self.workstation.strip(".,-"),
                "active": self.active,
                "position": position_obj,
            }
            form = LiableForm(data=data,files={'image':image_file})

            if form.is_valid():
                liable = form.save()
                self.form_errors = {}
                print(f'Los datos de {liable} se han modificado con éxito')

                if hasattr(self.parent, "get_all_liables"):
                    self.parent.get_all_liables()
                    self.parent.force_render = True
            
                else:
                    self.parent.Liables = list(Liable.objects.all())
                    self.parent.force_render = True
            else:
                self.form_errors = form.errors
                print("Errores:", self.form_errors)

        except Exception as e:
            print("Error general:", e)

    def updated_liable(self):
        try:
            self.liable=Liable.objects.get(id=self.liable.id)
            position_obj= Position.objects.get(id=self.position) if self.position != '0' else '0' 
            image_file = self.request.FILES.get("image")

            data = {
                "code": self.code,
                "name": self.name.strip(",."),
                "lastName": self.lastName.strip(",."),
                "email": self.email,
                "telephone": self.telephone.strip(",.,-"),
                "workstation": self.workstation.strip(".,-"),
                "active": self.active,
                "position": position_obj,
            }
            form = LiableForm(data=data, files={'image': image_file}, instance=self.liable)
            
            if form.is_valid():
                self.liable = form.save()
                self.form_errors = {}


                if hasattr(self.parent, "get_all_liables"):
                    self.parent.get_all_liables()
                    self.parent.force_render = True
            
                else:
                    self.parent.Liables = list(Liable.objects.all())
                    self.parent.force_render = True
            else:
                self.form_errors = form.errors
                print("Errores:", self.form_errors)
        
        except Exception as e:
            print("Error general:", e)
        
