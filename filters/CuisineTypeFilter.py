
from data import MealType,FoodItem,CuisineType,Rating

class CuisineTypeFilter:
    def __init__(self, cuisineType) -> None:
        self.cuisineType = cuisineType

    def filterFood(self,foodItem):
        if foodItem.getCuisineType() in self.cuisineType: 
            return True
        return False
    
    def filterRestaurant(self,restaurant):
        if restaurant.getCuisineType() in self.cuisineType: 
            return True
        return False
    
    
        