from typing import NoReturn


class Sentences:
    def __init__(self) -> None:
        self.sentences = []

    def add_sentence(self, sentence: str) -> None:
        self.sentences.append(sentence)

    def convert_sentence(self, index: int) -> None:
        if index == 0:
            self.sentences[index] = self.sentences[index].capitalize()
        elif index == 1:
            self.sentences[index] = self.sentences[index].title()
        else:
            pass


def get_user_input(sentence_container: Sentences) -> None:
    num_sentences = 2
    for _ in range(num_sentences):
        sentence = input()
        sentence_container.add_sentence(sentence)


def main() -> NoReturn:
    sentences = Sentences()
    get_user_input(sentences)
    sentences.convert_sentence(0)
    sentences.convert_sentence(1)

    for sentence in sentences.sentences:
        print(sentence)


if __name__ == '__main__':
    main()
