from collections import deque, defaultdict

class Solution(object):
    def findAllRecipes(self, recipes, ingredients, supplies):
        recipes_set = set(recipes)
        supplies_set = set(supplies)
        
        graph = defaultdict(list)
        in_degree = {}
        
        for i, recipe in enumerate(recipes):
            recipe_ings = [ing for ing in ingredients[i] if ing in recipes_set]
            basic_ings = [ing for ing in ingredients[i] if ing not in recipes_set]
            if all(ing in supplies_set for ing in basic_ings):
                in_degree[recipe] = len(recipe_ings)
                for ing in recipe_ings:
                    graph[ing].append(recipe)
            else:
                in_degree[recipe] = -1  
        queue = deque([r for r in recipes if in_degree.get(r, -1) == 0])
        result = []
        
        while queue:
            curr = queue.popleft()
            result.append(curr)
            for next_recipe in graph.get(curr, []):
                if in_degree[next_recipe] > 0:
                    in_degree[next_recipe] -= 1
                    if in_degree[next_recipe] == 0:
                        queue.append(next_recipe)
        
        return result
    
def run_test_case(test_num, recipes, ingredients, supplies, expected):
    solution = Solution()
    result = solution.findAllRecipes(recipes, ingredients, supplies)
    print(f"Test case {test_num}:")
    print(f"Recipes: {recipes}")
    print(f"Ingredients: {ingredients}")
    print(f"Supplies: {supplies}")
    print(f"Expected: {expected}")
    print(f"Output: {result}")
    print(f"Pass: {sorted(result) == sorted(expected)}\n")  

# Test case 1: Test cơ bản từ bài toán
run_test_case(
    1,
    recipes=["bread", "sandwich"],
    ingredients=[["yeast", "flour"], ["bread", "meat"]],
    supplies=["yeast", "flour", "meat"],
    expected=["bread", "sandwich"]
)

# Test case 2: Chỉ có nguyên liệu cơ bản, không phụ thuộc
run_test_case(
    2,
    recipes=["juice"],
    ingredients=[["orange"]],
    supplies=["orange"],
    expected=["juice"]
)

# Test case 3: Không thể làm công thức do thiếu nguyên liệu
run_test_case(
    3,
    recipes=["cake"],
    ingredients=[["flour", "sugar"]],
    supplies=["flour"],
    expected=[]
)

# Test case 4: Nhiều công thức không phụ thuộc lẫn nhau
run_test_case(
    4,
    recipes=["tea", "coffee"],
    ingredients=[["tea_leaves", "water"], ["coffee_beans", "water"]],
    supplies=["tea_leaves", "water", "coffee_beans"],
    expected=["tea", "coffee"]
)

# Test case 5: Chuỗi phụ thuộc dài hơn
run_test_case(
    5,
    recipes=["dough", "bread", "sandwich"],
    ingredients=[["flour", "water"], ["dough", "yeast"], ["bread", "meat"]],
    supplies=["flour", "water", "yeast", "meat"],
    expected=["dough", "bread", "sandwich"]
)