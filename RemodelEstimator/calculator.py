
# Base rates — change these as needed
RATES = {
    "prep_rate" : 100.00,           #$/linear foot
    "sandblast" : 6000.00,          #$
    "full_plumb_rate" : 3000.00,    #$
    "partial_plumb_rate" : 1800.00, #$
    "min_plumb_rate" : 800.00,      #$
    "plaster_rate" : 27.66,         #$ per sqft
    "tile_rate" : 100,              #$ per sqft
    "materials_rate" : 7,           #$ per sqft of tile
}

#tile calc : 10ft per day, 8hr day, $100 hr

def calculate_estimate(measurements, options, equipment):
    # getting vars out of lib of user entries
    prep_linfeet = measurements["prep_linear_feet"]
    tile_sqft = measurements["tile_sqft"]
    plaster_sqft = measurements["plaster_sqft"]
    tile_width = measurements["tile_width"]
    tile_height = measurements["tile_height"]


    # change vars based on non-local jobs
    if not options["localjob"]:
        # TODO: add modifiers with Katy

        pass

    #various totals
    prep_total = 0.00
    tile_total = 0.00
    plaster_total = 0.00
    equipment_total = 0.00
    plumbing_total = 0.00

    #tile vars
    tile_hours_per_day = 8 #hrs per day they can work on tile
    tile_done_per_day = 10 #sqft
    tile_smooth_factor = 37 #magic number. higher = smoother increase, lower = sharper increase.
    #magic tile price smoothing factor
    tile_fraction = (((tile_width * tile_height) + tile_smooth_factor) / (36 + tile_smooth_factor))

    #optional modifiers
    if options["sandblast"]:
        prep_total += RATES["sandblast"]

    if options["fullplumb"]:
        plumbing_total += RATES["full_plumb_rate"]

    if options["partplumb"]:
        plumbing_total += RATES["partial_plumb_rate"]

    if options["minplumb"]:
        plumbing_total += RATES["min_plumb_rate"]


    # tile
    tile_materials = tile_sqft * RATES["materials_rate"]#materials for doing tile
    tile_total += tile_sqft * RATES["tile_rate"] * tile_hours_per_day / tile_done_per_day / tile_fraction
    tile_total *= 1.05 #"just in case" factor
    tile_total += tile_materials

    #prep
    prep_total += prep_linfeet * RATES["prep_rate"]

    #plaster
    plaster_total += plaster_sqft * RATES["plaster_rate"]

    #equipment
    equipment_total += sum(eq["quantity"] * eq["price"] for eq in equipment)

    #add up everything
    total_cost = prep_total + tile_total + plaster_total + equipment_total + plumbing_total

    if options["divepool"]:
        total_cost += 2500


    return \
        {
        "prep_total": prep_total,
        "tile_total": tile_total,
        "plaster_total": plaster_total,
        "equipment_total": equipment_total,
        "plumbing_total": plumbing_total,
        "total_cost": total_cost,
        }