# Current Game State

- **Phase**: Playing Phase (gamestate is SELECTING_HAND)
- **Round**: 15
- **Ante**: 5/8
- **Money**: $8
- **Hands left**: 3/4
- **Discards left**: 1/4
- **Current Blind**: Boss (The Fish: Cards drawn face down after each hand played)
- **Target Score**: 22000
- **Current Score**: 7425
- **Deck**: RED
- **Stake**: WHITE
- **Seed**: EEEEEEE

## Jokers

The current Jokers count is 5/5.

- 0: Even Steven (Played cards with even rank give +4 Mult when scored (10, 8, 6, 4, 2))
  - **Sell value**: $2
- 1: Smeared Joker (Hearts and Diamonds count as the same suit, Spades and Clubs count as the same suit)
  - **Sell value**: $3
- 2: Jolly Joker (+8 Mult if played hand contains a Pair)
  - **Sell value**: $1
- 3: Supernova (Adds the number of times poker hand has been played this run to Mult)
  - **Sell value**: $2
- 4: Vagabond (Create a Tarot card if hand is played with $4 or less)
  - **Sell value**: $4

## Consumables

The current Consumables count is 2/2.

- 0: Judgement (Creates a random Joker card (Must have room))
  - **Sell value**: $1
- 1: The Magician (Enhances 2 selected cards to Lucky Cards)
  - **Sell value**: $1

## Poker Hands

Here is a list of the poker hands and their levels:

- **Flush House** (Level 1):
  - **Chips**: 140
  - **Mult**: 14
  - **Example**: `D_7, D_7, D_7, D_4, D_4`
  - During this run you have played Flush House 0 times, 0 of which were played this round.
- **Full House** (Level 3):
  - **Chips**: 90
  - **Mult**: 8
  - **Example**: `H_K, C_K, D_K, S_2, D_2`
  - During this run you have played Full House 0 times, 0 of which were played this round.
- **Flush** (Level 5):
  - **Chips**: 95
  - **Mult**: 12
  - **Example**: `H_A, H_K, H_T, H_5, H_4`
  - During this run you have played Flush 23 times, 1 of which were played this round.
- **Pair** (Level 4):
  - **Chips**: 55
  - **Mult**: 5
  - **Example**: `S_K (not scored), S_9, D_9, H_6 (not scored), D_3 (not scored)`
  - During this run you have played Pair 0 times, 0 of which were played this round.
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
- **Three of a Kind** (Level 2):
  - **Chips**: 50
  - **Mult**: 5
  - **Example**: `S_T, C_T, D_T, H_6 (not scored), D_5 (not scored)`
  - During this run you have played Three of a Kind 1 times, 0 of which were played this round.
- **Flush Five** (Level 1):
  - **Chips**: 160
  - **Mult**: 16
  - **Example**: `S_A, S_A, S_A, S_A, S_A`
  - During this run you have played Flush Five 0 times, 0 of which were played this round.
- **Two Pair** (Level 2):
  - **Chips**: 40
  - **Mult**: 3
  - **Example**: `H_A, D_A, C_Q (not scored), H_4, C_4`
  - During this run you have played Two Pair 1 times, 0 of which were played this round.
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

The current card count is 8 / 8
**CRITICAL LIMIT: You can play or discard MAXIMUM 5 cards per action - NEVER MORE THAN 5 CARDS (this is an absolute game rule).**


- 0: K of D (`D_K`)
- 1: Q of H (`H_Q`)
- 2: T of H (`H_T`)
- 3: 9 of D (`D_9`)
- 4: 7 of H (`H_7`)
- 5: 7 of C (`C_7`)
- 6: 7 of D (`D_7`)
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
