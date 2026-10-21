# Current Game State


- **Deck**: RED
- **Stake**: WHITE
- **Seed**: DDDDDDD

## Jokers

The current Jokers count is 6/6.

- 0: Wrathful Joker (Played cards with Spade suit give +3 Mult when scored)
  - **Sell value**: $5
  - **NEGATIVE Edition**
- 1: Fibonacci (Each played Ace, 2, 3, 5, or 8 gives +8 Mult when scored)
  - **Sell value**: $4
- 2: Blackboard (X3 Mult if all cards held in hand are Spades or Clubs)
  - **Sell value**: $3
- 3: Arrowhead (Played cards with Spade suit give +50 Chips when scored)
  - **Sell value**: $3
- 4: Campfire (This Joker gains X0.25 Mult for each card sold, resets when Boss Blind is defeated (Currently X2.75 Mult))
  - **Sell value**: $4
- 5: Seltzer (Retrigger all cards played for the next 10 hands)
  - **Sell value**: $3

## Consumables

The current Consumables count is 0/2.


## Vouchers

Here is the list of vouchers redeemed during the run:

- v_seed_money: 
- v_reroll_surplus: 
- v_grabber: 
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
  - During this run you have played Full House 1 times, 0 of which were played this round.
- **Flush** (Level 6):
  - **Chips**: 110
  - **Mult**: 14
  - **Example**: `H_A, H_K, H_T, H_5, H_4`
  - During this run you have played Flush 21 times, 1 of which were played this round.
- **Pair** (Level 1):
  - **Chips**: 10
  - **Mult**: 2
  - **Example**: `S_K (not scored), S_9, D_9, H_6 (not scored), D_3 (not scored)`
  - During this run you have played Pair 3 times, 0 of which were played this round.
- **Four of a Kind** (Level 1):
  - **Chips**: 60
  - **Mult**: 7
  - **Example**: `S_J, H_J, C_J, D_J, C_3 (not scored)`
  - During this run you have played Four of a Kind 0 times, 0 of which were played this round.
- **Straight Flush** (Level 2):
  - **Chips**: 140
  - **Mult**: 12
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
- **High Card** (Level 2):
  - **Chips**: 15
  - **Mult**: 2
  - **Example**: `S_A, D_Q (not scored), D_9 (not scored), C_4 (not scored), D_3 (not scored)`
  - During this run you have played High Card 2 times, 1 of which were played this round.






## Pack Selection

You have opened a booster pack. Choose a card or skip.

### Available Cards in Pack


- 0: **The Star** (Tarot)
  - **Effect**: Converts up to 3 selected cards to Diamonds


- 1: **The Lovers** (Tarot)
  - **Effect**: Enhances 1 selected card into a Wild Card


- 2: **The Magician** (Tarot)
  - **Effect**: Enhances 2 selected cards to Lucky Cards


- 3: **Temperance** (Tarot)
  - **Effect**: Gives the total sell value of all current Jokers (Max of $50) (Currently $22)


- 4: **The Tower** (Tarot)
  - **Effect**: Enhances 1 selected card into a Stone Card




### Your Hand (for targeting)

- 0: A of S
- 1: K of D
- 2: Q of C
- 3: J of S
- 4: 9 of S
- 5: 7 of C
- 6: 4 of D
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
