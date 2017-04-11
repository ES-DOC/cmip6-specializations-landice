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
DESCRIPTION = 'Land ice sheets'

# --------------------------------------------------------------------
# PROCESS: top level properties
# --------------------------------------------------------------------

# --------------------------------------------------------------------
# SUB-PROCESS: Mass Balance
# --------------------------------------------------------------------
DETAILS['mass_balance'] = {
    'description': 'TODO',
    'properties': [
        ('ablation_calculation', 'ENUM:ablation_calculation_types', '1.1',
             'Type of scheme used to calcualte ablation in te ice sheet mass balance'),
        ('downscaling_technique', 'str', '1.1',
             'Describe how the atmospheric variables are used in the mass balance calculations'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Dynamics
# --------------------------------------------------------------------
DETAILS['dynamics'] = {
    'description': 'TODO',
    'properties': [
        ('coupling_wth_atmosphere', 'str', '1.1',
             'Describe the coupling method between the land ice sheet and atmosphere'),
    ],
    'detail_sets': [
        'model_numerics',
    ]
}

DETAILS['dynamics:model_numerics'] = {
    'description': 'TODO',
    'properties': [
        ('timestep', 'int', '1.1',
             'Timestep (in seconds) of the land ice sheet scheme',),        
        ('uses_land_surface_timestep', 'bool', '1.1',
             'Is the timestep the same as land surface timestep?'),
        ('approximation', 'ENUM:approximation_types', '1.1',
            'Approximation type used in modelling ice sheet dynamics'),
        ('ice_streams', 'bool', '1.1',
             'Are ice streams modelled within the land ice model?'),
    ],
}

# --------------------------------------------------------------------
# SUB-PROCESS: Snow treatment
# --------------------------------------------------------------------
DETAILS['snow_treatment'] = {
    'description': 'TODO',
    'properties': [
        ('ice_sheet_snow', 'ENUM:ice_sheet_snow_methods', '1.1',
             'Treatment of ice sheet snow'),
        ('number_of_snow_layers', 'int', '0.1',
             'If ice sheet snow is different from land surface then how many layers in the ice sheet snow model?'),
        ('prognostic_variables', 'ENUM:snow_prognostic_variables', '0.N',
             'If ice sheet snow is different from land surface then list the prognostic variables the ice sheet snow model'),
        ('processes', 'ENUM:ice_sheet_snow_processes', '0.N',
             'If ice sheet snow is different from land surface then describe processes describing snow on ice sheets'),
    ],
}

# --------------------------------------------------------------------
# ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['ablation_calculation_types'] = {
    'description': 'Type of scheme used to model ice sheet ablation',
    'is_open': True,
    'members': [
        ('Energy balance model', None),
        ('PDD', None),
    ]
}

ENUMERATIONS['approximation_types'] = {
    'description': 'Approximation type used in modelling ice sheet dynamics',
    'is_open': True,
    'members': [
        ('shallow ice', None),
        ('higher order', None),
        ('full stokes', None),
        ]
    }

ENUMERATIONS['ice_sheet_snow_methods'] = {
    'description': 'Treatment of ice sheet snow',
    'is_open': True,
    'members': [
        ('same as snow in land surface', None),
        ('different from snow in land surface', None),
    ]
}

ENUMERATIONS['snow_prognostic_variables'] = {
    'description': 'Prognostic variables the ice sheet snow model',
    'is_open': True,
    'members': [
        ('snow albedo', None),
        ('snow density', None),
        ('snow water equivalent', None),
        ('snow heat content', None),
        ('snow temperature', None),
        ('snow liquid water content', None),
    ]
}

ENUMERATIONS['ice_sheet_snow_processes'] = {
    'description': 'Processes describing snow on ice sheets',
    'is_open': True,
    'members': [
        ('snow melting', None),
        ('snow refreezing', None),
        ('blowing snow', None),
    ]
}
