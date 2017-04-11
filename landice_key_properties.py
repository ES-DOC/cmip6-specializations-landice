"""A realm key-properties sepecialization.

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
DESCRIPTION = 'Land ice key properties'

# --------------------------------------------------------------------
# KEY PROPERTIES: top level
# --------------------------------------------------------------------
DETAILS['toplevel'] = {
    'description': 'General key properties in land ice',
    'properties': [
        ('grounding_line_method', 'ENUM:grounding_line_methods', '1.1',
            'Specify the technique used for modelling the grounding line in the ice sheet-ice shelf coupling'),
        ('land_ice_albedo', 'ENUM:land_ice_albedo_methods', '1.N',
            'Specify how land ice albedo is modelled',),
        ]
    }

# --------------------------------------------------------------------
# KEY PROPERTIES: ENUMERATIONS
# --------------------------------------------------------------------
ENUMERATIONS['grounding_line_methods'] = {
    'description': 'Specify the technique used for modelling the grounding line in the ice sheet-ice shelf coupling',
    'is_open': True,
    'members': [
        ('grounding line prescribed', None),
        ('flux prescribed (Schoof)', None),
        ('fixed grid size', None),
        ('moving grid', None),
    ]
}

ENUMERATIONS['land_ice_albedo_methods'] = {
    'description': 'Specify how land ice albedo is modelled',
    'is_open': True,
    'members': [
        ('prescribed', None),
        ('function of ice age', None),
        ('function of ice density', None),
    ]
}