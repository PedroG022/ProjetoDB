class User():

    def __init__(self, name, email, password, birthDate, subscription, address, phone, paymentMethod):
        self.name = name
        self.email = email
        self.password = password
        self.birthDate = birthDate
        self.subscription = subscription
        self.address = address
        self.phone = phone
        self.paymentMethod = paymentMethod

    def __str__(self):
        return "Name: %s\nEmail: %s\nPassword: %s\nBirthDate: %s\nSubscription: %s\nAddress: %s\nPhone: %s\nPaymentMethod: %s" % (self.name, self.email, self.password, self.birthDate, self.subscription, self.address, self.phone, self.paymentMethod)

    def toSql(self):
        return "('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (self.name, self.email, self.password, self.birthDate, self.subscription, self.address, self.phone, self.paymentMethod)

    def fromSql(self, row):
        self.name = row[0]
        self.email = row[1]
        self.password = row[2]
        self.birthDate = row[3]
        self.subscription = row[4]
        self.address = row[5]
        self.phone = row[6]
        self.paymentMethod = row[7]
        return self
