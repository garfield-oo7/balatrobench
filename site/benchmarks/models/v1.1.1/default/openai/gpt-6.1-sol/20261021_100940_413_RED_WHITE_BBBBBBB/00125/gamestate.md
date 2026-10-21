# Current Game State


- **Deck**: RED
- **Stake**: WHITE
- **Seed**: BBBBBBB

## Jokers

The current Jokers count is 5/5.

- 0: Zany Joker (+12 Mult if played hand contains a Three of a Kind)
  - **Sell value**: $1
- 1: Raised Fist (Adds double the rank of lowest ranked card held in hand to Mult)
  - **Sell value**: $2
- 2: Banner (+30 Chips for each remaining discard)
  - **Sell value**: $2
- 3: Abstract Joker (+3 Mult for each Joker card (Currently +15 Mult))
  - **Sell value**: $1
- 4: Ramen (X2 Mult, loses X0.01 Mult per card discarded)
  - **Sell value**: $2

## Consumables

The current Consumables count is 2/3.

- 0: The Moon (Converts up to 3 selected cards to Clubs)
  - **Sell value**: $1
- 1: Judgement (Creates a random Joker card (Must have room))
  - **Sell value**: $1

## Vouchers

Here is the list of vouchers redeemed during the run:

- v_clearance_sale: 
- v_reroll_surplus: 
- v_grabber: 
- v_crystal_ball: 
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
  - During this run you have played Full House 2 times, 0 of which were played this round.
- **Flush** (Level 1):
  - **Chips**: 35
  - **Mult**: 4
  - **Example**: `H_A, H_K, H_T, H_5, H_4`
  - During this run you have played Flush 2 times, 0 of which were played this round.
- **Pair** (Level 1):
  - **Chips**: 10
  - **Mult**: 2
  - **Example**: `S_K (not scored), S_9, D_9, H_6 (not scored), D_3 (not scored)`
  - During this run you have played Pair 6 times, 1 of which were played this round.
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
- **Three of a Kind** (Level 6):
  - **Chips**: 130
  - **Mult**: 13
  - **Example**: `S_T, C_T, D_T, H_6 (not scored), D_5 (not scored)`
  - During this run you have played Three of a Kind 4 times, 0 of which were played this round.
- **Flush Five** (Level 1):
  - **Chips**: 160
  - **Mult**: 16
  - **Example**: `S_A, S_A, S_A, S_A, S_A`
  - During this run you have played Flush Five 0 times, 0 of which were played this round.
- **Two Pair** (Level 5):
  - **Chips**: 100
  - **Mult**: 6
  - **Example**: `H_A, D_A, C_Q (not scored), H_4, C_4`
  - During this run you have played Two Pair 5 times, 1 of which were played this round.
- **Five of a Kind** (Level 1):
  - **Chips**: 120
  - **Mult**: 12
  - **Example**: `S_A, H_A, H_A, C_A, D_A`
  - During this run you have played Five of a Kind 0 times, 0 of which were played this round.
- **High Card** (Level 1):
  - **Chips**: 5
  - **Mult**: 1
  - **Example**: `S_A, D_Q (not scored), D_9 (not scored), C_4 (not scored), D_3 (not scored)`
  - During this run you have played High Card 1 times, 0 of which were played this round.






## Pack Selection

You have opened a booster pack. Choose a card or skip.

### Available Cards in Pack


- 0: **Uranus** (Planet)
  - **Effect**: (lvl.5) Level up Two Pair +1 Mult and +20 chips


- 1: **Mars** (Planet)
  - **Effect**: (lvl.1) Level up Four of a Kind +3 Mult and +30 chips


- 2: **Venus** (Planet)
  - **Effect**: (lvl.6) Level up Three of a Kind +2 Mult and +20 chips


- 3: **Mercury** (Planet)
  - **Effect**: (lvl.1) Level up Pair +1 Mult and +15 chips


- 4: **Earth** (Planet)
  - **Effect**: (lvl.1) Level up Full House +2 Mult and +25 chips







# Tools available

You **MUST** use one of the following tools to perform the intended action:

- Select a card from the pack or skip
  - Function: `pack`
  - Parameters:
    - `card`: (integer, optional) 0-based index of card to select (omit if skipping)
    - `targets`: (list, optional) 0-based indices of hand cards to target (for Tarot/Spectral that require selection)
    - `skip`: (boolean, optional) Set to true to skip the pack without selecting a card
    - `reasoning`: (string) Strategic reasoning for this selection or skip
