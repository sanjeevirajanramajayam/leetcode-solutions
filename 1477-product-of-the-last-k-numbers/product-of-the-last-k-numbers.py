class ProductOfNumbers:

    def __init__(self):
        self.prodArray = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.prodArray = [1]
        else:
            self.prodArray.append(self.prodArray[-1] * num)

    def getProduct(self, k: int) -> int:
        # print(self.prodArray)
        if k >= len(self.prodArray):
            return 0
        return self.prodArray[-1] // self.prodArray[len(self.prodArray) - 1 - k]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)