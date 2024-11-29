from pydantic import BaseModel

class UserLogin(BaseModel):
    phone_no: int


class UserSignup(BaseModel):
    name: str
    phone_no: int
    

class SenderDetails(BaseModel):
    pickup_location: str
    parcel_size: str
    parcel_type: str
    pincode: int
    mode: str
    ecomode: bool

class ReceiverDetails(BaseModel):
    receiver_name: str
    address: str
    pincode: int
    phone_no: int

class Tracking(BaseModel):
    status: str
    current_location: str

class Review(BaseModel):
    review: str

class AdminLogin(BaseModel):
    phone_no: int


class AdminSignup(BaseModel):
    name: str
    phone_no: int
  

class DeliveryPersonLogin(BaseModel):
    phone_no: int
  

class DeliveryPersonSignup(BaseModel):
    name: str
    phone_no: int

    vehicle_no: str
    adhaar_no: int
    
    