from math import ceil
purchase = input('Enter your purchases (comma separated) : \n')
print()
purchases = purchase.split(',')
exempted_products = {'food':'chocolate', 'books':'book', 'meds':'headache pills'}
total_bill_amt = 0
total_tax = 0

print('Your invoice is: ')
for i in purchases:
   
    product = i.split('at ')[0]
    def is_imported(invoice):
    
        if 'imported' in invoice:
            return True
        else:
            return False
        
        

    def is_exempted(invoice):
        for value in exempted_products.values():
            if value in product:
                return True
                
            
        
       
    def calc_tax(invoice):
        if is_imported(i) and not is_exempted(i):
            tax = 15
    
        if is_imported(i) and is_exempted(i):
            tax = 5
        
        if not is_imported(i) and not is_exempted(i):
            tax = 10
    
        if not is_imported(i) and is_exempted(i):
            tax = 0
            
        return tax

    tax = calc_tax(i)
    
    
    cost = float(i.split('at ')[1])
   
    
    total_tax += cost*tax/100
    
    
    bill_amt = cost+(cost*tax/100)
    
    
    total_bill_amt+=bill_amt

    
    pur = product+"{0:.2f}".format(bill_amt)
    print(pur)

print("Sales Taxes: "+"{0:.2f}".format(total_tax))
print("Sales Taxes: "+"{0:.2f}".format(total_bill_amt))