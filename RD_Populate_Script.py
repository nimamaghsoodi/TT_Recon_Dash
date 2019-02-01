import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ReconDashboard.settings')

import django
django.setup()

#Fake pop script
import random
from RDApp.models import ReconUpdate
from faker import Faker

fakegen = Faker()
# topics = ['ReconTitle','RespPers','ReconTotalCount','ReconExecutedCount','ReconDate']

# def add_topic():
#     t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#     return t

def populate(N=5):
    for entry in range(N):

        # top = add_topic()

        fake_title = fakegen.sentence()
        fake_name = fakegen.name()
        fake_total_count = fakegen.random_number()
        fake_executed_count = fakegen.random_number()
        fake_recon_date = fakegen.date_object(end_datetime=None)

        insert_rec = ReconUpdate.objects.get_or_create(ReconTitle=fake_title,RespPers=fake_name
                                                        ,ReconTotalCount=fake_total_count
                                                        ,ReconExecutedCount=fake_executed_count
                                                        ,ReconDate=fake_recon_date)[0]

if __name__ == '__main__':
    print('Populating in progress...')
    populate(120)
    print('Populating finished!!')
