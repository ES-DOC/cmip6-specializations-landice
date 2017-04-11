"""A realm sepecialization.

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
# CONTRIBUTORS: Set to realm specialization contributors (comma delimited).
# --------------------------------------------------------------------
CONTRIBUTORS = ''

# --------------------------------------------------------------------
# QUALITY CONTROL STATUS: Set to 'draft' or 'complete'
# --------------------------------------------------------------------
QC_STATUS = 'draft'

# --------------------------------------------------------------------
# CHANGE HISTORY: Set to list: (version, date, comment, who).
# --------------------------------------------------------------------
CHANGE_HISTORY = [
    ("0.1.0", "2016-04-11", "David Hassell",
        "Initialised from CMIP5 mind map + a bit of reorganising (but no logical difference)"),
]

# --------------------------------------------------------------------
# DESCRIPTION: Scientific context of this scientific realm
# --------------------------------------------------------------------
DESCRIPTION = 'Land Ice Realm'

# --------------------------------------------------------------------
# GRID: The grid used to layout the variables
# --------------------------------------------------------------------
GRID = 'landice_grid'

# --------------------------------------------------------------------
# KEY PROPERTIES: Key properties for the realm which differ from model defaults (grid, timestep etc)
# --------------------------------------------------------------------
KEY_PROPERTIES = 'landice_key_properties'

# --------------------------------------------------------------------
# PROCESSES: Processes simulated within the realm
# --------------------------------------------------------------------
PROCESSES = [
    'landice_glaciers',
    'landice_ice_sheet',
    'landice_ice_shelves',
]

# --------------------------------------------------------------------
# DETAILS: top level realm details
# --------------------------------------------------------------------
DETAILS = OrderedDict()

# --------------------------------------------------------------------
# ENUMERATIONS: top level realm enumerations
# --------------------------------------------------------------------
ENUMERATIONS = OrderedDict()