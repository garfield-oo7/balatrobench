# Current Game State


- **Deck**: RED
- **Stake**: WHITE
- **Seed**: AAAAAAA

## Jokers

The current Jokers count is 5/5.

- 0: Mad Joker (+10 Mult if played hand contains a Two Pair)
  - **Sell value**: $2
- 1: Burglar (When Blind is selected, gain +3 Hands and lose all discards)
  - **Sell value**: $3
- 2: Runner (Gains +15 Chips if played hand contains a Straight (Currently +0 Chips))
  - **Sell value**: $4
  - **HOLO Edition**
- 3: Half Joker (+20 Mult if played hand contains 3 or fewer cards)
  - **Sell value**: $2
- 4: Ancient Joker (Each played card with Diamond suit gives X1.5 Mult when scored, suit changes at end of round)
  - **Sell value**: $4

## Consumables

The current Consumables count is 0/2.


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
  - During this run you have played Flush 1 times, 0 of which were played this round.
- **Pair** (Level 1):
  - **Chips**: 10
  - **Mult**: 2
  - **Example**: `S_K (not scored), S_9, D_9, H_6 (not scored), D_3 (not scored)`
  - During this run you have played Pair 4 times, 1 of which were played this round.
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
- **Straight** (Level 2):
  - **Chips**: 60
  - **Mult**: 7
  - **Example**: `D_J, C_T, C_9, S_8, H_7`
  - During this run you have played Straight 1 times, 0 of which were played this round.
- **Three of a Kind** (Level 1):
  - **Chips**: 30
  - **Mult**: 3
  - **Example**: `S_T, C_T, D_T, H_6 (not scored), D_5 (not scored)`
  - During this run you have played Three of a Kind 0 times, 0 of which were played this round.
- **Flush Five** (Level 1):
  - **Chips**: 160
  - **Mult**: 16
  - **Example**: `S_A, S_A, S_A, S_A, S_A`
  - During this run you have played Flush Five 0 times, 0 of which were played this round.
- **Two Pair** (Level 2):
  - **Chips**: 40
  - **Mult**: 3
  - **Example**: `H_A, D_A, C_Q (not scored), H_4, C_4`
  - During this run you have played Two Pair 5 times, 1 of which were played this round.
- **Five of a Kind** (Level 1):
  - **Chips**: 120
  - **Mult**: 12
  - **Example**: `S_A, H_A, H_A, C_A, D_A`
  - During this run you have played Five of a Kind 0 times, 0 of which were played this round.
- **High Card** (Level 2):
  - **Chips**: 15
  - **Mult**: 2
  - **Example**: `S_A, D_Q (not scored), D_9 (not scored), C_4 (not scored), D_3 (not scored)`
  - During this run you have played High Card 8 times, 1 of which were played this round.






## Pack Selection

You have opened a booster pack. Choose a card or skip.

### Available Cards in Pack


- 0: **Earth** (Planet)
  - **Effect**: (lvl.1) Level up Full House +2 Mult and +25 chips


- 1: **Venus** (Planet)
  - **Effect**: (lvl.1) Level up Three of a Kind +2 Mult and +20 chips


- 2: **Pluto** (Planet)
  - **Effect**: (lvl.2) Level up High Card +1 Mult and +10 chips


- 3: **Mercury** (Planet)
  - **Effect**: (lvl.1) Level up Pair +1 Mult and +15 chips


- 4: **Uranus** (Planet)
  - **Effect**: (lvl.2) Level up Two Pair +1 Mult and +20 chips







# Tools available

You **MUST** use one of the following tools to perform the intended action:

- Select a card from the pack or skip
  - Function: `pack`
  - Parameters:
    - `card`: (integer, optional) 0-based index of card to select (omit if skipping)
    - `targets`: (list, optional) 0-based indices of hand cards to target (for Tarot/Spectral that require selection)
    - `skip`: (boolean, optional) Set to true to skip the pack without selecting a card
    - `reasoning`: (string) Strategic reasoning for this selection or skip
