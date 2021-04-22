from csv import DictWriter
with open('final.csv','w',newline='') as f:
    csv_writer=DictWriter(f,fieldnames=['firstname','lastname','age'])
    csv_writer.writeheader()
    # we have two method 
    # writerow 
    # writerows
    csv_writer.writerow({
        'firstname':'ANubhav',
        'lastname':'shukla',
        'age':22

    })
    csv_writer.writerow({
        'firstname':'Ashish',
        'lastname':'shukla',
        'age':24

    })

# writerows

    csv_writer.writerows([
         {'firstname':'Anubhav','lastname':'shukla','age':22},
         {'firstname':'ashish','lastname':'shukla','age':24},
         {'firstname':'Ambika','lastname':'shukla','age':48},

     ])
