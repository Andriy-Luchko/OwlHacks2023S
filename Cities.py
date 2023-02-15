class City:
    def __init__(self, name, Distances, Population, DiseasesPopulation):
        self.Name = name
        # A dictionary of distances in miles to other Cities with City names as the keys
        self.Distances = Distances
        # City Population Int
        self.Population = Population
        # A dictionary with disease names as the keys and affected population in city as values.
        self.DiseasesPopulation = DiseasesPopulation

        self.RateOfParticipation = .04 
        self.RateOfCancerInUSA = .0542
        self.RateOfHIVInUSA = 0.0036
        self.RateOfAlzInUSA = 0.017

        

    
# All City Objects
SOUDERTON = City(
    "SOUDERTON",
    {   
        "SOUDERTON": 0.0,
        "NEWYORK": 88.1,
        "PHILADELPHIA": 34.7,
        "BOSTON": 309.0,
        "PITTSBURGH": 308.7,
        "TRENTON": 48.5, 
        "DOVER": 101.4,
        "RICHMOND": 268.4
    },
    0,
    {
        "CANCER" : 0,
        "HIV" : 0,
        "ALZHEIMERS": 0
    }
    )
NEWYORK = City(
    "NEWYORK",
    {   
        "SOUDERTON": 86.8,
        "NEWYORK": 0.0,
        "PHILADELPHIA": 97.2,
        "BOSTON": 216.5,
        "PITTSBURGH": 391.4,
        "TRENTON": 70.0,
        "DOVER": 171.6,
        "RICHMOND": 338.6
    },
    8468000,
    {
        "CANCER" : 0,
        "HIV" : 0,
        "ALZHEIMERS": 0
    }
)
NEWYORK.DiseasesPopulation = {
        "CANCER": int(NEWYORK.Population * NEWYORK.RateOfParticipation * NEWYORK.RateOfCancerInUSA),
        "HIV": int(NEWYORK.Population * NEWYORK.RateOfParticipation * NEWYORK.RateOfHIVInUSA),
        "ALZHEIMERS": int(NEWYORK.Population * NEWYORK.RateOfParticipation * NEWYORK.RateOfAlzInUSA)
    }
PHILADELPHIA = City(
    "PHILADELPHIA",
    {
        "SOUDERTON": 34.5,
        "NEWYORK": 93.8,
        "PHILADELPHIA": 0.0,
        "BOSTON": 307.1,
        "PITTSBURGH": 304.9,
        "TRENTON": 32.9,
        "DOVER": 81.8,
        "RICHMOND": 248.8
    },
    1576000,
    {
        "Cancer" : 0,
        "HIV" : 0,
        "ALZHEIMERS": 0
    }
)
PHILADELPHIA.DiseasesPopulation = {
        "CANCER": int(PHILADELPHIA.Population * PHILADELPHIA.RateOfParticipation * PHILADELPHIA.RateOfCancerInUSA),
        "HIV": int(PHILADELPHIA.Population * PHILADELPHIA.RateOfParticipation * PHILADELPHIA.RateOfHIVInUSA),
        "ALZHEIMERS": int(PHILADELPHIA.Population * PHILADELPHIA.RateOfParticipation * PHILADELPHIA.RateOfAlzInUSA)
    }
BOSTON = City(
    "BOSTON",
    {
        "SOUDERTON": 307.6,
        "NEWYORK": 215.0, 
        "PHILADELPHIA": 308.3, 
        "BOSTON": 0.0, 
        "PITTSBURGH": 571.6, 
        "TRENTON": 281.1, 
        "DOVER": 382.7, 
        "RICHMOND": 549.7
    },
    654776,
    {
        "CANCER" : 0,
        "HIV" : 0,
        "ALZHEIMERS": 0
    }
)
BOSTON.DiseasesPopulation = {
        "CANCER": int(BOSTON.Population * BOSTON.RateOfParticipation * BOSTON.RateOfCancerInUSA),
        "HIV": int(BOSTON.Population * BOSTON.RateOfParticipation * BOSTON.RateOfHIVInUSA),
        "ALZHEIMERS": int(BOSTON.Population * BOSTON.RateOfParticipation * BOSTON.RateOfAlzInUSA)
    }
