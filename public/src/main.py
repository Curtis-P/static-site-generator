#./main.sh
from textnode import TextNode, TextType
# hello world
def main():
    exampleText = TextNode("example text to be used", TextType.bold, "https://google.com")
    print(repr(exampleText))
if __name__ == "__main__":
    main()
