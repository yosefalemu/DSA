class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        population_changes = {}
        for birth, death in logs:
            if birth in population_changes:
                population_changes[birth] += 1
            else:
                population_changes[birth] = 1
            if death in population_changes:
                population_changes[death] -= 1
            else:
                population_changes[death] = -1
        max_population = 0
        current_population = 0
        min_year = float("inf")
        for year in sorted(population_changes):
            current_population += population_changes[year]
            if current_population > max_population:
                max_population = current_population
                min_year = year
        return min_year
                
                
        
        