PITTSBURGH = City(
    "PITTSBURGH",
    {
        "SOUDERTON": 309.0,
        "NEWYORK": 371.3, 
        "PHILADELPHIA": 304.2, 
        "BOSTON": 572.6, 
        "PITTSBURGH": 0.0, 
        "TRENTON": 324.5, 
        "DOVER": 328.3, 
        "RICHMOND": 336.7
    },
    300431,
    {
        "CANCER" : 0,
        "HIV" : 0,
        "ALZHEIMERS": 0
    }
)
PITTSBURGH.DiseasesPopulation = {
        "CANCER": int(PITTSBURGH.Population * PITTSBURGH.RateOfParticipation * PITTSBURGH.RateOfCancerInUSA),
        "HIV": int(PITTSBURGH.Population * PITTSBURGH.RateOfParticipation * PITTSBURGH.RateOfHIVInUSA),
        "ALZHEIMERS": int(PITTSBURGH.Population * PITTSBURGH.RateOfParticipation * PITTSBURGH.RateOfAlzInUSA)
    }
TRENTON = City(
    "TRENTON",
    {
        "SOUDERTON": 47.3,
        "NEWYORK": 66.1, 
        "PHILADELPHIA": 33.2, 
        "BOSTON": 279.2, 
        "PITTSBURGH": 324.1, 
        "TRENTON": 0.0, 
        "DOVER": 66.1,
        "RICHMOND": 278.4
    },
    90457,
    {
        "CANCER" : 0,
        "HIV" : 0,
        "ALZHEIMERS": 0
    }
)
TRENTON.DiseasesPopulation = {
        "CANCER": int(TRENTON.Population * TRENTON.RateOfParticipation * TRENTON.RateOfCancerInUSA),
        "HIV": int(TRENTON.Population * TRENTON.RateOfParticipation * TRENTON.RateOfHIVInUSA),
        "ALZHEIMERS": int(TRENTON.Population * TRENTON.RateOfParticipation * TRENTON.RateOfAlzInUSA)
    }
DOVER = City(
    "DOVER",
    {
        "SOUDERTON": 102.2,
        "NEWYORK": 168.4, 
        "PHILADELPHIA": 82.6 , 
        "BOSTON": 381.5, 
        "PITTSBURGH": 329.7, 
        "TRENTON": 111.9, 
        "DOVER": 0.0, 
        "RICHMOND": 204.2
    },
    38992,
    {
        "CANCER" : 0,
        "HIV" : 0,
        "ALZHEIMERS": 0
    }
    )
DOVER.DiseasesPopulation = {
    "CANCER": int(DOVER.Population * DOVER.RateOfParticipation * DOVER.RateOfCancerInUSA),
    "HIV": int(DOVER.Population * DOVER.RateOfParticipation * DOVER.RateOfHIVInUSA),
    "ALZHEIMERS": int(DOVER.Population * DOVER.RateOfParticipation * DOVER.RateOfAlzInUSA)
    }
RICHMOND = City(
    "RICHMOND",
    {
        "SOUDERTON": 266.7,
        "NEWYORK": 332.9, 
        "PHILADELPHIA": 247.2, 
        "BOSTON": 546.1, 
        "PITTSBURGH": 343.8, 
        "TRENTON": 280.3, 
        "DOVER": 195.3, 
        "RICHMOND": 0.0
    },
    226604,
    {
        "CANCER" : 0,
        "HIV" : 0,
        "ALZHEIMERS": 0
    }
    )
RICHMOND.DiseasesPopulation = {
        "CANCER": int(RICHMOND.Population * RICHMOND.RateOfParticipation * RICHMOND.RateOfCancerInUSA),
        "HIV": int(RICHMOND.Population * RICHMOND.RateOfParticipation * RICHMOND.RateOfHIVInUSA),
        "ALZHEIMERS": int(RICHMOND.Population * RICHMOND.RateOfParticipation * RICHMOND.RateOfAlzInUSA)
    }
