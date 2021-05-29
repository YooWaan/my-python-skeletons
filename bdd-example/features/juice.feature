Feature: Juice

   Scenario Outline: Make Juice
     Given I put <thing> ,
      When I mix
      Then it should transform into <juice>

      Eample: Fruit Set
      | thing | juice |
      | apple | apple juice |

