from fastapi import FastAPI, Request

import symmetric
import asymmetric

app = FastAPI()

# Keys
symmetric_key = "2-YmNMytBHoCCjIqboJGg2_4XKM27xelu1SBI3Y29nw="
asymmetric_keys = None

# Symetryczne
@app.get("/symmetric/key")
def get_symmetric_key():
    return symmetric.get_key()

@app.post("/symmetric/key")
def set_symmetric_key(key: str):
    global symmetric_key
    if len(key) == 32:
        symmetric_key = key

    if symmetric_key == key:
        return True

    return ValueError("Setting new symetric key failed! Try again!")

@app.post("/symmetric/encode")
def symmetric_encode(text: str):
    if symmetric_key is None:
        return ValueError("Symmetric key connot be None! Set key with POST /symmetric/key!")

    return symmetric.encode_text(symmetric_key=symmetric_key, text=text)

@app.post("/symmetric/decode")
def symmetric_decode(token: str):
    if symmetric_key is None:
        return ValueError("Symmetric key connot be None! Set key with POST /symmetric/key!")

    return symmetric.decode_text(symmetric_key=symmetric_key, token=token)


# Asymetryczne
@app.get("/asymmetric/key")
def asymmetric_key():
    global asymmetric_keys
    keys = asymmetric.get_asymmetric_key()

    asymmetric_keys = keys
    print(asymmetric_keys)
    return True

@app.get("/asymmetric/key/ssh")
def asymmetric_key_ssh():
    return asymmetric.get_asymmetric_key_ssh()


@app.post("/asymmetric/key")
def set_asymmetric_key(private_key: str, public_key: str):
    global asymmetric_keys

    asymmetric_keys = {
        "private": private_key,
        "public": public_key
    }

    return True


@app.post("/asymmetric/sign")
def asymmetric_sign(text: str):
    print("KEYS")
    print(asymmetric_keys)
    return asymmetric.sign(private_key=asymmetric_keys['private_key'], text=text)

@app.post("/asymmetric/verify")
def asymmetric_verify(text: str):
    return asymmetric.verify()


@app.post("/asymmetric/encode")
def asymmetric_encode(text: str):
    return asymmetric.encode()


@app.post("/asymmetric/decode")
def asymmetric_decode(text: str):
    return asymmetric.decode()
