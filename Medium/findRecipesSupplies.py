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