import csv
from ..models import UserQuery

def run() :
    with open('GeneralistRails_Project_MessageData.csv') as file : 
        reader = csv.reader(file)
        next(reader)

        UserQuery.objects.all().delete()

        for row in reader:
            query = UserQuery(userID=row[0], timestamp=row[1], messageBody=row[2])
            query.save()
