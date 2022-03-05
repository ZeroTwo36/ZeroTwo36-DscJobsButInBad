import requests

class DSCJobsAPIResponse(object): 
    def __init__(self, **kwargs):
        
        for k in list(kwargs.keys()):
            self.__setattr__(k,kwargs.get(k))

def getUserByID(userID):
    r = requests.get(f"https://api.dscjobs.org/user/{userID}")
    r.raise_for_status()
    return DSCJobsAPIResponse(**r.json())
    
def getReviewByID(userID):
    r = requests.get(f"https://api.dscjobs.org/rev/{userID}")
    r.raise_for_status()
    return DSCJobsAPIResponse(**r.json())