# Current Game State


- **Phase**: Shop Phase (gamestate is SHOP)
- **Round**: 20
- **Ante**: 7/8
- **Money**: $54
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
- 2: Ancient Joker (Each played card with Spade suit gives X1.5 Mult when scored, suit changes at end of round)
  - **Sell value**: $4
- 3: Blackboard (X3 Mult if all cards held in hand are Spades or Clubs)
  - **Sell value**: $3
- 4: Arrowhead (Played cards with Spade suit give +50 Chips when scored)
  - **Sell value**: $3
- 5: Campfire (This Joker gains X0.25 Mult for each card sold, resets when Boss Blind is defeated (Currently X1.25 Mult))
  - **Sell value**: $4

## Consumables

The current Consumables count is 1/2.

- 0: Earth ((lvl.1) Level up Full House +2 Mult and +25 chips)
  - **Sell value**: $1

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
  - During this run you have played Flush 19 times, 1 of which were played this round.
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
  - During this run you have played Two Pair 1 times, 0 of which were played this round.
- **Five of a Kind** (Level 1):
  - **Chips**: 120
  - **Mult**: 12
  - **Example**: `S_A, H_A, H_A, C_A, D_A`
  - During this run you have played Five of a Kind 0 times, 0 of which were played this round.
- **High Card** (Level 2):
  - **Chips**: 15
  - **Mult**: 2
  - **Example**: `S_A, D_Q (not scored), D_9 (not scored), C_4 (not scored), D_3 (not scored)`
  - During this run you have played High Card 4 times, 0 of which were played this round.




## Shop

Here are the available cards in the shop:


- 0: Mars ((lvl.1) Level up Four of a Kind +3 Mult and +30 chips)
  - **Set**: Planet
  - **Cost**: $3
  - **Sell value**: $1

The cost of the reroll is $3.




### Booster Packs

- 0: **Standard Pack**
  - **Effect**: Choose 1 of up to 3 Playing cards to add to your deck
  - **Cost**: $4
- 1: **Celestial Pack**
  - **Effect**: Choose 1 of up to 3 Planet cards to be used immediately
  - **Cost**: $4







# Tools available

You **MUST** use one of the following tools to perform the intended action:

- Buy a card, voucher, or pack from the shop
  - Function: `buy`
  - Parameters (provide exactly one of):
    - `card`: (integer) 0-based index of shop card to buy
    - `voucher`: (integer) 0-based index of voucher to buy
    - `pack`: (integer) 0-based index of booster pack to buy and open
    - `reasoning`: (string) Strategic reasoning for this purchase
- Reroll the shop items
  - Function: `reroll`
  - Parameters:
    - `reasoning`: (string) Strategic reasoning for rerolling
- Leave the shop and advance to blind selection
  - Function: `next_round`
  - Parameters:
    - `reasoning`: (string) Strategic reasoning for leaving the shop
- Rearrange jokers or consumables
  - Function: `rearrange`
  - Parameters (provide exactly one of):
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
