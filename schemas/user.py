from fastapi import APIRouter
from fastapi import HTTPException
from models import UserLogin,UserSignup,SenderDetails,ReceiverDetails,Tracking,Review,AdminLogin,AdminSignup,DeliveryPersonLogin,DeliveryPersonSignup
user = APIRouter

@user.post('/user-login')
def post_userlogin(user_login: UserLogin):
    
       return { "phone_no": UserLogin.phone_no}
       
    

@user.post('/user_signup')
def post_usersignup(user_signup: UserSignup):
         return{ "name": UserSignup.name,
          "phone_no": UserSignup.phone_no,}
         
     
@user.post('/sender_details')
def post_senderdetails(sender_details: SenderDetails):
      
           return{"pickup_location":SenderDetails.pick_location,
           "parcel_size":SenderDetails.parcel_size,
           "parcel_type":SenderDetails.parcel_type,
           "pincode":SenderDetails.pincode,
           "mode":SenderDetails.mode,
           "eco_mode":SenderDetails.eco_mode}
      
@user.post('/receiver_details')
def post_receiverdeatails(receiver_details: ReceiverDetails):
    
          return {"receiver_name": ReceiverDetails.Receiver_name,
           "address": ReceiverDetails.address,
           "pincode": ReceiverDetails.pincode,
           "phone_no": ReceiverDetails.phone_no}
           
@user.post('tracking')
def post_tracking(tracking: Tracking):
     
          return{"status":Tracking.status}

@user.post('/review')
def post_review(review:Review):
     
         return {"review":Review.review}
          
@user.post('admin_login')
def post_adminlogin(admin_login:AdminLogin):
     
         return{ "phone_no":AdminLogin.Phone_number,
          "password":AdminLogin.password}
     
@user.post('admin_signup')
def post_adminsignup(admin_signup:AdminSignup):
      
           
           return {"name":AdminSignup.name,
          "phone_no":AdminSignup.phone_no,
           "password":AdminSignup.password}

@user.get('/track')
def tracking_details():

     return {"review":Review.review}
         
@user.get('/order')
def order_details(details: ReceiverDetails):
     return {"pickup location": SenderDetails.picklocation,"drop location":ReceiverDetails.address,"status":Tracking.status}
     
@user.get("/userdetails") 
def user_details(details:UserLogin):
     return {"user name": UserSignup.name,"phone_no":UserLogin.phone_no}

@user.get("/deliveryperson")
def deliveryperson_details():
     return {"name":DeliveryPersonSignup.name,"phone_no":DeliveryPersonSignup.phone_no,"vehicle_no":DeliveryPersonSignup.vehicle_no}

@user.get("/reviewdetails")
def reviewdetails():
     return {"review": Review.review }
     
@user.post('deliveryperson_login')
def post_deliver_person(deliveryperson_login:DeliveryPersonLogin):
     
          return{ "phone_no":DeliveryPersonLogin.phone_no,
           "password":DeliveryPersonLogin.password}
      
@user.post('deliveryperson_signup')
def post_delivery_person(deliveryperson_signup:DeliveryPersonSignup):
      
         return{  "name":DeliveryPersonSignup.name,
           "phone_no":DeliveryPersonSignup.phone_no,
           "password":DeliveryPersonSignup.password,
           "vehicle_no":DeliveryPersonSignup.vehicle_no,
           "adhaar_no":DeliveryPersonSignup.adhaar_no}

           
     

          
        


          