import attrs


@attrs.define()
class Pdf:
    filename: str
    base64_encoded: bool
    content: str
