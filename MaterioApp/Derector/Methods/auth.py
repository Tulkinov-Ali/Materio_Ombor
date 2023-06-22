from methodism import custom_response,error_params_unfilled
from rest_framework.authtoken.models import Token
from MaterioApp.models.auth import User,user_type_
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from coinfig.base.send_sms import send_sms
from methodism.helper import generate_key,exception_data,code_decoder
from userapp.models.auth import OTP
import random
import string
import uuid

import datetime     




def regis(request,params):
    user = User.objects.filter(phone=params["phone"]).first()

    
    if user:
        return custom_response(False,error_params_unfilled(user))
    
        
        
    if "phone" not in params or "password" not in params:
           
            return custom_response(False,message="Error")
        
        
    if len(str(params["phone"])) != 12:
        return custom_response(False,message="Error")
        
        
    if type(params["phone"]) is not int:
       return custom_response(False,message="Error")
        
        
    if len(params["password"]) < 6 or params["password"].isalnum():
           return custom_response(False,message="Error")
        
    if " " in params["password"]:
        return custom_response(False,message="Error")
        
        
    user_data = {
        "phone" : params["phone"],
        "password" : params["password"],
        "name" :params.get("name",'')
    }
        
        
    if params.get("key",None):
        user_data.update({
            "is_staff" : True,
            "is_superuser" : True,
            'type':user_type_(params["key"])
        })
       
        
    user = User.objects.create_user(**user_data)
    token = Token.objects.create(user=user)
        
    return custom_response(True,message={"token" : token.key})