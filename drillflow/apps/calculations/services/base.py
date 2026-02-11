class CalculationService:
    name = ""
    required_inputs = []

    def validate(self, data: dict):
        missing = [f for f in self.required_inputs if f not in data or data.get(f) is None]
        if missing:
            raise ValueError(f"Missing inputs: {missing}")

    def run(self, data: dict):
        raise NotImplementedError
class CalculationService:
    name = ""
    required_inputs = []

    def validate(self, data: dict):
        missing = [f for f in self.required_inputs if f not in data]
        if missing:
            raise ValueError(f"Missing inputs: {missing}")

    def run(self, data: dict):
        raise NotImplementedError
