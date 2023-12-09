## Notes
- Card Game
- Regular card values
- We can have 5 of a kind omg
- Hand comparison = Classical
- If 2 hands with the same type : Check on first card value
  - If equals again, check on second card and so on...

## Input
- A list of hands (5 cards) ; An associated bid

## Goal
- Order them according to their strength

## Ideas

- Hand classification
  - Hand = Dict {A:0, K:2, Q:2, J:1, ...}
    - Stop search when we have 5 cards total
- Hand sorter
  - Five of a kind : hand.values() = 5
  - Four of a kind : hand.values() =4
  - Full house: hand.values() = 3;2
  - 3 kind : hand.values() = 3;1; 1
  - 2 pair : Hand.values() = 2;2;1
  - 1 pair: Hand.values() =2;1;1;1
  - High: Hand.values() = 1;1;1;1;1