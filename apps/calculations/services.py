from decimal import Decimal

# --- Calculation Service Layer ---
class CalculationService:
    """Service layer for drilling fluids calculations"""
    @staticmethod
    def calculate_pv(θ600, θ300):
        """Plastic Viscosity (PV) = θ600 - θ300"""
        return Decimal(θ600) - Decimal(θ300)

    @staticmethod
    def calculate_yp(θ300, pv):
        """Yield Point (YP) = θ300 - PV"""
        return Decimal(θ300) - Decimal(pv)

    @staticmethod
    def calculate_av(θ600):
        """Apparent Viscosity (AV) = θ600 / 2"""
        return Decimal(θ600) / Decimal(2)

    @staticmethod
    def bingham_model(θ600, θ300):
        pv = CalculationService.calculate_pv(θ600, θ300)
        yp = CalculationService.calculate_yp(θ300, pv)
        av = CalculationService.calculate_av(θ600)
        return {'PV': pv, 'YP': yp, 'AV': av}

    # Add more rheology, hydraulics, ECD, surge/swab, hole cleaning, etc. as needed
