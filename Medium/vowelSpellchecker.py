class Solution(object):
    def spellchecker(self, wordlist, queries):
        vowels = set('aeiou')
        def devowel(w):
            w = w.lower()
            return ''.join('*' if c in vowels else c for c in w)

        exact = set(wordlist)
        case_map = {}
        vowel_map = {}
        for w in wordlist:
            lw = w.lower()
            if lw not in case_map:
                case_map[lw] = w
            dv = devowel(w)
            if dv not in vowel_map:
                vowel_map[dv] = w

        ans = []
        for q in queries:
            if q in exact:
                ans.append(q)
            else:
                lq = q.lower()
                if lq in case_map:
                    ans.append(case_map[lq])
                else:
                    ans.append(vowel_map.get(devowel(q), ""))
        return ans
