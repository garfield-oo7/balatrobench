# Current Game State

- **Phase**: Playing Phase (gamestate is SELECTING_HAND)
- **Round**: 16
- **Ante**: 6/8
- **Money**: $27
- **Hands left**: 7/7
- **Discards left**: 0/0
- **Current Blind**: Small
- **Target Score**: 20000
- **Current Score**: 0
- **Deck**: RED
- **Stake**: WHITE
- **Seed**: AAAAAAA

## Jokers

The current Jokers count is 5/5.

- 0: Burglar (When Blind is selected, gain +3 Hands and lose all discards)
  - **Sell value**: $3
- 1: Scary Face (Played face cards give +30 Chips when scored)
  - **Sell value**: $2
- 2: Green Joker (+1 Mult per hand played -1 Mult per discard (Currently +28 Mult))
  - **Sell value**: $3
  - **HOLO Edition**
- 3: Hanging Chad (Retrigger first played card used in scoring 2 additional times)
  - **Sell value**: $2
- 4: Photograph (First played face card gives X2 Mult when scored)
  - **Sell value**: $2

## Consumables

The current Consumables count is 0/2.


## Vouchers

Here is the list of vouchers redeemed during the run:

- v_directors_cut: 
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
  - During this run you have played Full House 0 times, 0 of which were played this round.
- **Flush** (Level 2):
  - **Chips**: 50
  - **Mult**: 6
  - **Example**: `H_A, H_K, H_T, H_5, H_4`
  - During this run you have played Flush 4 times, 0 of which were played this round.
- **Pair** (Level 1):
  - **Chips**: 10
  - **Mult**: 2
  - **Example**: `S_K (not scored), S_9, D_9, H_6 (not scored), D_3 (not scored)`
  - During this run you have played Pair 7 times, 0 of which were played this round.
- **Four of a Kind** (Level 1):
  - **Chips**: 60
  - **Mult**: 7
  - **Example**: `S_J, H_J, C_J, D_J, C_3 (not scored)`
  - During this run you have played Four of a Kind 0 times, 0 of which were played this round.
- **Straight Flush** (Level 1):
  - **Chips**: 100
  - **Mult**: 8
  - **Example**: `S_Q, S_J, S_T, S_9, S_8`
  - During this run you have played Straight Flush 0 times, 0 of which were played this round.
- **Straight** (Level 1):
  - **Chips**: 30
  - **Mult**: 4
  - **Example**: `D_J, C_T, C_9, S_8, H_7`
  - During this run you have played Straight 0 times, 0 of which were played this round.
- **Three of a Kind** (Level 1):
  - **Chips**: 30
  - **Mult**: 3
  - **Example**: `S_T, C_T, D_T, H_6 (not scored), D_5 (not scored)`
  - During this run you have played Three of a Kind 2 times, 0 of which were played this round.
- **Flush Five** (Level 1):
  - **Chips**: 160
  - **Mult**: 16
  - **Example**: `S_A, S_A, S_A, S_A, S_A`
  - During this run you have played Flush Five 0 times, 0 of which were played this round.
- **Two Pair** (Level 2):
  - **Chips**: 40
  - **Mult**: 3
  - **Example**: `H_A, D_A, C_Q (not scored), H_4, C_4`
  - During this run you have played Two Pair 11 times, 0 of which were played this round.
- **Five of a Kind** (Level 1):
  - **Chips**: 120
  - **Mult**: 12
  - **Example**: `S_A, H_A, H_A, C_A, D_A`
  - During this run you have played Five of a Kind 0 times, 0 of which were played this round.
- **High Card** (Level 2):
  - **Chips**: 15
  - **Mult**: 2
  - **Example**: `S_A, D_Q (not scored), D_9 (not scored), C_4 (not scored), D_3 (not scored)`
  - During this run you have played High Card 21 times, 0 of which were played this round.


## Current Hand

The current card count is 8 / 8
**CRITICAL LIMIT: You can play or discard MAXIMUM 5 cards per action - NEVER MORE THAN 5 CARDS (this is an absolute game rule).**


- 0: A of S (`S_A`)
- 1: Q of H (`H_Q`)
- 2: T of H (`H_T`)
- 3: 8 of C (`C_8`)
  - **BONUS Enhancement**
- 4: 5 of C (`C_5`)
- 5: 4 of H (`H_4`)
- 6: 2 of H (`H_2`)
- 7: 2 of D (`D_2`)







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
