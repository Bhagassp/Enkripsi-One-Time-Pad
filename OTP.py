def one_time_pad_encrypt(plaintext, key):
    if len(plaintext) != len(key):
        raise ValueError("Panjang plainteks dan kunci harus sama")

    encrypted_text = ""
    for i in range(len(plaintext)):
        # XOR antara karakter plainteks dan kunci
        encrypted_char = chr(ord(plaintext[i]) ^ ord(key[i]))
        encrypted_text += encrypted_char

    return encrypted_text

def one_time_pad_decrypt(ciphertext, key):
    if len(ciphertext) != len(key):
        raise ValueError("Panjang cipherteks dan kunci harus sama")

    decrypted_text = ""
    for i in range(len(ciphertext)):
        # XOR antara karakter cipherteks dan kunci
        decrypted_char = chr(ord(ciphertext[i]) ^ ord(key[i]))
        decrypted_text += decrypted_char

    return decrypted_text

def main():
    # Input plainteks dan kunci
    plaintext = input("Masukkan plainteks : ")
    key = input("Masukkan kunci : ")

    try:
        # Enkripsi dengan One-Time Pad
        ciphertext = one_time_pad_encrypt(plaintext, key)
        print("Teks Terenkripsi:", ciphertext)

        # Dekripsi dengan One-Time Pad
        decrypted_text = one_time_pad_decrypt(ciphertext, key)
        print("Teks Terdekripsi:", decrypted_text)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
