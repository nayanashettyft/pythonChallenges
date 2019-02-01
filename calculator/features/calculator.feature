Feature: Test my calculator

  Scenario Outline: Test positive scenarios of add int Feature
    Given we have a calculator 
    When we give 2 Ints <Num1> and <Num2>
    Then we get the int result of <Result>
  Examples: positive
  | Num1  | Num2  | Result|
  | 4     | 2     | 6     |
  | -4    | 4     | 0     |
  | -4    | 2     | -2    |
  | 0     | 2     | 2     |
  | 0     | 0     | 0     |


  Scenario Outline: Test positive scenarios of add float Feature
    Given we have a calculator 
    When we give 2 Floats <Float1> and <Float2>
    Then we get the float result of <Result>
  Examples: positive
  | Float1  | Float2  | Result|
  | 4.0   | 2.1       | 6.1   |
  | -4.0  | 4.2       | 0.2   |
  | -4.3  | 2.0       | -2.3  |
  | 2.5   | -1        | 1.5   |
  | 0     | 2         | 2     |
  | 0     | 0         | 0     |




#  Scenario Outline: Test negative scenarios of add Feature
#    Given we have a calculator 
#    When we give <Val1> and <Val2>
#    Then we get a failure
#  Examples: negative
#  | Num1  | Num2  |
#  | a     | b     |
#  | "Text"| 4     |

  