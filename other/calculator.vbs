'(c)2025 Justus Decker - A very simple VBS Calculator
a = InputBox("Type in the first number","Calculator")
b = InputBox("Type in the second number","Calculator")
c = CDbl(a) + CDbl(b)
MsgBox "The result is: " & c