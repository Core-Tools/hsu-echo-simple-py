from hsu_echo.domain.contract import Contract

class SimpleHandler(Contract):
    def __init__(self):
        pass

    def Echo(self, message: str) -> str:
        return "py-simple-echo: " + message
