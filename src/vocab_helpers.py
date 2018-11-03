strong_affirmatives = ["yes", "yeah", "always", "all", "any", "every", "everybody", "everywhere", "ever"]

strong_negations = ["no", "not", "never", "none" "n't", "nothing", "neither", "nobody", "nowhere"]

punctuation = ["?", "!", "..."]

interjections = ["oh", "hey", "wow", "aha", "aham", "aw", "bam", "blah", "bingo", "boo", "bravo",
                 "cheers", "congratulations", "congrats", "duh", "eh", "gee", "gosh", "hey", "hmm",
                 "huh", "hurray", "oh", "oh dear", "oh my", "oh well", "oops", "ouch", "ow", "phew",
                 "shh", "uh", "uh-huh", "mhm", "ugh", "well", "wow", "woah", "yeah", "yep", "yikes", "yo"]

intensifiers = ["amazingly", "astoundingly", "awful", "bare", "bloody", "crazy", "dreadfully",
                "colossally", "especially", "exceptionally", "excessively", "extremely",
                "extraordinarily", "fantastically", "frightfully", "fucking", "fully", "hella",
                "holy", "incredibly", "insanely", "literally", "mightily", "moderately", "most",
                "outrageously", "phenomenally", "precious", "quite", "radically", "rather",
                "really", "remarkably", "right", "sick", "strikingly", "super", "supremely",
                "surprisingly", "terribly", "terrifically", "too", "totally", "uncommonly",
                "unusually", "veritable", "very", "wicked"]

# Based on wikipedia
contractions = {
    "ain't": "is not",
    "aren't": "are not",
    "can't": "cannot",
    "ve": "have",
    "cause": "because",
    "could've": "could have",
    "couldn't": "could not",
    "couldn't've": "could not have",
    "didn't": "did not",
    "doesn't": "does not",
    "don't": "do not",
    "hadn't": "had not",
    "hadn't've": "had not have",
    "hasn't": "has not",
    "haven't": "have not",
    "ll": "will",
    "n": "and",
    "s": "is",  # or has
    "d": "would",   # or had
    "m": "am",
    "isn't": "is not",
    "it'd": "it would",
    "it'd've": "it would have",
    "let's": "let us",
    "all's": "all",
    "ma'am": "madam",
    "b'day": "birthday",
    "might've": "might have",
    "must've": "must have",
    "mustn't": "must not",
    "mustn't've": "must not have",
    "needn't": "need not",
    "needn't've": "need not have",
    "o'clock": "of the clock",
    "oughtn't": "ought not",
    "oughtn't've": "ought not have",
    "she'll": "she will",
    "she'd": "she would",
    "he'd": "he would",
    "i'd": "I would",
    "i'm": "I am",
    "shan't": "shall not",
    "sha'n't": "shall not",
    "shan't've": "shall not have",
    "should've": "should have",
    "shouldn't": "should not",
    "shouldn't've": "should not have",
    "that'd": "that would",     # or that had
    "that's": "that is",
    "there'd": "there would",   # or there had
    "there'd've": "there would have",
    "there's": "there is",
    "to've": "to have",
    "wasn't": "was not",
    "re": "are",
    "weren't": "were not",
    "what'll": " what will",
    "what'll've": "what will have",
    "what're": "what are",
    "they're": "they are",
    "what's": "what is",
    "what've": "what have",
    "when's": "when is",
    "when've": "when have",
    "where'd": "where did",
    "where's": "where is",
    "where've": "where have",
    "who'll": " who will",
    "who'll've": "who will have",
    "who's": "who is",
    "who've": "who have",
    "why's": "why is",
    "why've": "why have",
    "will've": "will have",
    "won't": "will not",
    "won't've": "will not have",
    "would've": "would have",
    "wouldn't": "would not",
    "wouldn't've": "would not have",
    "y'all": "you all",
    "y'll": "you all",
    "ya'll": "you all",
    "y'all'd": "you all would",
    "y'all'd've": "you all would have",
    "y'all're": "you all are",
    "y'all've": "you all have",
    "c'mon": "come on",
    "ma": "am going to"
}

