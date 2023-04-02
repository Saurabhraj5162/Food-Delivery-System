
from data import MealType,FoodItem,CuisineType,Rating

class MealTypeFilter:
    def __init__(self, mealType) -> None:
        self.mealType = mealType

    def filterFood(self,foodItem):
        return foodItem.getMealType == self.mealType
    
    def filterRestaurant(self,restaurant):
        return restaurant.getMealType == self.mealType
    
        

