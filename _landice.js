(function (APP) {

    // ECMAScript 5 Strict Mode
    "use strict";

    // Register with application.
    APP.registerTopic({"id": "cmip6.landice", "label": "Landice", "description": "Land Ice Realm", "contact": "David Hassell", "authors": ["David Hassell"], "contributors": ["Sophie Nowicki", "Steve George"], "project": "cmip6", "changeHistory": [{"note": "Initialised from CMIP5 mind map", "date": "2016-04-11", "version": "0.1.0", "author": "David Hassell (NCAS)"}, {"note": "Updated with input from Steve George (NCAS)", "date": "2017-04-25", "version": "0.2.0", "author": "David Hassell (NCAS)"}, {"note": "Updated with input from Sophie Nowicki (NASA)", "date": "2017-05-22", "version": "0.3.0", "author": "David Hassell"}, {"note": "Reorganisation of grid info; first draft of short table", "date": "2017-06-28", "version": "0.4.0", "author": "David Hassell (NCAS)"}, {"note": "Updated with input from Christian Rodehacke (DMI)", "date": "2017-12-15", "version": "0.5.0", "author": "David Hassell (NCAS)"}], "qcStatus": "draft", "shortTables": [], "subTopics": [{"id": "cmip6.landice.key_properties", "label": "Key Properties", "description": "Land ice key properties", "contact": "David Hassell", "properties": [{"id": "cmip6.landice.key_properties.overview", "label": "Overview", "description": "Overview of land surface model.", "cardinality": "1.1", "type": "str"}, {"id": "cmip6.landice.key_properties.model_name", "label": "Model Name", "description": "Name of land surface model code", "cardinality": "1.1", "type": "str"}, {"id": "cmip6.landice.key_properties.ice_albedo", "label": "Ice Albedo", "description": "Specify how ice albedo is modelled", "cardinality": "1.N", "type": "enum", "enum": {"id": "Specify how ice albedo is modelled", "label": "Ice Albedo Methods", "description": "Specify how ice albedo is modelled", "is_open": true, "choices": [{"description": null, "value": "prescribed"}, {"description": null, "value": "function of ice age"}, {"description": null, "value": "function of ice density"}]}}, {"id": "cmip6.landice.key_properties.atmospheric_coupling_variables", "label": "Atmospheric Coupling Variables", "description": "Which variables are passed between the atmosphere and ice (e.g. orography, ice mass)", "cardinality": "1.1", "type": "str"}, {"id": "cmip6.landice.key_properties.oceanic_coupling_variables", "label": "Oceanic Coupling Variables", "description": "Which variables are passed between the ocean and ice", "cardinality": "1.1", "type": "str"}, {"id": "cmip6.landice.key_properties.prognostic_variables", "label": "Prognostic Variables", "description": "Which variables are prognostically calculated in the ice model", "cardinality": "1.N", "type": "enum", "enum": {"id": "Which variables are prognostically calculated in the ice model", "label": "Prognostic Variable Types", "description": "Which variables are prognostically calculated in the ice model", "is_open": true, "choices": [{"description": null, "value": "ice velocity"}, {"description": null, "value": "ice thickness"}, {"description": null, "value": "ice temperature"}]}}, {"id": "cmip6.landice.key_properties.software_properties.repository", "label": "Software Properties > Repository", "description": "Location of code for this component.", "cardinality": "0.1", "type": "str"}, {"id": "cmip6.landice.key_properties.software_properties.code_version", "label": "Software Properties > Code Version", "description": "Code version identifier.", "cardinality": "0.1", "type": "str"}, {"id": "cmip6.landice.key_properties.software_properties.code_languages", "label": "Software Properties > Code Languages", "description": "Code language(s).", "cardinality": "0.N", "type": "str"}]}, {"id": "cmip6.landice.grid", "label": "Grid", "description": "Land ice grid", "contact": "David Hassell", "properties": [{"id": "cmip6.landice.grid.overview", "label": "Overview", "description": "Overview of the grid in the land ice scheme", "cardinality": "1.1", "type": "str"}, {"id": "cmip6.landice.grid.adaptive_grid", "label": "Adaptive Grid", "description": "Is an adative grid being used?", "cardinality": "1.1", "type": "bool"}, {"id": "cmip6.landice.grid.base_resolution", "label": "Base Resolution", "description": "The base resolution (in metres), before any adaption", "cardinality": "1.1", "type": "float"}, {"id": "cmip6.landice.grid.resolution_limit", "label": "Resolution Limit", "description": "If an adaptive grid is being used, what is the limit of the resolution (in metres)", "cardinality": "0.1", "type": "float"}, {"id": "cmip6.landice.grid.projection", "label": "Projection", "description": "The projection of the land ice grid (e.g. albers_equal_area)", "cardinality": "1.1", "type": "str"}]}, {"id": "cmip6.landice.glaciers", "label": "Glaciers", "description": "Land ice glaciers", "contact": "David Hassell", "properties": [{"id": "cmip6.landice.glaciers.overview", "label": "Overview", "description": "Overview of glaciers in the land ice scheme", "cardinality": "1.1", "type": "str"}, {"id": "cmip6.landice.glaciers.description", "label": "Description", "description": "Describe the treatment of glaciers, if any", "cardinality": "1.1", "type": "str"}, {"id": "cmip6.landice.glaciers.dynamic_areal_extent", "label": "Dynamic Areal Extent", "description": "Does the model include a dynamic glacial extent?", "cardinality": "0.1", "type": "bool"}]}, {"id": "cmip6.landice.ice", "label": "Ice", "description": "Ice sheet and ice shelf", "contact": "David Hassell", "properties": [{"id": "cmip6.landice.ice.overview", "label": "Overview", "description": "Overview of the ice sheet and ice shelf in the land ice scheme", "cardinality": "1.1", "type": "str"}, {"id": "cmip6.landice.ice.grounding_line_method", "label": "Grounding Line Method", "description": "Specify the technique used for modelling the grounding line in the ice sheet-ice shelf coupling", "cardinality": "1.1", "type": "enum", "enum": {"id": "Specify the technique used for modelling the grounding line in the ice sheet-ice shelf coupling", "label": "Grounding Line Methods", "description": "Specify the technique used for modelling the grounding line in the ice sheet-ice shelf coupling", "is_open": true, "choices": [{"description": null, "value": "grounding line prescribed"}, {"description": null, "value": "flux prescribed (Schoof)"}, {"description": null, "value": "fixed grid size"}, {"description": null, "value": "moving grid"}]}}, {"id": "cmip6.landice.ice.ice_sheet", "label": "Ice Sheet", "description": "Are ice sheets simulated?", "cardinality": "1.1", "type": "bool"}, {"id": "cmip6.landice.ice.ice_shelf", "label": "Ice Shelf", "description": "Are ice shelves simulated?", "cardinality": "1.1", "type": "bool"}, {"id": "cmip6.landice.ice.mass_balance.surface_mass_balance", "label": "Mass Balance > Surface Mass Balance", "description": "Describe how and where the surface mass balance (SMB) is calulated. Include the temporal coupling frequeny from the atmosphere, whether or not a seperate  SMB model is used, and if so details of this model, such as its resolution", "cardinality": "1.1", "type": "str"}, {"id": "cmip6.landice.ice.mass_balance.basal.bedrock", "label": "Mass Balance > Basal > Bedrock", "description": "Describe the implementation of basal melting over bedrock", "cardinality": "0.1", "type": "str"}, {"id": "cmip6.landice.ice.mass_balance.basal.ocean", "label": "Mass Balance > Basal > Ocean", "description": "Describe the implementation of basal melting over the ocean", "cardinality": "0.1", "type": "str"}, {"id": "cmip6.landice.ice.mass_balance.frontal.calving", "label": "Mass Balance > Frontal > Calving", "description": "Describe the implementation of calving from the front of the ice shelf", "cardinality": "0.1", "type": "str"}, {"id": "cmip6.landice.ice.mass_balance.frontal.melting", "label": "Mass Balance > Frontal > Melting", "description": "Describe the implementation of melting from the front of the ice shelf", "cardinality": "0.1", "type": "str"}, {"id": "cmip6.landice.ice.dynamics.description", "label": "Dynamics > Description", "description": "General description if ice sheet and ice shelf dynamics", "cardinality": "1.1", "type": "str"}, {"id": "cmip6.landice.ice.dynamics.approximation", "label": "Dynamics > Approximation", "description": "Approximation type used in modelling ice dynamics", "cardinality": "1.N", "type": "enum", "enum": {"id": "Approximation type used in modelling ice sheet dynamics", "label": "Approximation Types", "description": "Approximation type used in modelling ice sheet dynamics", "is_open": true, "choices": [{"description": null, "value": "SIA"}, {"description": null, "value": "SAA"}, {"description": null, "value": "full stokes"}]}}, {"id": "cmip6.landice.ice.dynamics.adaptive_timestep", "label": "Dynamics > Adaptive Timestep", "description": "Is there an adaptive time scheme for the ice scheme?", "cardinality": "1.1", "type": "bool"}, {"id": "cmip6.landice.ice.dynamics.timestep", "label": "Dynamics > Timestep", "description": "Timestep (in seconds) of the ice scheme. If the timestep is adaptive, then state a representative timestep.", "cardinality": "1.1", "type": "int"}]}]});

}(this.APP));