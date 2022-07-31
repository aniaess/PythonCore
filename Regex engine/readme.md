This program find regex pattern without re module.
Special characters supported ^, $, ?, *, + ,. ,/ .

#####Examples:
- Input:      '\.$|end.'              Output: True
- Input:     '3\+3|3+3=6'             Output: True
- Input:       '\?|Is this working?'  Output: True
- Input:       '\\|\'                 Output: True
- Input: 'colou\?r|color'             Output: False
- Input: 'colou\?r|colour'            Output: False
