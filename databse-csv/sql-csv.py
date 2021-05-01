with open('dump.csv', 'wb') as f:
    out = csv.writer(f)
    out.writerow(['id', 'description'])

    for item in session.query(Queue).all():
        out.writerow([item.id, item.description])