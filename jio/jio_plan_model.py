class JioPlanModel:
    def __init__(self, amount, data, validity, sms, voice, total_data, description, category):
        self.amount = amount
        self.data = data
        self.validity = validity
        self.sms = sms
        self.voice = voice
        self.total_data = total_data
        self.description = description
        self.category = category

    def __init__(self, amount, data, validity, category):
        self.amount = amount
        self.data = data
        self.validity = validity
        self.sms = 'NA'
        self.voice = 'NA'
        self.total_data = 'NA'
        self.description = 'NA'
        self.category = category

    def __str__(self):
        return self.category + " | " + \
               self.amount + " | " + \
               self.data + " | " + \
               self.validity + " | " + \
               self.sms + " | " + \
               self.voice + " | " + \
               self.description


