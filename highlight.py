from pygments import highlight
from pygments.formatters import ImageFormatter
from pygments.lexers import RacketLexer
from pygments.style import Style
from pygments.token import (
    Comment,
    Error,
    Generic,
    Keyword,
    # Literal,
    Name,
    Number,
    Operator,
    Punctuation,
    String,
    Whitespace,
)


class DrRacketStyle(Style):
    default_style = ""
    styles = {
        Punctuation: "bold #843c24",
        Whitespace: "#bbbbbb",
        Comment: "bold #c27452",
        Comment.Preproc: "noitalic #c27452",
        Comment.Special: "bold #c27452",
        Keyword: "bold #262680",
        Keyword.Declaration: "#843c24",
        Keyword.Pseudo: "nobold",
        Keyword.Type: "nobold #262680",
        Keyword.Namespace: "#000000",
        Operator: "#666666",
        Operator.Word: "bold #AA22FF",
        Name: "bold #262680",
        Name.Builtin: "#262680",
        Name.Function: "#262680",
        Name.Class: "bold #262680",
        Name.Namespace: "#000000",
        Name.Exception: "bold #D2413A",
        Name.Variable: "#262680",
        Name.Constant: "#262680",
        Name.Label: "#262680",
        Name.Entity: "bold #999999",
        Name.Attribute: "#7D9029",
        Name.Tag: "bold #008000",
        Name.Decorator: "#AA22FF",
        String: "bold #298026",
        String.Doc: "italic",
        String.Interpol: "bold #B00040",
        String.Escape: "bold #B00040",
        String.Regex: "#A0A000",
        String.Symbol: "#19177C",
        String.Other: "#008000",
        Number: "bold #298026",
        Generic.Heading: "bold #000080",
        Generic.Subheading: "bold #800080",
        Generic.Deleted: "#A00000",
        Generic.Inserted: "#00A000",
        Generic.Error: "#E40000",
        Generic.Emph: "italic",
        Generic.Strong: "bold",
        Generic.Prompt: "bold #000080",
        Generic.Output: "#888888",
        Generic.Traceback: "#04D",
        Error: "border:#FF0000",
    }


# Racket source code
racket_code = """
> 1
1

(define (factorial n)
    (if (zero? n)
        1
        (* n (factorial (- n 1)))))
"""

# Use Pygments to highlight the code
lexer = RacketLexer()
tokens = lexer.get_tokens(racket_code)

for t in tokens:
    print(t)

formatter = ImageFormatter(
    style=DrRacketStyle, font_name="Courier New", font_size=28, line_numbers=False
)
image_data = highlight(racket_code, lexer, formatter)

# Save the image data to a file
with open("racket_code.png", "wb") as f:
    f.write(image_data)
