import json


def main():
    print('1)Create obj\n2)View database\n3)View a specific object\n4)Edit object\n5)Delete obj\n6)Like the car\n7)Leave a comment for the car\n8)finish work ')    
    try:
        a=int(input('Select an action:'))
        if a == 1:
            brand=input('Brand:')
            model=input('Model:')
            year=int(input('Year of release:'))
            volume=input('Engine volume:')
            color=input('Color:')
            body=int(input('body type:\n1-Sedan\n2-station wagon\n3-coupe\n4-hatchback\n5-Minivan\n6-SUV\n7-Pickup\n'))
            if body==1:
                body='Sedan'
            elif body==2:
                body='Station wagon'
            elif body==3:
                body='Coupe'
            elif body==4:
                body='Hatchback'
            elif body==5:
                body='Minivan'
            elif body==6:
                body='SUV'
            elif body==7:
                body='Pickup'
            mileage=int(input('Mileage:'))
            price=int(input('Price:'))
            Cars().create(brand, model, year, volume,color, body, mileage, price)
            main()
        elif a == 2 :
            print(Cars.listing())
            main()
        elif a == 3:
            object=int(input('Enter object index:'))
            print(Cars.retrieve(object))
            main()
        elif a == 4:
            object=int(input('Enter object index:'))
            kwargs={}
            obj=input('What do you want to change:')
            val=input('What value do you want to change this to:')
            kwargs[obj]=val
            Cars().update_car(object, **kwargs)
            main()
        elif a == 5 :
            object=int(input('Enter object index:'))
            Cars().delete_car(object)
            main()

        elif a == 6:
            id = int(input('Enter object index:'))
            Cars().like_(id)
            main()
        elif a==7:
            id=int(input('Enter object index:'))
            kwargs = {}
            com = input('Comment: ')
            kwargs['comment'] = com
            Cars().coments(id, **kwargs)
            main()

        elif a == 8:
            print('Work completed!!!')
    except:
        print('INCORRECT DATA!!!!!!!!')
        main()


class Cars:
    FILE='jsondb/cars.json'
    id=0
    coment=None
    like=0

    def create(self, brand, model, year, volume,color, body, mileage, price):
        self.brand=brand
        self.model=model
        self.year=year
        self.volume=volume
        self.color=color
        self.body=body
        self.milage=mileage
        self.price=price
        self.send_cars_to_json()
    
    @classmethod
    def get_id(cls):
        cls.id+=1
        return cls.id     
    @classmethod
    def listing(cls):
        with open(cls.FILE) as file:
            return json.load(file)
    @staticmethod
    def get_one_car(auto,id):
        car= list(filter(lambda x : x['id']==id , auto))
        if not car:
            return('No such product')
        return car[0]


    @classmethod
    def send_auto_to_json(cls, auto):
        with open(Cars.FILE, 'w') as file:
            json.dump(auto, file)

    def send_cars_to_json(self):
        auto=Cars.listing()
        car={
            'id':Cars.get_id(),
            'Brand':self.brand,
            'Model':self.model,
            'Year of release':self.year,
            'Engine volume':self.volume,
            'Color':self.color,
            'body type':self.body,
            'Mileage':self.milage,
            'Price':self.price,

        }
        auto.append(car)
         
        with open(Cars.FILE, 'w') as file:
            json.dump(auto, file)

        return{'satus':'201', 'msg':'car'}

    @classmethod
    def retrieve(cls,id):
        auto = cls.listing()
        car=cls.get_one_car(auto, id)
        return car

    @classmethod
    def update_car(cls,id, **kwargs):
        data=cls.listing()
        car = cls.get_one_car(data,id)
        index = data.index(car)
        data[index].update(**kwargs)
        cls.send_auto_to_json(data)
        return{'status':'200','msg':'Updated'}
    @classmethod
    def delete_car(cls,id):
        data=cls.listing()
        car=cls.get_one_car(data,id)
        if type(car)!=dict:
            return car
        index=data.index(car)
        data.pop(index)
        cls.send_auto_to_json(data)
        print({'status':'204','msg':'Deleted'})
    @classmethod
    def like_(cls, id):
        data = cls.listing()
        car = cls.get_one_car(data,id)
        index = data.index(car)
        data[index].update(like = 1)
        cls.send_auto_to_json(data)
        return {'status':'200','msg':'liked'}

    @classmethod
    def dislike(cls, id):
        data = cls.listing()
        car = cls.get_one_car(data,id)
        index = data.index(car)
        data[index].update(like = 0)
        cls.send_auto_to_json(data)
        return {'status':'200','msg':'disliked'}

    @classmethod
    def coments(cls,id, **kwargs ):
        data=cls.listing()
        car = cls.get_one_car(data,id)
        index = data.index(car)
        data[index].update(**kwargs)
        cls.send_auto_to_json(data)
        return{'status':'200','msg':'comented'}

    with open (FILE, 'w')as file :
        json.dump([],file)

main()