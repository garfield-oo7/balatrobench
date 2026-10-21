# Current Game State


- **Deck**: RED
- **Stake**: WHITE
- **Seed**: BBBBBBB

## Jokers

The current Jokers count is 5/5.

- 0: Mystic Summit (+15 Mult when 0 discards remaining)
  - **Sell value**: $1
- 1: Burglar (When Blind is selected, gain +3 Hands and lose all discards)
  - **Sell value**: $1
- 2: Photograph (First played face card gives X2 Mult when scored)
  - **Sell value**: $1
- 3: Ramen (X2 Mult, loses X0.01 Mult per card discarded)
  - **Sell value**: $1
- 4: Mad Joker (+10 Mult if played hand contains a Two Pair)
  - **Sell value**: $1

## Consumables

The current Consumables count is 2/3.

- 0: Pluto ((lvl.2) Level up High Card +1 Mult and +10 chips)
  - **Sell value**: $1
- 1: Mars ((lvl.1) Level up Four of a Kind +3 Mult and +30 chips)
  - **Sell value**: $1

## Vouchers

Here is the list of vouchers redeemed during the run:

- v_clearance_sale: 
- v_crystal_ball: 
- v_reroll_surplus: 
- v_liquidation: 
## Poker Hands

Here is a list of the poker hands and their levels:

- **Flush House** (Level 1):
  - **Chips**: 140
  - **Mult**: 14
  - **Example**: `D_7, D_7, D_7, D_4, D_4`
  - During this run you have played Flush House 0 times, 0 of which were played this round.
- **Full House** (Level 2):
  - **Chips**: 65
  - **Mult**: 6
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
  - During this run you have played Pair 11 times, 0 of which were played this round.
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
  - During this run you have played Straight 2 times, 0 of which were played this round.
- **Three of a Kind** (Level 4):
  - **Chips**: 90
  - **Mult**: 9
  - **Example**: `S_T, C_T, D_T, H_6 (not scored), D_5 (not scored)`
  - During this run you have played Three of a Kind 5 times, 0 of which were played this round.
- **Flush Five** (Level 1):
  - **Chips**: 160
  - **Mult**: 16
  - **Example**: `S_A, S_A, S_A, S_A, S_A`
  - During this run you have played Flush Five 0 times, 0 of which were played this round.
- **Two Pair** (Level 7):
  - **Chips**: 140
  - **Mult**: 8
  - **Example**: `H_A, D_A, C_Q (not scored), H_4, C_4`
  - During this run you have played Two Pair 18 times, 2 of which were played this round.
- **Five of a Kind** (Level 1):
  - **Chips**: 120
  - **Mult**: 12
  - **Example**: `S_A, H_A, H_A, C_A, D_A`
  - During this run you have played Five of a Kind 0 times, 0 of which were played this round.
- **High Card** (Level 2):
  - **Chips**: 15
  - **Mult**: 2
  - **Example**: `S_A, D_Q (not scored), D_9 (not scored), C_4 (not scored), D_3 (not scored)`
  - During this run you have played High Card 3 times, 0 of which were played this round.






## Pack Selection

You have opened a booster pack. Choose a card or skip.

### Available Cards in Pack


- 0: **Uranus** (Planet)
  - **Effect**: (lvl.7) Level up Two Pair +1 Mult and +20 chips


- 1: **Venus** (Planet)
  - **Effect**: (lvl.4) Level up Three of a Kind +2 Mult and +20 chips


- 2: **Saturn** (Planet)
  - **Effect**: (lvl.1) Level up Straight +3 Mult and +30 chips







# Tools available

You **MUST** use one of the following tools to perform the intended action:

- Select a card from the pack or skip
  - Function: `pack`
  - Parameters:
    - `card`: (integer, optional) 0-based index of card to select (omit if skipping)
    - `targets`: (list, optional) 0-based indices of hand cards to target (for Tarot/Spectral that require selection)
    - `skip`: (boolean, optional) Set to true to skip the pack without selecting a card
    - `reasoning`: (string) Strategic reasoning for this selection or skip
