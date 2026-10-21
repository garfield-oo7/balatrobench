# Current Game State


- **Deck**: RED
- **Stake**: WHITE
- **Seed**: DDDDDDD

## Jokers

The current Jokers count is 6/6.

- 0: Scary Face (Played face cards give +30 Chips when scored)
  - **Sell value**: $2
- 1: Wrathful Joker (Played cards with Spade suit give +3 Mult when scored)
  - **Sell value**: $5
  - **NEGATIVE Edition**
- 2: Even Steven (Played cards with even rank give +4 Mult when scored (10, 8, 6, 4, 2))
  - **Sell value**: $2
- 3: Ancient Joker (Each played card with Diamond suit gives X1.5 Mult when scored, suit changes at end of round)
  - **Sell value**: $4
- 4: Golden Joker (Earn $4 at end of round)
  - **Sell value**: $3
- 5: Abstract Joker (+3 Mult for each Joker card (Currently +18 Mult))
  - **Sell value**: $2

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
  - During this run you have played Full House 1 times, 0 of which were played this round.
- **Flush** (Level 1):
  - **Chips**: 35
  - **Mult**: 4
  - **Example**: `H_A, H_K, H_T, H_5, H_4`
  - During this run you have played Flush 8 times, 1 of which were played this round.
- **Pair** (Level 1):
  - **Chips**: 10
  - **Mult**: 2
  - **Example**: `S_K (not scored), S_9, D_9, H_6 (not scored), D_3 (not scored)`
  - During this run you have played Pair 2 times, 0 of which were played this round.
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
  - During this run you have played Three of a Kind 0 times, 0 of which were played this round.
- **Flush Five** (Level 1):
  - **Chips**: 160
  - **Mult**: 16
  - **Example**: `S_A, S_A, S_A, S_A, S_A`
  - During this run you have played Flush Five 0 times, 0 of which were played this round.
- **Two Pair** (Level 1):
  - **Chips**: 20
  - **Mult**: 2
  - **Example**: `H_A, D_A, C_Q (not scored), H_4, C_4`
  - During this run you have played Two Pair 0 times, 0 of which were played this round.
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


- 0: **The Moon** (Tarot)
  - **Effect**: Converts up to 3 selected cards to Clubs


- 1: **The Wheel of Fortune** (Tarot)
  - **Effect**: 1 in 4 chance to add Foil, Holographic, or Polychrome edition to a random Joker


- 2: **Judgement** (Tarot)
  - **Effect**: Creates a random Joker card (Must have room)


- 3: **Death** (Tarot)
  - **Effect**: Select 2 cards, convert the left card into the right card (Drag to rearrange)


- 4: **The Tower** (Tarot)
  - **Effect**: Enhances 1 selected card into a Stone Card




### Your Hand (for targeting)

- 0: Q of C
- 1: J of C
- 2: 8 of H
- 3: 7 of C
- 4: 6 of C
- 5: 5 of C
- 6: 3 of D
- 7: 2 of S





# Tools available

You **MUST** use one of the following tools to perform the intended action:

- Select a card from the pack or skip
  - Function: `pack`
  - Parameters:
    - `card`: (integer, optional) 0-based index of card to select (omit if skipping)
    - `targets`: (list, optional) 0-based indices of hand cards to target (for Tarot/Spectral that require selection)
    - `skip`: (boolean, optional) Set to true to skip the pack without selecting a card
    - `reasoning`: (string) Strategic reasoning for this selection or skip
