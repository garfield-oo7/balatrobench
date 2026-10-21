# Current Game State

- **Phase**: Playing Phase (gamestate is SELECTING_HAND)
- **Round**: 24
- **Ante**: 8/8
- **Money**: $8
- **Hands left**: 5/5
- **Discards left**: 2/4
- **Current Blind**: Boss (Crimson Heart: One random Joker disabled every hand)
- **Target Score**: 100000
- **Current Score**: 0
- **Deck**: RED
- **Stake**: WHITE
- **Seed**: BBBBBBB

## Jokers

The current Jokers count is 5/5.

- 0: Abstract Joker (All abilities are disabled)
  - **Sell value**: $1
  - **Debuff**: this joker is debuffed so its effect is disabled
- 1: Zany Joker (+12 Mult if played hand contains a Three of a Kind)
  - **Sell value**: $1
  - **HOLO Edition**
- 2: Ramen (X1.41 Mult, loses X0.01 Mult per card discarded)
  - **Sell value**: $1
- 3: Campfire (This Joker gains X0.25 Mult for each card sold, resets when Boss Blind is defeated (Currently X4 Mult))
  - **Sell value**: $2
- 4: Card Sharp (X3 Mult if played poker hand has already been played this round)
  - **Sell value**: $1

## Consumables

The current Consumables count is 0/2.


## Vouchers

Here is the list of vouchers redeemed during the run:

- v_liquidation: 
- v_clearance_sale: 
- v_reroll_surplus: 
- v_grabber: 
- v_paint_brush: 
## Poker Hands

Here is a list of the poker hands and their levels:

- **Flush House** (Level 1):
  - **Chips**: 140
  - **Mult**: 14
  - **Example**: `D_7, D_7, D_7, D_4, D_4`
  - During this run you have played Flush House 0 times, 0 of which were played this round.
- **Full House** (Level 1):
  - **Chips**: 40
  - **Mult**: 4
  - **Example**: `H_K, C_K, D_K, S_2, D_2`
  - During this run you have played Full House 4 times, 0 of which were played this round.
- **Flush** (Level 1):
  - **Chips**: 35
  - **Mult**: 4
  - **Example**: `H_A, H_K, H_T, H_5, H_4`
  - During this run you have played Flush 1 times, 0 of which were played this round.
- **Pair** (Level 1):
  - **Chips**: 10
  - **Mult**: 2
  - **Example**: `S_K (not scored), S_9, D_9, H_6 (not scored), D_3 (not scored)`
  - During this run you have played Pair 2 times, 0 of which were played this round.
- **Four of a Kind** (Level 3):
  - **Chips**: 120
  - **Mult**: 13
  - **Example**: `S_J, H_J, C_J, D_J, C_3 (not scored)`
  - During this run you have played Four of a Kind 1 times, 0 of which were played this round.
- **Straight Flush** (Level 1):
  - **Chips**: 100
  - **Mult**: 8
  - **Example**: `S_Q, S_J, S_T, S_9, S_8`
  - During this run you have played Straight Flush 0 times, 0 of which were played this round.
- **Straight** (Level 1):
  - **Chips**: 30
  - **Mult**: 4
  - **Example**: `D_J, C_T, C_9, S_8, H_7`
  - During this run you have played Straight 1 times, 0 of which were played this round.
- **Three of a Kind** (Level 9):
  - **Chips**: 190
  - **Mult**: 19
  - **Example**: `S_T, C_T, D_T, H_6 (not scored), D_5 (not scored)`
  - During this run you have played Three of a Kind 9 times, 0 of which were played this round.
- **Flush Five** (Level 1):
  - **Chips**: 160
  - **Mult**: 16
  - **Example**: `S_A, S_A, S_A, S_A, S_A`
  - During this run you have played Flush Five 0 times, 0 of which were played this round.
- **Two Pair** (Level 11):
  - **Chips**: 220
  - **Mult**: 12
  - **Example**: `H_A, D_A, C_Q (not scored), H_4, C_4`
  - During this run you have played Two Pair 10 times, 0 of which were played this round.
- **Five of a Kind** (Level 1):
  - **Chips**: 120
  - **Mult**: 12
  - **Example**: `S_A, H_A, H_A, C_A, D_A`
  - During this run you have played Five of a Kind 0 times, 0 of which were played this round.
- **High Card** (Level 1):
  - **Chips**: 5
  - **Mult**: 1
  - **Example**: `S_A, D_Q (not scored), D_9 (not scored), C_4 (not scored), D_3 (not scored)`
  - During this run you have played High Card 0 times, 0 of which were played this round.


## Current Hand

The current card count is 9 / 9
**CRITICAL LIMIT: You can play or discard MAXIMUM 5 cards per action - NEVER MORE THAN 5 CARDS (this is an absolute game rule).**


- 0: A of C (`C_A`)
- 1: Q of H (`H_Q`)
- 2: Q of C (`C_Q`)
- 3: J of H (`H_J`)
  - **STEEL Enhancement**
- 4: T of H (`H_T`)
- 5: 9 of C (`C_9`)
  - **GOLD Seal**
- 6: 7 of S (`S_7`)
- 7: 7 of S (`S_7`)
  - **BLUE Seal**
- 8: 5 of D (`D_5`)
  - **STEEL Enhancement**







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
