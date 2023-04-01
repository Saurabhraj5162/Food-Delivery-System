from filters import CuisineTypeFilter, MealTypeFilter, StarRatingFilter
from searchers import FoodItemSearcher

class FoodItemSearcherAPI:
    def searchFoodItems(self, foodItemName, mealType, cuisinsType, rating):
        filters = []
        if mealType:
            filters.append(MealTypeFilter(mealType))

        if cuisinsType:
            filters.append(CuisineTypeFilter(cuisinsType))
        if rating:
            filters.append(StarRatingFilter(rating))

        foodItemSearcher = FoodItemSearcher()
        return foodItemSearcher.search(foodItemName, filters)


    