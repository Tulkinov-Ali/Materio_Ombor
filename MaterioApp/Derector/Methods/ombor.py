from methodism import custom_response,error_params_unfilled
from MaterioApp.models.auth import User,user_type_
from MaterioApp.models.warehouse import WareHose



def all_ombor(request,paramas):
    if request.user.type != 1:
        return custom_response(False,error_params_unfilled("sizga ruxsat yoq"))
    else:
        return custom_response(True,data=(x.format_workers() for x in WareHose.objects.all()))