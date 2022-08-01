import string


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        letters = list(string.ascii_lowercase)
        letter_dict = {}
        for letter in letters:
            letter_dict[letter] = letter

        def union(x, y):
            x = find(x)
            y = find(y)

            letter_dict[y] = x

        def find(x):
            if letter_dict[x] == x:
                return x
            else:
                return find(letter_dict[x])

        not_equals = []
        for eq in equations:
            if eq[1] == "=":
                union(eq[0], eq[3])
            else:
                not_equals.append(eq)

        for eq in not_equals:
            if find(eq[0]) == find(eq[3]):
                return False

        return True
