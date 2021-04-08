from database import db, Cars

# Create
new_car = Cars( 'Nissan GTR', 600 )
db.session.add( new_car )
db.session.commit()

# Read
all_cars = Cars.query.all() # Reading all cars in the database 

# Select by id
first_car = Cars.query.get(1)

# Filtering
gmc_cars = Cars.query.filter_by( name = 'GMC' )

# Update 
first_car = Cars.query.get(1)
first_car.horse_power = 345
db.session.add(first_car)
db.session.commit()

# Delete
second_car = Cars.query.get(2)
db.session.delete(second_car)
db.session.commit()