slang = {
    "4ward": "forward",
    "brb": "be right back",
    "b4": "before",
    "bfn": "bye for now",
    "bgd": "background",
    "btw": "by the way",
    "br": "best regards",
    "clk": "click",
    "da": "the",
    "deet": "detail",
    "deets": "details",
    "dm": "direct message",
    "f2f": "face to face",
    "ftl": " for the loss",
    "ftw": "for the win",
    "kk" : "cool cool",
    "kewl": "cool",
    "rt": "retweet",
    "smh": "so much hate",
    "yaass": "yes",
    "a$$":"ass",
    "bby": "baby",
    "bc": "because",
    "coz": "because",
    "cuz": "because",
    "cause": "because",
    "cmon": "come on",
    "cmonn": "come on",
    "dafuq": "what the fuck",
    "dafuk": "what the fuck",
    "dis": "this",
    "diss": "this",
    "ma": "my",
    "dono": "do not know",
    "donno": "do not know",
    "dunno": "do not know",
    "fb": "facebook",
    "couldnt": "could not",
    "n": "and",
    "gtg": "got to go",
    "yep": "yes",
    "yw": "you are welcome",
    "im": "i am",
    "youre":"you are",
    "hes": "he is",
    "shes": "she is",
    "theyre": "they are",
    "af": "as fuck",
    "fam": "family",
    "fwd": "forward",
    "ffs": "for fuck sake",
    "fml": "fuck my life",
    "lol": "laugh out loud",
    "lel": "laugh out loud",
    "lool": "laugh out loud",
    "lmao": "laugh my ass off",
    "lmaoo": "laugh my ass off",
    "omg":"oh my god",
    "oomg":"oh my god",
    "omgg":"oh my god",
    "omfg": "oh my fucking god",
    "stfu": "shut the fuck up",
    "awsome":"awesome",
    "imo": "in my opinion",
    "imho": "in my humble opinion",
    "ily": "i love you",
    "ilyy": "i love you",
    "ikr": "i know right",
    "ikrr": "i know right",
    "idk": "i do not know",
    "jk": "joking",
    "lmk": "let me know",
    "nsfw": "not safe for work",
    "hehe": "haha",
    "tmrw": "tomorrow",
    "yt": "youtube",
    "hahaha": "haha",
    "hihi": "haha",
    "pls": "please",
    "ppl": "people",
    "wtf": "what the fuck",
    "wth": "what teh hell",
    "obv": "obviously",
    "nomore": "no more",
    "u": "you",
    "ur": "your",
    "wanna": "want to",
    "luv": "love",
    "imma": "i am",
    "&": "and",
    "thanx": "thanks",
    "til": "until",
    "till": "until",
    "thx": "thanks",
    "pic": "picture",
    "pics": "pictures",
    "gp": "doctor",
    "xmas": "christmas",
    "rlly": "really",
    "boi": "boy",
    "boii": "boy",
    "rly": "really",
    "whch": "which",
    "awee": "awe", # or maybe awesome is better
    "sux" : "sucks",
    "nd": "and",
    "fav": "favourite",
    "frnds": "friends",
    "info": "information",
    "loml": "love of my life",
    "bffl": "best friend for life",
    "gg": "goog game",
    "xx": "love",
    "xoxo": "love",
    "thats": "that is",
    "homie": "best friend",
    "homies": "best friends"
}

implicit_emoticons = {
    ":)": "smiling face with open mouth",
    "=)": "smiling face with open mouth",
    ":-)": "smiling face with open mouth",
    ";-)": "winking face",
    "(:": "smiling face with open mouth",
    "(-:": "smiling face with open mouth",
    "(':": "smiling face with open mouth",
    "='d": "happy face",
    ":d": "grinning face",
    ";d": "grinning face",
    "xd": "grinning face",
    "dx": "grinning face",
    ":))": "face with tears of joy",
    ":-))": "face with tears of joy",
    "=))": "face with tears of joy",
    ";)": "winking face",
    ":x": "smiling face with open mouth with heart-shaped eyes",
    "p": "face with stuck-out tongue",
    ":p": "face with stuck-out tongue",
    ";p": "face with stuck-out tongue",
    ":-p": "face with stuck-out tongue",
    ":(": "disappointed face",
    ":-(": "disappointed face",
    ";(": "disappointed face",
    ";;": "confused face",
    "::": "confused face",
    ":'(": "crying face",
    ":((": "crying face",
    ":/": "sarcastic dace",
    ":|": "neutral face",
    ":3": "cute face",
    "x": "love",
    "xx": "love",
    "xoxo": "hugs and kisses",
    "xo": "hugs and kisses",
    ":o": "face with open mouth",
    ":-o": "face with open mouth",
    "\m/": "metal music"
}

