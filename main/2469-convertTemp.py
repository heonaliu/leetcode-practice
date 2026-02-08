class Solution:
    def convertTemperature(self, celsius: float) -> List[float]: #type: ignore
        fah = celsius *1.8 +32
        return [celsius+273.15, fah]