from .base import CalculationService


class RheologyService(CalculationService):
    name = "rheology"
    required_inputs = ["rpm_600", "rpm_300"]

    def run(self, data: dict):
        self.validate(data)
        pv = data.get("rpm_600") - data.get("rpm_300")
        yp = data.get("rpm_300") - pv
        av = data.get("rpm_600") / 2 if data.get("rpm_600") is not None else None
        return {"PV": pv, "YP": yp, "AV": av}
