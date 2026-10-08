
#Given a string s, return a new string in which characters at even indices are lowercase and characters at odd indices are uppercase. The relative order of characters must remain unchanged.

#Note: Indices are 0-indexed (i.e. index 0 is even, index 1 is odd, index 2 is even, etc.).

#Example 1:
#Input: s = "abcdefghijkm"
#Output: "aBcDeFgHiJkM"
#Example 2:
#Input: s = "hello"
#Output: "hElLo"
#Example 3:
#Input: s = "WORLD"
#Output: "wOrLd"
#Example 4:
#nput: s = "a"
#Output: "a"
#Constraints:
# &lt;= s.length &lt;= 10^5
#s consists of English letters.
#Examples
#Example 1:
#Input: {"s": "abcdefghijkm"}
#Output: "aBcDeFgHiJkM"
#Explanation: Sample testcase example
def alternatingCase(s: str) -> str:
    res = []
    
    # Iterate through each character in the string along with its 0-based index
    for i, char in enumerate(s):
        # Check if the index is even (0, 2, 4, ...)
        if i % 2 == 0:
            # Convert characters at even indices to lowercase
            res.append(char.lower())
        else:
            # Convert characters at odd indices (1, 3, 5, ...) to uppercase
            res.append(char.upper())
            
    # Join the list of transformed characters back into a single string
    return "".join(res)