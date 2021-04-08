from database import db, Cars

# Creating tables
db.create_all()

chevy_tahoe = Cars('Chevrolet Tahoe', 420)
yukon = Cars('GMC Yukon', 420)

# Passing values to the database
db.session.add_all([chevy_tahoe, yukon])

# Or adding one by one
# db.session.add(chevy_tahoe)

# Commiting changes 
db.session.commit()