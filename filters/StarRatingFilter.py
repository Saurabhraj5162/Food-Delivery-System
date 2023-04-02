
from data import MealType,FoodItem,CuisineType,Rating

class StarRatingFilter:
    def __init__(self,rating ) -> None:
        self.rating = rating

    def filterFood(self,foodItem):
        return foodItem.getStarRating >= self.rating.Enum(foodItem.getStarRating)
    
    def filterRestaurant(self,restaurant):
        return restaurant.getStarRating >= self.rating.Enum(restaurant.getStarRating)
    
    
        