with open("secret.hex") as f:
    ciphertext = f.read()

    k1 = chr(ord(ciphertext[0:1]) ^ ord("H"))
    k2 = chr(ord(ciphertext[1:2]) ^ ord("g"))
    keystream = (k1 + k2) * (len(ciphertext) / 2)

    plaintext = "".join(
            [chr(ord(k) ^ ord(c)) for k, c in zip(keystream, ciphertext)]
    )

    print plaintext
