#!/usr/bin/env python
# coding: utf-8

# In[255]:


import pandas as pd


class BANK_ACCOUNT():
    
    def __init__(self):
        self.name = None
        self.surname = None 
        self.address = None
        self.postcode = None
        self.customer_queue = 0
        self.income = 0
        self.interest_rate = 0
  
    def data_extracting(self, form):
        self.name=form.split(' - ')[0].split()[0]
        self.surname=form.split(' - ')[0].split()[1]
        self.customer_queue=form.split(' - ')[1]
        self.income=form.split(' - ')[2]
        self.address=form.split(' - ')[-1]
                                                         
    def data_featuring(self):
        self.postcode=self.address.split()[-1]
    
    def data_remain_cleaning(self):
        
        return{
            'name' : self.name,
            'surname' : self.surname,
            'earning money' : self.interest_rate * self.income,
            'income' : self.income,
            'interest_rate' : self.interest_rate
        }
    
    #custom methods
        
    def set_income(self,new_amount):
        self.income = new_amount
        
    def interest_rate1(self):
        self.interest_rate += 1

        
customer_information_ahmet="Ahmet Oğuz - 56 - 20000 - 3 rue naclieres 75025  "
customer_information_maxi="Maxi Laundrieu - 85 - 5000 - 3 rue Paris 75862  "
customer_information_camille="Camille Laundrieu - 96 - 0 - 9 rue caen 94456  " 
customer_information_marie="Marie Anne - 12 - 120 - 16 rue d'harcourt 14231  "
customer_information_mathilde="Mathilde Dupont - 26 - 1000 - 45 rue Saint Jean 95632 "
customer_information_angel="Angel Galloute - 52 - 1500 - 1 rue fontenay 56236"

ahmet=BANK_ACCOUNT()
maxi=BANK_ACCOUNT()
camille=BANK_ACCOUNT()
marie=BANK_ACCOUNT()
mathilde=BANK_ACCOUNT()
angel=BANK_ACCOUNT()

ahmet.data_extracting(customer_information_ahmet)
maxi.data_extracting(customer_information_max)
camille.data_extracting(customer_information_camille)
marie.data_extracting(customer_information_marie)
mathilde.data_extracting(customer_information_mathilde)
angel.data_extracting(customer_information_angel)

ahmet.data_featuring()
maxi.data_featuring()
camille.data_featuring()
marie.data_featuring()
mathilde.data_featuring()
angel.data_featuring()

# business life

ahmet.set_income(1000)
marie.set_income(3000)
angel.set_income(50)

ahmet.interest_rate1()
maxi.interest_rate1()
camille.interest_rate1()
camille.interest_rate1()
camille.interest_rate1()
marie.interest_rate1()

bank = [
    
        ahmet.data_remain_cleaning() , 
        maxi.data_remain_cleaning(),camille.data_remain_cleaning(),marie.data_remain_cleaning(),mathilde.data_remain_cleaning(),angel.data_remain_cleaning() 
    
    ]
df = pd.DataFrame.from_records(bank)
df


# In[ ]:




