import huffman as hf

with open("message.txt", "r") as reader:
    contents = list(reader.read())


print(contents)
huffman = hf.Huffman(contents)
huffman.huffing()
huffman.write_code()
letters = huffman.read_code()

with open("decoded.txt", "w") as writer:
    for value in letters:
        writer.write(value)
