def process_string(user_input: str) -> None:
    words = user_input.split(" ")
    word_count = str(len(words))
    words_reversed = " ".join(words[::-1])
    print(f"{word_count}\n{words_reversed}")


process_string(input())
