class Restaurant:
    def __init__(self, id, name, description, businessHour, mealType, cuisineType, rating, menu) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.businessHour = businessHour
        self.mealType = mealType
        self.cuisineType = cuisineType
        self.rating =rating
        self.menu = menu

    def getId(self,):
        return self.id
    
    def getName(self):
        return self.name
    
    def getDescription(self):
        return self.description
    
    def getBusinessHours(self):
        return self.businessHour
    
    def getMealType(self,):
        return self.mealType
    def getCuisineType(self):
        return self.cuisineType
    
    def getRating(self,):
        return self.rating
    
    def getMenu(self):
        return self.menu
