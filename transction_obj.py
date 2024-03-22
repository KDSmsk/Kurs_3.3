class transaction:

    def __init__(self):
        self.id = None
        self.state = None
        self.date = None
        self.operationAmount = None
        self.description = None
        self.from_ = None
        self.to_ = None
        self.info = "Курсовая №3"


    def get_id(self):
        return self.id

    def get_state(self):
        return self.state

    def get_date(self):
        return self.date

    def get_many_id(self):
        return self.operationAmount['currency']['code']

    def get_many_cont(self):
        return self.operationAmount['amount']

    def get_description(self):
        return self.description

    def get_from(self):
        return self.from_

    def get_to(self):
        return self.to_

    def set_param_from_json(self, json_dict):
        for key, value in json_dict.items():
            if key == "id":
                self.id = value
            elif key == "state":
                self.state = value
            elif key == "date":
                self.date = value
            elif key == "operationAmount":
                self.operationAmount = value
            elif key == "description":
                self.description = value
            elif key == "from":
                self.from_ = value
            elif key == "to":
                self.to_ = value
    def __repr__(self):
        return self.info