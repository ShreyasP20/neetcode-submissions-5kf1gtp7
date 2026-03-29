class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False

        validparentheses = list()
        for i in s:
            if i == "(" or i == "{" or i == "[":
                validparentheses.append(i)
            elif i == ")":
                if len(validparentheses) > 0:
                    if validparentheses.pop() != "(":
                        return False
                else:
                    return False

            elif i == "}":
                if len(validparentheses) > 0:
                    if validparentheses.pop() != "{":
                        return False
                else:
                    return False

            elif i == "]":
                if len(validparentheses) > 0:
                    if validparentheses.pop() != "[":
                        return False
                else:
                    return False
                    

        if len(validparentheses)!=0:
            return False


        return True
             
            