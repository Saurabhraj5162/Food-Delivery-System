class RestaurantSearcher:
    def __init__(self,) -> None:
        pass

    def search(self, restaurantName, filters):
        if not restaurantName or len(restaurantName) == 0 or not filters:
            raise Exception('Missing Params!')
        DataAccessorResults = DataAccessor.getRestaurantWithName(restaurantName)
        restaurants = DataAccessorParser(DataAccessorResults)

        for filter in filters:
            filteredRestaurants = []
            for rest in restaurants:
                if filter.filter(rest):
                    filteredRestaurants.append(rest)

            restaurants = filteredRestaurants
        return restaurants