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


class OwnerNameInvalidError(Exception):
    def __init__(self, owner, message="Username may only contain "
                 " a-z, and must be lowercase"):
        self.owner = owner
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.owner} -> {self.message}"


class TableNameInvalidError(Exception):
    def __init__(self, tablename, message="Table name may only contain "
                 " a-z and _, and must be lowercase"):
        self.tablename = tablename
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.tablename} -> {self.message}"


class HeadersNotCSVError(Exception):
    def __init__(self, headers, message="Headers must be comma-separated"):
        self.headers = headers
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"{self.headers} -> {self.message}"


class InvalidTypeError(Exception):
    def __init__(self, type_):
        valid_types = ["TEXT", "BOOLEAN", "INTEGER","DECIMAL"]
        type_s = ", ".join(type_x for type_x in valid_types)
        self.type_ = type_
        self.message = f"Valid Types Are: {type_s}"
        super().__init__(self.message)

    def __str__(self):
        return f"{self.type_} -> {self.message}"


class TypesAssymetricalError(Exception):
    def __init__(self, type_len, headers_len):
        self.type_len = type_len
        self.headers_len = headers_len
        self.message = f"Length of Headers: {type_len}\n" \
            f"Length of Types: {headers_len}"
        super().__init__(self.message)

    def __str__(self):
        return self.message


class TimeNotEpochError(Exception):
    def __init__(self, snapshot):
        self.snapshot = snapshot
        self.message = f"Valid Types Are: {snapshot}"
        super().__init__(self.message)

    def __str__(self):
        return f"{self.snapshot} -> {self.message}"

'''
class FileEmptyError(Exception):
    def __init__(self, snapshot):
        self.snapshot = snapshot
        self.message = f"Valid Types Are: {snapshot}"
        super().__init__(self.message)

    def __str__(self):
        return f"{self.snapshot} -> {self.message}"'''
        
