
from filters import CuisineTypeFilter, MealTypeFilter, StarRatingFilter
from searchers import RestaurantSearcher

class RestaurantSearcherAPI:
    def searchRestaurants(self, restaurantName, mealType, cuisineType, starRating):
        filters = []

        if mealType:
            filters.append(MealTypeFilter(mealType))
        if cuisineType:
            filters.append(CuisineTypeFilter(cuisineType))
        if starRating:
            filters.append(StarRatingFilter(starRating))

        restaurantSearcher = RestaurantSearcher()
        return restaurantSearcher.search(restaurantName, filters)

        
    