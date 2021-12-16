import django  # nopep8
django.setup()  # nopep8

from apscheduler.schedulers.blocking import BlockingScheduler
from products.clock import update_historic

sched = BlockingScheduler({'apscheduler.timezone': 'America/Sao_Paulo'})


@sched.scheduled_job('cron', day_of_week='mon-sun', hour=7)
def update_historic_cron():
    print('----STARTING PRICE CHECK----')
    update_historic()
    print('----FINISHING PRICE CHECK----')


sched.start()
