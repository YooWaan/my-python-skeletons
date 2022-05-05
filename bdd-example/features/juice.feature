Feature: Juice

Scenario Outline: Make Juice
   Given I put <thing> ,
   When I mix
   Then it should transform into <juice>

   Examples: Fruit Set
   | thing | juice |
   | apple | apple juice |

Scenario Outline: ジュースを作る
   Given 果物を <thing> 用意します
   When 混ぜます
   Then <juice> ができました

   Examples: Fruit Set
   | thing  | juice        |
   | banana | banana juice |
