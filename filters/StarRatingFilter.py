
from data import MealType,FoodItem,CuisineType,Rating

class CuisineTypeFilter:
    def __init__(self, ) -> None:
        self.rating = Rating

    def filter(self,foodItem):

        return foodItem.getStarRating >= self.rating.Enum(foodItem.getStarRating)
    
    
        