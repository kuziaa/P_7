def censor(forbidden, substitution):
    def decorator(fn):
        def decorated_fn():
            def change_text(text):
                for forbidden_frase in forbidden:
                    while text.find(forbidden_frase) != -1:
                        text = text.replace(forbidden_frase, substitution)
                return text

            list_of_strings = fn() if type(fn()) == list else [fn()]
            list_of_strings = map(change_text, list_of_strings)
            return list_of_strings
        return decorated_fn
    return decorator

@censor(forbidden=("ipsum", "quis"), substitution="[CENSORED]")
def text_producer():
    return [
        """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
    ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
    dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
    deserunt mollit anim id est laborum.""",
    "ipsum aaaaaaaaa quis",
    "ipsum bbbbbbbbb quis"
    ]

text_after_censor = text_producer()
for _ in text_after_censor:
    print(_)
