class User():

    def __init__(self, name, email, password, birthDate, subscription, address, phone, paymentMethod):
        self.id = -1
        self.name = name
        self.email = email
        self.password = password
        self.birthDate = birthDate
        self.subscription = subscription
        self.address = address
        self.phone = phone
        self.paymentMethod = paymentMethod

    def __str__(self):
        return "Id: %s\nName: %s\nEmail: %s\nPassword: %s\nBirthDate: %s\nSubscription: %s\nAddress: %s\nPhone: %s\nPaymentMethod: %s" % (self.id, self.name, self.email, self.password, self.birthDate, self.subscription, self.address, self.phone, self.paymentMethod)

    def toSql(self):
        return "('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (self.name, self.email, self.password, self.birthDate, self.subscription, self.address, self.phone, self.paymentMethod)

    def columns(self):
        return "(name, email, password, birthDate, subscription, address, phone, paymentMethod)"

    def fromSql(self, row):
        self.id = row[0]
        self.name = row[1]
        self.email = row[2]
        self.password = row[3]
        self.birthDate = row[4]
        self.subscription = row[5]
        self.address = row[6]
        self.phone = row[7]
        self.paymentMethod = row[8]
        return self
