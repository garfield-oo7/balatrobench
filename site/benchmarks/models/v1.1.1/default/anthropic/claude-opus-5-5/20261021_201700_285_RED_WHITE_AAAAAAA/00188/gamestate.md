# Current Game State

- **Phase**: Playing Phase (gamestate is SELECTING_HAND)
- **Round**: 24
- **Ante**: 8/8
- **Money**: $3
- **Hands left**: 2/4
- **Discards left**: 3/5
- **Current Blind**: Boss (Amber Acorn: Flips and shuffles all Joker cards)
- **Target Score**: 100000
- **Current Score**: 62172
- **Deck**: RED
- **Stake**: WHITE
- **Seed**: AAAAAAA

## Jokers

The current Jokers count is 5/5.

- 0: the joker is face down
- 1: the joker is face down
- 2: the joker is face down
- 3: the joker is face down
- 4: the joker is face down

## Consumables

The current Consumables count is 1/2.

- 0: Death (Select 2 cards, convert the left card into the right card (Drag to rearrange))
  - **Sell value**: $1

## Vouchers

Here is the list of vouchers redeemed during the run:

- v_wasteful: 
## Poker Hands

Here is a list of the poker hands and their levels:

- **Flush House** (Level 2):
  - **Chips**: 180
  - **Mult**: 18
  - **Example**: `D_7, D_7, D_7, D_4, D_4`
  - During this run you have played Flush House 0 times, 0 of which were played this round.
- **Full House** (Level 5):
  - **Chips**: 140
  - **Mult**: 12
  - **Example**: `H_K, C_K, D_K, S_2, D_2`
  - During this run you have played Full House 2 times, 0 of which were played this round.
- **Flush** (Level 3):
  - **Chips**: 65
  - **Mult**: 8
  - **Example**: `H_A, H_K, H_T, H_5, H_4`
  - During this run you have played Flush 1 times, 0 of which were played this round.
- **Pair** (Level 2):
  - **Chips**: 25
  - **Mult**: 3
  - **Example**: `S_K (not scored), S_9, D_9, H_6 (not scored), D_3 (not scored)`
  - During this run you have played Pair 4 times, 0 of which were played this round.
- **Four of a Kind** (Level 2):
  - **Chips**: 90
  - **Mult**: 10
  - **Example**: `S_J, H_J, C_J, D_J, C_3 (not scored)`
  - During this run you have played Four of a Kind 0 times, 0 of which were played this round.
- **Straight Flush** (Level 2):
  - **Chips**: 140
  - **Mult**: 12
  - **Example**: `S_Q, S_J, S_T, S_9, S_8`
  - During this run you have played Straight Flush 1 times, 0 of which were played this round.
- **Straight** (Level 2):
  - **Chips**: 60
  - **Mult**: 7
  - **Example**: `D_J, C_T, C_9, S_8, H_7`
  - During this run you have played Straight 1 times, 0 of which were played this round.
- **Three of a Kind** (Level 2):
  - **Chips**: 50
  - **Mult**: 5
  - **Example**: `S_T, C_T, D_T, H_6 (not scored), D_5 (not scored)`
  - During this run you have played Three of a Kind 2 times, 0 of which were played this round.
- **Flush Five** (Level 2):
  - **Chips**: 210
  - **Mult**: 19
  - **Example**: `S_A, S_A, S_A, S_A, S_A`
  - During this run you have played Flush Five 0 times, 0 of which were played this round.
- **Two Pair** (Level 10):
  - **Chips**: 200
  - **Mult**: 11
  - **Example**: `H_A, D_A, C_Q (not scored), H_4, C_4`
  - During this run you have played Two Pair 29 times, 2 of which were played this round.
- **Five of a Kind** (Level 2):
  - **Chips**: 155
  - **Mult**: 15
  - **Example**: `S_A, H_A, H_A, C_A, D_A`
  - During this run you have played Five of a Kind 0 times, 0 of which were played this round.
- **High Card** (Level 2):
  - **Chips**: 15
  - **Mult**: 2
  - **Example**: `S_A, D_Q (not scored), D_9 (not scored), C_4 (not scored), D_3 (not scored)`
  - During this run you have played High Card 2 times, 0 of which were played this round.


## Current Hand

The current card count is 8 / 8
**CRITICAL LIMIT: You can play or discard MAXIMUM 5 cards per action - NEVER MORE THAN 5 CARDS (this is an absolute game rule).**


- 0: A of C (`C_A`)
- 1: A of D (`D_A`)
- 2: A of D (`D_A`)
  - **GOLD Enhancement**
- 3: Q of H (`H_Q`)
- 4: 4 of S (`S_4`)
- 5: 4 of C (`C_4`)
- 6: 3 of S (`S_3`)
  - **STEEL Enhancement**
- 7: 3 of D (`D_3`)







# Tools available

You **MUST** use one of the following tools to perform the intended action:

- Play cards from hand
  - Function: `play`
  - Parameters:
    - `cards`: (list) 0-based indices of cards to play (1-5 cards)
    - `reasoning`: (string) Strategic reasoning for playing these cards
- Discard cards from hand
  - Function: `discard`
  - Parameters:
    - `cards`: (list) 0-based indices of cards to discard
    - `reasoning`: (string) Strategic reasoning for discarding these cards
- Rearrange cards in hand, jokers, or consumables
  - Function: `rearrange`
  - Parameters (provide exactly one of):
    - `hand`: (list) New order of hand cards (0-based indices, must include all cards)
    - `jokers`: (list) New order of jokers (0-based indices, must include all jokers)
    - `consumables`: (list) New order of consumables (0-based indices, must include all consumables)
    - `reasoning`: (string) Strategic reasoning for this arrangement
- Sell a joker or consumable for money
  - Function: `sell`
  - Parameters (provide exactly one of):
    - `joker`: (integer) 0-based index of joker to sell
    - `consumable`: (integer) 0-based index of consumable to sell
    - `reasoning`: (string) Strategic reasoning for selling
- Use a consumable card (Tarot, Planet, or Spectral)
  - Function: `use`
  - Parameters:
    - `consumable`: (integer) 0-based index of consumable to use
    - `cards`: (list) 0-based indices of cards to target (required for some consumables)
    - `reasoning`: (string) Strategic reasoning for using this consumable
