# Current Game State


- **Deck**: RED
- **Stake**: WHITE
- **Seed**: BBBBBBB

## Jokers

The current Jokers count is 5/5.

- 0: Certificate (When round begins, add a random playing card with a random seal to your hand)
  - **Sell value**: $2
- 1: Zany Joker (+12 Mult if played hand contains a Three of a Kind)
  - **Sell value**: $1
- 2: Raised Fist (Adds double the rank of lowest ranked card held in hand to Mult)
  - **Sell value**: $2
- 3: Clever Joker (+80 Chips if played hand contains a Two Pair)
  - **Sell value**: $1
- 4: Abstract Joker (+3 Mult for each Joker card (Currently +15 Mult))
  - **Sell value**: $1

## Consumables

The current Consumables count is 1/2.

- 0: The Sun (Converts up to 3 selected cards to Hearts)
  - **Sell value**: $1

## Vouchers

Here is the list of vouchers redeemed during the run:

- v_clearance_sale: 
- v_reroll_surplus: 
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
- **Four of a Kind** (Level 1):
  - **Chips**: 60
  - **Mult**: 7
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
  - During this run you have played Straight 0 times, 0 of which were played this round.
- **Three of a Kind** (Level 4):
  - **Chips**: 90
  - **Mult**: 9
  - **Example**: `S_T, C_T, D_T, H_6 (not scored), D_5 (not scored)`
  - During this run you have played Three of a Kind 2 times, 1 of which were played this round.
- **Flush Five** (Level 1):
  - **Chips**: 160
  - **Mult**: 16
  - **Example**: `S_A, S_A, S_A, S_A, S_A`
  - During this run you have played Flush Five 0 times, 0 of which were played this round.
- **Two Pair** (Level 3):
  - **Chips**: 60
  - **Mult**: 4
  - **Example**: `H_A, D_A, C_Q (not scored), H_4, C_4`
  - During this run you have played Two Pair 2 times, 0 of which were played this round.
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


- 0: **The World** (Tarot)
  - **Effect**: Converts up to 3 selected cards to Spades


- 1: **Temperance** (Tarot)
  - **Effect**: Gives the total sell value of all current Jokers (Max of $50) (Currently $7)


- 2: **The Emperor** (Tarot)
  - **Effect**: Creates up to 2 random Tarot cards (Must have room)




### Your Hand (for targeting)

- 0: A of C
- 1: K of S
- 2: Q of S
- 3: T of S
- 4: 4 of D
- 5: 3 of S
- 6: 3 of H
- 7: 2 of H





# Tools available

You **MUST** use one of the following tools to perform the intended action:

- Select a card from the pack or skip
  - Function: `pack`
  - Parameters:
    - `card`: (integer, optional) 0-based index of card to select (omit if skipping)
    - `targets`: (list, optional) 0-based indices of hand cards to target (for Tarot/Spectral that require selection)
    - `skip`: (boolean, optional) Set to true to skip the pack without selecting a card
    - `reasoning`: (string) Strategic reasoning for this selection or skip
