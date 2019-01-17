from crontab import CronTab

cron = CronTab('root')  
job = cron.new(command='python ~/fabriccron/n.py')  
job.minute.every(30)

cron.write()
