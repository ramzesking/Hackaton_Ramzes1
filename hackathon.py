# import json

# class Cars:
#     FILE = 'jsondb/cars.json'
#     id = 0
#     def create(self,brand,model,year,engine_volume,color,body_type,mileage,price):
#         self.brand = brand
#         self.model = model 
#         self.year = year 
#         self.engine_volume = engine_volume
#         self.color = color
#         self.body_type = body_type
#         self.mileage = mileage
#         self.price = price
#         self.send_car_to_json()
#     @classmethod
#     def get_id(cls):
#         cls.id += 1
#         return cls.id


#     @classmethod
#     def listing(cls):
#         with open(cls.FILE) as file:
#            return json.load(file)

#     @classmethod
#     def retrieve(cls,id):
#         data = cls.listing()
#         car = list(filter(lambda x :x['id']== id ,data))
#         if not car:
#             return 'Такого авто нет!!'
#         else:
#             return car[0]
    
    


#     @classmethod
#     def send_data_to_json(cls,data):
#         with open(cls.FILE, 'w') as file:
#             json.dump(data,file)   

   
#     def send_car_to_json(self):
#         data =Cars.listing()
#         car = {
#             'id':Cars.get_id(),
#             'brand': self.brand,
#             'model': self.model,
#             'year': self.year,
#             'engine_volume': self.engine_volume,
#             'color': self.color,
#             'body_type': self.body_type,
#             'mileage':self.mileage,
#             'price':self.price
#         }
#         data.append(car)
#         with open (Cars.FILE, 'w') as file:
#             json.dump(data,file)
#         return {'status':201,'msg':car}
    


#     @classmethod
#     def update(cls,id,**kwargs):
#         data = cls.listing()
#         car = cls.retrieve(id)
#         if type(car) !=dict:
#             return car
#         index = data.index(car)
#         data[index].update(**kwargs)
#         cls.send_data_to_json(data)
#         return {'status':'200', 'msg':'Updated'}

#     @classmethod
#     def delete(cls,id):
#         data = cls.listing()
#         car = cls.retrieve(id)
#         if type(car) !=dict:
#             return car
#         index = data.index(car)
#         data.pop(index)
#         cls.send_data_to_json(data)
#         return {'status':204, 'msg':'Deleted'}

# with open(Cars.FILE , 'w')as file:
#     json.dump([],file)


# car1 = Cars()
# car2 = Cars()
# car3 = Cars()
# car2.create('BMW','X5 M50i ',2021,4,'White','SUV',0, 82.800)
# car1.create('Mercedes-Benz','GLC Coupe',2021,3,'Blue','crossover',0, 183.957)
# car3.create('Toyota','Camry',2017,3,'Black','Sedan',0,25000)
# print(Cars.retrieve(2))
# print(Cars.update(2,year = 2022))
# print()
# print(Cars.retrieve(2))
# print(Cars.delete(2))
# print()
# print(Cars.listing())