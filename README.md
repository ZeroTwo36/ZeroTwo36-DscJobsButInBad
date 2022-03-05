## DuckJobs - The worst ever API Wrapper

***DSCJobsAPIResponse***  
**~.User**  
|-userID: int,  
|-banned: bool,  
|-staff: bool,  
|-premium: bool,  
|-lifetime: bool,  
|-duration: int    
**~.Review**  
|-id: str,  
|-userID: str,  
|-content: str,  
|-likes: int,  
|-dislikes: int,  
|-reports: int,  
|-replies: int,  
|-rate: int,  
|-date: int,  

***Functions***  
  
~.getUserByID(userID)  
~.getReviewByID(userID)  
