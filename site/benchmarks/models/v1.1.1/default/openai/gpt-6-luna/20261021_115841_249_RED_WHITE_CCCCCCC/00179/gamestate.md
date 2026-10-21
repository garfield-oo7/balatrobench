# Current Game State


- **Deck**: RED
- **Stake**: WHITE
- **Seed**: CCCCCCC

## Jokers

The current Jokers count is 5/5.

- 0: Hiker (Every played card permanently gains +5 Chips when scored)
  - **Sell value**: $2
- 1: Bootstraps (+2 Mult for every $5 you have (Currently +18 Mult))
  - **Sell value**: $3
  - **FOIL Edition**
- 2: Supernova (Adds the number of times poker hand has been played this run to Mult)
  - **Sell value**: $2
- 3: Mystic Summit (+15 Mult when 0 discards remaining)
  - **Sell value**: $2
- 4: Droll Joker (+10 Mult if played hand contains a Flush)
  - **Sell value**: $1

## Consumables

The current Consumables count is 0/2.


## Vouchers

Here is the list of vouchers redeemed during the run:

- v_clearance_sale: 
- v_grabber: 
- v_seed_money: 
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
- **Flush** (Level 6):
  - **Chips**: 110
  - **Mult**: 14
  - **Example**: `H_A, H_K, H_T, H_5, H_4`
  - During this run you have played Flush 26 times, 2 of which were played this round.
- **Pair** (Level 2):
  - **Chips**: 25
  - **Mult**: 3
  - **Example**: `S_K (not scored), S_9, D_9, H_6 (not scored), D_3 (not scored)`
  - During this run you have played Pair 9 times, 0 of which were played this round.
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
  - During this run you have played Three of a Kind 5 times, 0 of which were played this round.
- **Flush Five** (Level 1):
  - **Chips**: 160
  - **Mult**: 16
  - **Example**: `S_A, S_A, S_A, S_A, S_A`
  - During this run you have played Flush Five 0 times, 0 of which were played this round.
- **Two Pair** (Level 1):
  - **Chips**: 20
  - **Mult**: 2
  - **Example**: `H_A, D_A, C_Q (not scored), H_4, C_4`
  - During this run you have played Two Pair 16 times, 1 of which were played this round.
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






## Pack Selection

You have opened a booster pack. Choose a card or skip.

### Available Cards in Pack


- 0: **Cryptid** (Spectral)
  - **Effect**: Create 2 copies of 1 selected card in your hand


- 1: **Incantation** (Spectral)
  - **Effect**: Destroy 1 random card in your hand, add 4 random Enhanced numbered cards to your hand


- 2: **Ectoplasm** (Spectral)
  - **Effect**: Add Negative to a random Joker, -1 hand size


- 3: **Talisman** (Spectral)
  - **Effect**: Add a Gold Seal to 1 selected card in your hand




### Your Hand (for targeting)

- 0: A of H
- 1: A of H
- 2: 8 of S
- 3: 8 of H
- 4: 8 of C
- 5: 3 of D
- 6: 2 of C





# Tools available

You **MUST** use one of the following tools to perform the intended action:

- Select a card from the pack or skip
  - Function: `pack`
  - Parameters:
    - `card`: (integer, optional) 0-based index of card to select (omit if skipping)
    - `targets`: (list, optional) 0-based indices of hand cards to target (for Tarot/Spectral that require selection)
    - `skip`: (boolean, optional) Set to true to skip the pack without selecting a card
    - `reasoning`: (string) Strategic reasoning for this selection or skip
