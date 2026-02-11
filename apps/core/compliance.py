# --- API RP 13B Compliance Utilities ---

API_RP_13B_LIMITS = {
    'mud_weight_min': 8.5,  # ppg
    'mud_weight_max': 19.0, # ppg
    # Add more regulated parameters as needed
}

def check_api_rp_13b_compliance(param, value):
    """Check if a value is within API RP 13B limits."""
    if param in API_RP_13B_LIMITS:
        min_val = API_RP_13B_LIMITS.get(f'{param}_min')
        max_val = API_RP_13B_LIMITS.get(f'{param}_max')
        if min_val is not None and value < min_val:
            return False, f"{param} below API minimum ({min_val})"
        if max_val is not None and value > max_val:
            return False, f"{param} above API maximum ({max_val})"
    return True, "OK"

# --- Regulated Parameter Locking ---
LOCKED_PARAMETERS = set()

def lock_parameter(param):
    LOCKED_PARAMETERS.add(param)

def is_parameter_locked(param):
    return param in LOCKED_PARAMETERS

# --- Company Override Logic ---
COMPANY_OVERRIDES = {}

def set_company_override(company, param, value):
    COMPANY_OVERRIDES[(company, param)] = value

def get_company_override(company, param):
    return COMPANY_OVERRIDES.get((company, param))

# --- Regional Compliance Flags ---
REGIONAL_FLAGS = {}

def set_regional_flag(region, flag, value):
    REGIONAL_FLAGS[(region, flag)] = value

def get_regional_flag(region, flag):
    return REGIONAL_FLAGS.get((region, flag))

# --- Calculation Assumptions Display ---
ASSUMPTIONS = {}

def set_assumption(calc_type, text):
    ASSUMPTIONS[calc_type] = text

def get_assumption(calc_type):
    return ASSUMPTIONS.get(calc_type, "No assumptions documented.")

# --- Validation Warnings System ---
VALIDATION_WARNINGS = []

def add_validation_warning(msg):
    VALIDATION_WARNINGS.append(msg)

def get_validation_warnings():
    return VALIDATION_WARNINGS

# --- Compliance Mode Toggles ---
COMPLIANCE_MODES = {'api': True, 'company': False, 'regional': False}

def set_compliance_mode(mode, enabled):
    COMPLIANCE_MODES[mode] = enabled

def get_compliance_mode(mode):
    return COMPLIANCE_MODES.get(mode, False)

# --- Export Standards Summary ---
def export_standards_summary():
    summary = {
        'api_limits': API_RP_13B_LIMITS,
        'company_overrides': COMPANY_OVERRIDES,
        'regional_flags': REGIONAL_FLAGS,
        'compliance_modes': COMPLIANCE_MODES,
    }
    return summary
