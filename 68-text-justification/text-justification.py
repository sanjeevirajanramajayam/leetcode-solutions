class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        currentWords = []
        currentLength = 0
        currentSpaces = 0
        fin = []
        for word in words:
            if currentLength + currentSpaces + len(word) <= maxWidth:
                currentWords.append(word)
                currentLength += len(word)
                currentSpaces += 1
            else:
                # print(currentWords)
                # print(currentLength)
                # print(currentSpaces)
                # print(maxWidth, currentLength, currentSpaces)
                # print("spaces", maxWidth - currentLength)
                spaces = maxWidth - currentLength
                if len(currentWords) > 1:
                    div = spaces // (len(currentWords) - 1)
                    spacesArr = [div] * (len(currentWords) - 1)
                    remainder = spaces % (len(currentWords) - 1)
                    for i in range(len(spacesArr)):
                        if remainder == 0:
                            break
                        spacesArr[i] += 1
                        remainder -= 1
                    # print(spacesArr)
                else:
                    spacesArr = [spaces]

                
                ans = ""

                for i in range(len(currentWords)):
                    ans += currentWords[i]
                    if i != len(currentWords) - 1:
                        ans += " " * spacesArr[i]
                
                if len(currentWords) == 1:
                    ans += " " * spaces
                
                fin.append(ans)
                # print(ans)
                currentWords = [word]
                currentLength = len(word)
                currentSpaces = 1


        
        ans = ""

        for i in range(len(currentWords)):
            ans += currentWords[i]
            if i != len(currentWords) - 1:
                ans += " " 
        
        ans += " " * (maxWidth - len(ans))
        
        fin.append(ans)
        return fin