class water:
    def __init__(self):
        self.guest=0
        self.total_water_2=900
        self.total_water_3=1500
        self.total_guest=0
        self.corporation_amount_2=0
        self.borewell_amount_2=0
        self.corporation_amount_3=0
        self.borewell_amount_3=0
        
    def allotwater(self,apartment_type,ratio):
        ratio=ratio.split(":")
        ratio=[int(i) for i in ratio]
        if apartment_type==2:
            self.corporation_amount_2=(self.total_water_2*ratio[0])//sum(ratio)
            self.borewell_amount_2=(self.total_water_2*ratio[1])//sum(ratio)
            print(self.corporation_amount_2,self.borewell_amount_2)
        else:
            self.corporation_amount_3=(self.total_water_3*ratio[0])//sum(ratio)
            self.borewell_amount_3=(self.total_water_3*ratio[1])//sum(ratio)
            print("else")

    def add_guest(self,guest_number):
        self.total_guest+=guest_number

    def bill(self):
        guest_total_cost=0
        guest_total_water=self.total_guest*30*10
        #while guest_total_water>0:

        if(guest_total_water>=0 and guest_total_water<=500):
            guest_total_cost+=guest_total_water*2

        elif(guest_total_water>=501 and guest_total_water<=1500):
            guest_total_cost+=(500*2)+(guest_total_water-500)*3
            print("second else")
        
        elif(guest_total_water>=1501 and guest_total_water<=3000):
            guest_total_cost+=(500*2)+(guest_total_water-500)*3+(guest_total_water-1500)*5
        else:
            guest_total_cost+=(500*2)+(guest_total_water-500)*3+(guest_total_water-1500)*5+(guest_total_water-3000)*8
        print(guest_total_water,"guest_total_water",guest_total_cost)

        apartment_2=(self.corporation_amount_2+self.corporation_amount_3)*1
        apartment_3=(self.borewell_amount_2 + self.borewell_amount_3)*1.5
        print(apartment_2,"apartment_2",apartment_3,"apartment_3")

        apartment_total_water=self.corporation_amount_2+self.corporation_amount_3+self.borewell_amount_2+self.borewell_amount_3
        total_water_used=apartment_total_water+guest_total_water
        total_cost=guest_total_cost+apartment_2+apartment_3
        return [total_water_used,int(total_cost)]

if __name__ =='__main__':
    ratio="2:1"
    water=water()
    water.allotwater(3,ratio)
    water.add_guest(4)
    water.add_guest(1)
    a=water.bill()
    print(a)



            

