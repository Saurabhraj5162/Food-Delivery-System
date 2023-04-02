class FoodItemSearcher:
    def __init__(self) -> None:
        pass

    def search(self, foodItemName, filters):
        if not foodItemName or len(foodItemName) == 0 or not filters:
            raise Exception('Missing Params!')
        DataAccessorResults = DataAccessor.getFoodItemWithName(foodItemName)
        foodItems = DataAccessorParser(DataAccessorResults)

        for filter in filters:
            filteredFoodItems = []
            for item in foodItems:
                if filter.filter(item):
                    filteredFoodItems.append(item)

            foodItems = filteredFoodItems
        return foodItems
    
    def searchById(self, id):
        if not id:
            raise Exception('Missing Param')
        DataAccessorResults = DataAccessor.getFoodItemWithId(id)
        foodItems = DataAccessorParser(DataAccessorResults)

        return foodItems
