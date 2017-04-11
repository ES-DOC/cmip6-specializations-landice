"""A realm process sepecialization.

For further information goto http://wordpress.es-doc.org/cmip6-model-specializations.

"""
# --------------------------------------------------------------------
# INTERNAL (do not change)
# --------------------------------------------------------------------
from collections import OrderedDict

DETAILS = OrderedDict()
ENUMERATIONS = OrderedDict()

# --------------------------------------------------------------------
# CONTACT: Set to realm specialization co-ordinator.
# --------------------------------------------------------------------
CONTACT = 'David Hassell'

# --------------------------------------------------------------------
# AUTHORS: Set to realm specialization authors (comma delimited).
# --------------------------------------------------------------------
AUTHORS = 'David Hassell'

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# DESCRIPTION: Short description of the specialization.
# --------------------------------------------------------------------
DESCRIPTION = 'Land ice glaciers'

# --------------------------------------------------------------------
# PROCESS: top level properties
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'Key properties of land ice glaciers',
    'properties': [
        ('dynamic_areal_extent', 'bool', '1.1',
             'Does the model include a dynamic glacial extent?'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Mass Balance
# --------------------------------------------------------------------
DETAILS['mass_balance'] = {
    'description': 'TODO',
    'properties': [
        ('ablation_calculation', 'ENUM:ablation_calculation_types', '1.1',
             'Type of scheme used to model glacier ablation'),
        ('downscaling_technique', 'str', '1.1',
             'Describe how the atmospheric variables are used in the mass balance calculations'),
    ],
}

DETAILS['snow_treatment'] = {
    'description': 'TODO',
    'properties': [
        ('glacier_snow', 'ENUM:glacier_snow_methods', '1.1',
             'Treatment of glacier snow'),
        ('number_of_snow_layers', 'int', '0.1',
             'If glacier snow is different from land surface then how many layers in the glacier snow model?'),
        ('processes', 'ENUM:snow_processes', '0.N',
             'If glacier snow is different from land surface then describe processes describing snow on glaciers'),
    ],
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['ablation_calculation_types'] = {
    'description': 'Type of scheme used to model glacier ablation',
    'is_open': True,
    'members': [
        ('Energy balance model', None),
        ('PDD', None),
    ]
}

ENUMERATIONS['glacier_snow_methods'] = {
    'description': 'Treatment of glacier snow',
    'is_open': True,
    'members': [
        ('same as snow in land surface', None),
        ('different from snow in land surface', None),
        ]
    }

ENUMERATIONS['snow_processes'] = {
    'description': 'Processes describing snow on glaciers',
    'is_open': True,
    'members': [
        ('prognostic snow albedo', None),
        ('prognostic snow density', None),
        ('prognostic snow water equivalent', None),
        ('prognostic snow heat content', None),
        ('prognostic snow temperature', None),
        ('prognostic snow liquid water content', None),
        ('snow melting', None),
        ('snow refreezing', None),
        ('blowing snow', None),
    ]
}