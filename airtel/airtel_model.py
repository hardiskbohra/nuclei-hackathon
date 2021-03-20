class AirtelModel:
    def __init__(self, amount, data, validity, sms, tag, additionalInfo, otherInfo):
        self.amount = amount
        self.data = data
        self.validity = validity
        self.sms = sms
        self.tag = tag
        self.additionalInfo = additionalInfo
        self.otherInfo = otherInfo


    def __str__(self):
        return self.tag + " | " + \
               self.amount + " | " + \
               self.data + " | " + \
               self.validity + " | " + \
               self.sms + " | " + \
               self.additionalInfo + " | " + \
                self.otherInfo


