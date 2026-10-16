from math import floor

MARKUP = 2.0

def get_equipment_list():
    equipment = {
                "SP32950VSPX1 2.7HP VS":        1814.61,
                "SP23520VSPX1 1.65HP VS":       1353.02,
                "HSP30060 Booster Pump":        509.25,
                "Polaris 280":                  713.81,
                "S310S":                        1205.39,
                "S244S":                        920.31,
                "SP0715X62 Valve":              345.31,
                "C5030 Cartridge Filter":       1704.79,
                "C4030 Cartridge Filter":       1322.79,
                "HDFS400":                      3841.50,
                "HDFS275":                      3095.05,
                "HP31405T":                     4913.97,
                "GPC-25 Chiller":               2962.16,
                "AQRS340":                      1994.85,
                "AQRS325":                      1721.09,
                "CL200EF":                      118.82,
                "FUSION":                       466.61,
                "DuoClear Cartridge":           271.84,
                "Rainbow 320 - R171096":        156.80,
                "LACUS11100":                   482.14,
                "WFB100 Bubbler":               133.15,
                "300W 12/13/14V Transformer":   123.96,
                "HLPRO4W":                      1899.23,
                "HLPRO4SW":                     2682.70,
                "Actuator GVA-24":              213.20,
                "T104P3 Timer":                 117.01,
                "SPB101 1hp 115v Blower":       206.99,
                "SPB152 1.5hp 230v Blower":     236.23,
                # extra lines for stuff. impossible to get to = 0 with floor function
                "Miscellaneous(Only 1 misc line!)": 0,
                "Final Price Adjustment": 0,
            }

    return {name: retail_price(cost) for name, cost in equipment.items()}


def retail_price(price):
    return floor(price * MARKUP) + 0.95