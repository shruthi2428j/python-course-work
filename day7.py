s="python programming"
s.startswith('py')
True
s.startswith('java')
False
s.endswith('ed')
False
'abc'.isalpha()
True
'abc1'.isalpha()
False
'abc def'.isalpha()
False
'abc@'.isalpha()
False
'1abc'.isalpha()
False
'abcsd'.isalnum()
True
'12abc'.isalnum()
True
'$%@'.isalnum()
False
'abc'.islower()
True
'Abc'.isupper()
False
'ABC'.isupper()
True
'shruthi  kummari'.isspace()
False
'shruthikummari'.isspace()
False
'    '.isspace()
True
'Abc Bced Cde'.istitle()
True
'my_var.isidentifier()

'my_var'.isidentifier()
True
'234.isdecimal()

'234'.isdecimal()
True
'abc'.isdecimal()
False
'12.3'.isdigit()
False


