class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        dici={}
        for i in range(len(paths)):
            i,j=paths[i]
            dici[i]=j
            for final_city in dici.values():
                if final_city not in dici:
                    destination=final_city
        return destination