class OwnerNotOnboardedError(Exception):
    def __init__(self, owner, message="User not onboarded"):
        self.owner = owner
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.owner} -> {self.message}"


class TableAlreadyExistsError(Exception):
    def __init__(self, tablename, message="Table already exists"):
        self.tablename = tablename
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.tablename} -> {self.message}"


class OwnerAlreadyOnboardedError(Exception):
    def __init__(self, owner, message="User already onboarded"):
        self.owner = owner
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.owner} -> {self.message}"
