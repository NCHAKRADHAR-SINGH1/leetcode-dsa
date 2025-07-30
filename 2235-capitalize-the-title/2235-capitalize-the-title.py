class Solution:
    def capitalizeTitle(self, title: str) -> str:
        li=title.lower().split()
        for i in range(len(li)):
            if len(li[i]) >= 3:
               word=li[i]
               right_word=word.capitalize()
               li[i]=right_word

        return ' '.join(li)