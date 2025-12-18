from collections import defaultdict

AHO_NO_PASS = -(10**10)
class Aho:
    def __init__(self, words):
        self.max_states = sum([len(word) for word in words])
        self.out = [0]*(self.max_states+1)
        self.fail = [AHO_NO_PASS]*(self.max_states+1)
        self.goto = [[AHO_NO_PASS]*26 for _ in range(self.max_states+1)]
        for i in range(len(words)):
            words[i] = words[i].lower()
        self.words = words

        k = len(self.words)
        states = 1
        for i in range(k):
            word = self.words[i]
            current_state = 0
            for character in word:
                ch = ord(character) - ord('a')
                if self.goto[current_state][ch] == AHO_NO_PASS:
                    self.goto[current_state][ch] = states
                    states += 1
                current_state = self.goto[current_state][ch]
            self.out[current_state] |= (1<<i)
        for ch in range(26):
            if self.goto[0][ch] == AHO_NO_PASS:
                self.goto[0][ch] = 0

        queue = []
        for ch in range(26):
            if self.goto[0][ch] != 0:
                self.fail[self.goto[0][ch]] = 0
                queue.append(self.goto[0][ch])
        while queue:
            state = queue.pop(0)
            for ch in range(26):
                if self.goto[state][ch] != AHO_NO_PASS:
                    failure = self.fail[state]
                    while self.goto[failure][ch] == AHO_NO_PASS:
                        failure = self.fail[failure]
                    failure = self.goto[failure][ch]
                    self.fail[self.goto[state][ch]] = failure
                    self.out[self.goto[state][ch]] |= self.out[failure]
                    queue.append(self.goto[state][ch])

    def _go_next(self, current_state, next_input):
        answer = current_state
        ch = ord(next_input) - ord('a')
        while self.goto[answer][ch] == AHO_NO_PASS:
            answer = self.fail[answer]
        return self.goto[answer][ch]

    def search_words(self, text):
        text = text.lower()
        current_state = 0
        result = defaultdict(list)
        for i in range(len(text)):
            current_state = self._go_next(current_state, text[i])
            if self.out[current_state] == 0: continue
            for j in range(len(self.words)):
                if (self.out[current_state] & (1<<j)) > 0:
                    word = self.words[j]
                    result[word].append(i-len(word)+1)
        return result
