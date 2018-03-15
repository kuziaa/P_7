def censor(forbidden, substitution):
    def decorator(fn):
        def decorated_fn():
            text = fn()
            for forbidden_frase in forbidden:
                while text.find(forbidden_frase) != -1:
                    text = text.replace(forbidden_frase, substitution)
            return text
        return decorated_fn
    return decorator


@censor(forbidden=("ipsum", "quis"), substitution="[CENSORED]")
def text_producer():
    return """Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
    labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi
    ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum
    dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia
    deserunt mollit anim id est laborum."""

 

c = text_producer()
print(c)