# Processed from https://en.wikipedia.org/wiki/List_of_emoticons
wikipedia_emoticons = {
    ':-)': 'smiling face with open mouth',
    '8-)': 'smiling face with open mouth',
    ':]': 'smiling face with open mouth',
    ':)': 'smiling face with open mouth',
    ':-3': 'smiling face with open mouth',
    ':->': 'smiling face with open mouth',
    ':-}': 'smiling face with open mouth',
    '(-:': 'smiling face with open mouth',
    "(:": "smiling face with open mouth",
    ':-]': 'smiling face with open mouth',
    '=]': 'smiling face with open mouth',
    '=)': 'smiling face with open mouth',
    ':3': 'smiling face with open mouth',
    ':c)': 'smiling face with open mouth',
    ':^)': 'smiling face with open mouth',
    ':}': 'smiling face with open mouth',
    ':>': 'smiling face with open mouth',
    '8)': 'smiling face with open mouth',
    '=d': 'grinning face',
    ":d": "grinning face",
    'xd': 'grinning face',
    '8-d': 'grinning face',
    '8d': 'grinning face',
    ':-d': 'grinning face',
    '=3': 'grinning face',
    'x-d': 'grinning face',
    ':-))': 'face with tears of joy',
    ':))': 'face with tears of joy',
    '))': 'face with tears of joy',
    ']]': 'face with tears of joy',
    '=))': 'face with tears of joy',
    ':<': 'disappointed face',
    ':(': 'disappointed face',
    ':@': 'disappointed face',
    ':-<': 'disappointed face',
    '>:[': 'disappointed face',
    ':[': 'disappointed face',
    ':{': 'disappointed face',
    ':c': 'disappointed face',
    '>:(': 'disappointed face',
    ':-c': 'disappointed face',
    ':-(': 'disappointed face',
    ':-||': 'disappointed face',
    ':-[': 'disappointed face',
    ":-(": "disappointed face",
    ";(": "disappointed face",
    ";;": "confused face",
    "::": "confused face",
    ":'-(": 'crying face',
    ":'(": 'crying face',
    ":'((": 'crying face',
    ":((": 'crying face',
    "((": 'crying face',
    ":'-)": 'face with tears of joy',
    ":')": 'face with tears of joy',
    'd=': 'anguished face',
    'd:<': 'anguished face',
    'd8': 'anguished face',
    'd;': 'anguished face',
    'dx': 'anguished face',
    "d-':": 'anguished face',
    ':-o': 'astonished face',
    ':o)': 'astonished face',
    '8-0': 'astonished face',
    ':-O': 'astonished face',
    ':O': 'astonished face',
    ':-0': 'astonished face',
    ':o': 'astonished face',
    '>:o': 'astonished face',
    ':x': 'kissing face',
    ':*': 'kissing face',
    ':-*': 'kissing face',
    'xx': 'black heart suit',
    'x': 'black heart suit',
    'xoxo': 'kiss mark',
    'xo': 'kiss mark',
    ':-,': 'winking face',
    ';^)': 'winking face',
    ';d': 'winking face',
    ';-]': 'winking face',
    ';]': 'winking face',
    '*)': 'winking face',
    ';-)': 'winking face',
    '*-)': 'winking face',
    ';)': 'winking face',
    'x-p': 'face with stuck-out tongue',
    '=p': 'face with stuck-out tongue',
    'd:': 'face with stuck-out tongue',
    ':p': 'face with stuck-out tongue',
    ':b': 'face with stuck-out tongue',
    ':-b': 'face with stuck-out tongue',
    ':-p': 'face with stuck-out tongue',
    ';p': 'face with stuck-out tongue',
    ':P': 'face with stuck-out tongue',
    '>:p': 'face with stuck-out tongue',
    'xp': 'face with stuck-out tongue',
    '>:/': 'confused face',
    ':L': 'confused face',
    '=\\': 'confused face',
    ':S': 'confused face',
    ':-.': 'confused face',
    '=/': 'confused face',
    '>:\\': 'confused face',
    ':-/': 'confused face',
    ':\\': 'confused face',
    '=l': 'confused face',
    ':/': 'confused face',
    ':|': 'neutral face',
    ':-|': 'neutral face',
    ':$': 'flushed face',
    '0;^)': 'smiling face with open mouth',
    'O:-)': 'smiling face with open mouth',
    '0:3': 'smiling face with open mouth',
    '0:-)': 'smiling face with open mouth',
    '0:)': 'smiling face with open mouth',
    '0:-3': 'smiling face with open mouth',
    'O:)': 'smiling face with open mouth',
    "\m/": "multiple musical notes"
}

