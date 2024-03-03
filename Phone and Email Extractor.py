import re,pyperclip

phone_re = re.compile(r'(\+\d{2}|)(\d{10})')
email_re = re.compile(r'''(
                      [a-zA-Z0-9._%+-]+
                      @
                      [a-zA-Z0-9.-]+
                      (\.[a-zA-Z]{2,4})
                      )''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []

for groups in phone_re.findall(text):
    phone_num = '-'.join(groups)
    matches.append(phone_num)

for groups in email_re.findall(text):
    matches.append(groups[0])

if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')