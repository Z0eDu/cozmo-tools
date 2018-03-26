from .worldmap import *

def make_walls():

    # ~12 inch walls

    w1 = WallSpec(length=600, height=190, door_width = 77, door_height=110,
                    markers={ 1 : (+1, ( 65., 50.)),
                              2 : (+1, (153.,150.)),
                              3 : (+1, (241., 50.)),
                              4 : (+1, (359., 50.)),
                              5 : (+1, (447.,150.)),
                              6 : (+1, (535., 50.)),
                             12 : (-1, ( 65., 50.)),
                             11 : (-1, (153.,150.)),
                             10 : (-1, (241., 50.)),
                              9 : (-1, (359., 50.)),
                              8 : (-1, (447.,150.)),
                              7 : (-1, (535., 50.))  },
                    doorways = [ (153., 77.), (447., 77.) ],
                    door_ids = [ 2, 5, 8, 11 ])

    w13 = WallSpec(length=600, height=190, door_width = 77, door_height=110,
                    markers={ 13 : (+1, ( 65., 50.)),
                              14 : (+1, (153.,150.)),
                              15 : (+1, (241., 50.)),
                              16 : (+1, (359., 50.)),
                              17 : (+1, (447.,150.)),
                              18 : (+1, (535., 50.)),
                              24 : (-1, ( 65., 50.)),
                              23 : (-1, (153.,150.)),
                              22 : (-1, (241., 50.)),
                              21 : (-1, (359., 50.)),
                              20 : (-1, (447.,150.)),
                              19 : (-1, (535., 50.))  },
                    doorways = [ (153., 77.), (447., 77.) ],
                    door_ids = [ 14,17,20,23])

    w25 = WallSpec(length=600, height=190, door_width = 77, door_height=110,
                    markers={ 25 : (+1, ( 65., 50.)),
                              26 : (+1, (153.,150.)),
                              27 : (+1, (241., 50.)),
                              28 : (+1, (359., 50.)),
                              29 : (+1, (456.,150.)),
                              30 : (+1, (535., 50.)),
                              36  : (-1, ( 65., 50.)),
                              35  : (-1, (153.,150.)),
                              34  : (-1, (241., 50.)),
                              33  : (-1, (359., 50.)),
                              32  : (-1, (447.,150.)),
                              31  : (-1, (535., 50.))  },
                    doorways = [ (153., 77.), (447., 77.) ],
                    door_ids = [ 26,29,32,35])

    
    # ~9 inch walls
    w49 = WallSpec(length=400, height=190, door_width = 77, door_height=110,
                    markers={ 49 : (+1, ( 112., 50.)),
                              50 : (+1, (200.,150.)),
                              51 : (+1, (288., 50.)),
                              54 : (-1, ( 112., 50.)),
                              53 : (-1, (200.,150.)),
                              52 : (-1, (288., 50.))},
                    doorways = [ (200., 77.) ],
                    door_ids = [ 50,53])

    w55 = WallSpec(length=400, height=190, door_width = 77, door_height=110,
                    markers={ 55 : (+1, ( 112., 50.)),
                              56 : (+1, (200.,150.)),
                              57 : (+1, (288., 50.)),
                              60 : (-1, ( 112., 50.)),
                              59 : (-1, (200.,150.)),
                              58 : (-1, (288., 50.))},
                    doorways = [ (200., 77.) ],
                    door_ids = [ 56,59])
    
    
    
    
    
    # ~6 inch walls

    w37 = WallSpec(length=300, height=190, door_width = 77, door_height=110,
                    markers={ 37 : (+1, ( 62., 50.)),
                              38 : (+1, (150.,150.)),
                              39 : (+1, (238., 50.)),
                              42 : (-1, ( 62., 50.)),
                              41 : (-1, (150.,150.)),
                              40 : (-1, (238., 50.))},
                    doorways = [ (150., 77.) ],
                    door_ids = [ 38,41])

    w43 = WallSpec(length=300, height=190, door_width = 77, door_height=110,
                    markers={ 43 : (+1, ( 62., 50.)),
                              44 : (+1, (150.,150.)),
                              45 : (+1, (238., 50.)),
                              48 : (-1, ( 62., 50.)),
                              47 : (-1, (150.,150.)),
                              46 : (-1, (238., 50.))},
                    doorways = [ (150., 77.) ],
                    door_ids = [ 44,47])

    
    
make_walls()
