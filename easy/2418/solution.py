class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        aux = 0

        for i in range(len(heights)):
            taller = heights[aux]
            index = -1

            for j in range(aux, len(heights), 1):
                if heights[j] > taller:
                    taller = heights[j]
                    index = j

            if index != -1:
                name = names[aux]
                names[aux] = names[index]
                names[index] = name

                height = heights[aux]
                heights[aux] = heights[index]
                heights[index] = height

            aux += 1

        return names
