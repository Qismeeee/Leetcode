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


def run_tests():
    s = Solution()
    cases = [
        (["KiTe","kite","hare","Hare"],
         ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"],
         ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]),
        (["yellow"], ["YellOw"], ["yellow"]),
        (["YellOw"], ["yollow","yeellow","yllw"], ["YellOw","",""]),
        (["ABC","abc"], ["Abc","aBc","abd"], ["ABC","ABC",""]),
    ]
    for wordlist, queries, expected in cases:
        out = s.spellchecker(wordlist, queries)
        assert out == expected, f"expected {expected}, got {out}"
        print(out)

run_tests()