emotiocons_to_emojis = {
    ':{': '😞', ':c)': '😃', ':-||': '😞', ':(': '😞', ':-))': '😂', 'dx': '😧',
    ':-d': '😀', '))': '😂', ':-*': '😗', ':d': '😀', ":'((": '😢', ':‑Þ': '😛',
    ':-[': '😞', ':-<': '😞', ":'-)": '😂', ":'-(": '😢', ':þ': '😛', ':‑,': '😉',
    '=]': '😃', '>:[': '😞', ':Þ': '😛', ':‑|': '😐', 'd8': '😧', 'O:‑)': '😃',
    ';)': '😉', ':‑b': '😛', ":')": '😂', '>:(': '😞', '8-0': '😲', ';-)': '😃',
    ':o)': '😲', ':‑þ': '😛', ':o': '😲', ':-)': '😃', ':-o': '😲', '(-:': '😃',
    ';d': '😉', ':))': '😂', ':x': '😗', ';^)': '😉', '(:': '😃', ':$': '😳', 'd;': '😧',
    'd:<': '😧', ':O': '😲', ':-c': '😞', 'xoxo': '💋', ':‑p': '😛', '8)': '😃',
    '0:)': '😃', '0;^)': '😃', ':@': '😞', 'xx': '♥', ':-}': '😃', '::': '😕', ';‑)': '😉',
    'x': '♥', ':-]': '😃', ':*': '😗', ':-(': '😞', ']]': '😂', '\\m/': '🎶', '*)': '😉',
    ':}': '😃', ':)': '😃', '=/': '😕', ';;': '😕', '>:o': '😲', '=d': '😀', ':L': '😕',
    ':((': '😢', '=3': '😀', '0:‑)': '😃', ':-O': '😲', ':<': '😞', 'd=': '😧', '0:3': '😃',
    ';]': '😉', ';p': '😛', ':P': '😛', 'x‑p': '😛', '=)': '😃', 'O:)': '😃', ':p': '😛',
    'x-d': '😀', '8-)': '😃', ':S': '😕', "d-':": '😧', ':c': '😞', ':|': '😐', '0:‑3': '😃',
    '>:p': '😛', '>:\\': '😕', ':/': '😕', ':]': '😃', ':3': '😃', ':b': '😛', ';‑]': '😉',
    '8d': '😀', 'xo': '💋', '>:/': '😕', '((': '😢', ':[': '😞', ':‑/': '😕', ':->': '😃',
    ';(': '😞', '=))': '😂', '=\\': '😕', ":'(": '😢', '*-)': '😉', ':\\': '😕', 'xd': '😀',
    'xp': '😛', ':-3': '😃', '=l': '😕', ':^)': '😃', '=p': '😛', ':>': '😃', '8-d': '😀',
    ':-0': '😲', 'd:': '😛', ':‑.': '😕'
}
