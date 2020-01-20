from django.test import TestCase
from django.test import Client


class Exercise1Test(TestCase):
    def test_fields_in_view(self):
        """"Test that all the fields we defined appear in the HTML from the view."""
        c = Client()
        response = c.get('/form-example/')

        self.assertIn(b'<input type="text" name="text_input" value="Text Input">', response.content)

        self.assertIn(b'<input type="password" name="password_input" value="Password Input">', response.content)

        self.assertIn(b'<input type="checkbox" name="checkbox_on" value="Checkbox Checked" checked>', response.content)

        self.assertIn(b'<input type="radio" name="radio_input" value="Value One">', response.content)
        self.assertIn(b'<input type="radio" name="radio_input" value="Value Two" checked>', response.content)
        self.assertIn(b'<input type="radio" name="radio_input" value="Value Three">', response.content)

        self.assertIn(b'<select name="favorite_book">', response.content)
        self.assertIn(b'<optgroup label="Non-Fiction">', response.content)
        self.assertIn(b'<option value="1">Deep Learning with Keras</option>', response.content)
        self.assertIn(b'<option value="2">The Django Workshop</option>', response.content)
        self.assertIn(b'<optgroup label="Fiction">', response.content)
        self.assertIn(b'<option value="3">Brave New World</option>', response.content)
        self.assertIn(b'<option value="4">The Great Gatsby</option>', response.content)

        self.assertIn(b'<select name="books_you_own" multiple>', response.content)
        self.assertIn(b'<textarea name="text_area">Text Area Value</textarea>', response.content)

        self.assertIn(b'<input type="number" name="number_input" value="3.14159" step="any">', response.content)

        self.assertIn(b'<input type="email" name="email_input" value="user@example.com">', response.content)

        self.assertIn(b'<input type="date" name="date_input" value="2019-11-23">', response.content)

        self.assertIn(b'<input type="submit" name="submit_input" value="Submit Input">', response.content)

        self.assertIn(b'<button type="submit" name="button_element" value="Button Element">', response.content)
        self.assertIn(b'Button With <strong>Styled</strong> Text', response.content)

        self.assertIn(b'<input type="hidden" name="hidden_input" value="Hidden Value">', response.content)
