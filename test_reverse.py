import string
import random
import StringReverser

def test_output(capsys, monkeypatch):
    random_string = ''
    for _ in range(5):
        random_string += random.choice(string.ascii_letters)

    input = [random_string]
    random_string_backwards = random_string [::-1]
    
    monkeypatch.setattr('builtins.input', lambda _:input.pop())
    StringReverser.string_reverser()

    captured = capsys.readouterr()
    statements = captured.out.split("\n")

    assert statements[-2] == random_string_backwards[-1]
    assert statements[-3] == random_string_backwards[-2]
    assert statements[-4] == random_string_backwards[-3]
    assert statements[-5] == random_string_backwards[-4]
    assert statements[-6] == random_string_backwards[-5]
    
