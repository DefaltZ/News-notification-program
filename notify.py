from notifypy import Notify

#use bsf to chart the code into variables
#the specific content of the site to be charted into the variables
#turn that variable into the notification title
#that will be cool

notification = Notify()
notification.title = "cool title"
notification.message = "even cooler message"
notification.send()