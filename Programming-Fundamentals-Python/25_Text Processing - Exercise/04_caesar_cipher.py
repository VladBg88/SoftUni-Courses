received_text = input()
encrypted_text = [chr(ord(x) + 3) for x in received_text]
print( ''.join(encrypted_text))