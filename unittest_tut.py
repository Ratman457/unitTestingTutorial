from unittest import TestCase
from string import ascii_letters, punctuation, digits


def get_message_input():
    message = input("Please type the message you want to encrypt:")
    return message


def get_shift_factor_input():
    shift_factor = input("Please enter the desired shift factor:")
    while not shift_factor.isdigit():
        shift_factor = input("Please enter a number to represent the desired shift factor:")
    shift_factor = int(shift_factor)
    # Ensure that any shift factor will not overwhelm
    while shift_factor > 95:
        shift_factor -= 95
    return shift_factor


def encrypt(message, shift_factor):
    abc = (ascii_letters + punctuation + digits + " ") * 2
    encrypted_message = "".join([abc[abc.find(char) + shift_factor] for idx, char in enumerate(message)])
    print(message, " became ", encrypted_message)
    return encrypted_message


def main():
    encrypted_message = encrypt(get_message_input(), get_shift_factor_input())
    print(f"Your encrypted message is: {encrypted_message}")


class TestEncryption(TestCase):

    def setUp(self):
        self.my_message = "Pizza 9!"
        self.shift_factor = 17
    # tests go here

    def test_messageExists(self):
        self.assertIsNotNone(self.my_message)

    def test_shiftExists(self):
        self.assertIsNotNone(self.shift_factor)

    def test_messageType(self):
        self.assertIsInstance(self.my_message, str)

    def test_shiftFactorType(self):
        self.assertIsInstance(self.shift_factor, int)

    def test_shiftFactorSize(self):
        self.assertGreater(95, self.shift_factor)

    def test_getMessageInputFuncReturnsSomething(self):
        self.assertIsNotNone(get_message_input())

    def test_getShiftFactorInputFuncReturnsSomething(self):
        self.assertIsNotNone(get_shift_factor_input())

    def test_encryptFuncReturnsSomething(self):
        self.assertIsNotNone(encrypt(self.my_message, self.shift_factor))

    def test_messageLengthMatchesEncryptedLength(self):
        self.assertEqual(len(self.my_message), len(encrypt(self.my_message, self.shift_factor)))

    def test_encryptedIsDifferentFromMessage(self):
        self.assertNotIn(self.my_message, encrypt(self.my_message, self.shift_factor))

    def test_encryptedMessageType(self):
        self.assertIsInstance(encrypt(self.my_message, self.shift_factor), str)

    def test_shiftedCypherShiftsCorrectly(self):
        abc = (ascii_letters + punctuation + digits + " ") * 2
        encrypted_message = (
            "".join([abc[abc.find(char) + self.shift_factor] for idx, char in enumerate(self.my_message)]))
        self.assertEqual(encrypted_message, encrypt(self.my_message, self.shift_factor))


if __name__ == "__main__":
    main()
