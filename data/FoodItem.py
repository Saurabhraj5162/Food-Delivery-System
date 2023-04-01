class FoodItem:
    def __init__(self,id, name, description, price, mealType, cuisineType, starRating, restaurantID, isAvailable ) -> None:
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.cuisineType = cuisineType
        self.mealType = mealType
        self.starRating = starRating
        self.restaurantID = restaurantID
        self.isAvailable = isAvailable

    def getId(self,):
        return self.id
    
    def getName(self,):
        return self.name
    
    def getDescription(self,):
        return self.description
    
    def getPrice(self,):
        return self.price
    
    def getCuisineType(self,):
        return self.cuisineType
    
    def getMealType(self,):
        return self.mealType
    
    def getStarRating(self,):
        return self.starRating
    
    def getRestaurant(self,):
        return self.restaurantID
    
    def getIsVailable(self,):
        return self.isAvailable
    




