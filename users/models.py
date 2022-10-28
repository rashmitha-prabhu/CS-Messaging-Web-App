from email.policy import default
from django.db import models

# Create your models here.
URGENCY = (
    ('LOW', 'LOW'),
    ('MED', 'MED'),
    ('HIGH', 'HIGH')
)

class UserQuery(models.Model):
    userID = models.PositiveSmallIntegerField("User ID")
    timestamp = models.DateTimeField("Timestamp (UTC)", auto_now_add=True)
    messageBody = models.TextField("Message Body")
    urgency_status = models.CharField(max_length=20)
    resolved = models.BooleanField(default=False)

    def get_urgency_status(self, query):
        message = self.messageBody.lower()
        keywords = ['loan', 'approval', 'process', 'disburse', 'when']
        status = set(keywords).intersection(message.split())
        count = 0
        for word in status:
            count += message.split().count(word)

        if set(keywords).intersection(message.split()):
            return 'HIGH'
        return 'LOW'

    def save(self, *args, **kwargs):
        self.urgency_status = self.get_urgency_status(self.messageBody)
        super(UserQuery, self).save(*args, **kwargs)
