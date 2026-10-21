# Current Game State


- **Phase**: Shop Phase (gamestate is SHOP)
- **Round**: 23
- **Ante**: 8/8
- **Money**: $27
- **Deck**: RED
- **Stake**: WHITE
- **Seed**: BBBBBBB

## Jokers

The current Jokers count is 5/5.

- 0: Abstract Joker (+3 Mult for each Joker card (Currently +15 Mult))
  - **Sell value**: $1
  - **HOLO Edition**
- 1: Zany Joker (+12 Mult if played hand contains a Three of a Kind)
  - **Sell value**: $1
  - **HOLO Edition**
- 2: Ramen (X1.9 Mult, loses X0.01 Mult per card discarded)
  - **Sell value**: $1
- 3: Campfire (This Joker gains X0.25 Mult for each card sold, resets when Boss Blind is defeated (Currently X4 Mult))
  - **Sell value**: $2
- 4: Card Sharp (X3 Mult if played poker hand has already been played this round)
  - **Sell value**: $1

## Consumables

The current Consumables count is 1/3.

- 0: The Fool (Creates the last Tarot or Planet card used during this run The Fool excluded )
  - **Sell value**: $1

## Vouchers

Here is the list of vouchers redeemed during the run:

- v_crystal_ball: 
- v_grabber: 
- v_liquidation: 
- v_clearance_sale: 
- v_overstock_norm: 
- v_reroll_surplus: 
- v_paint_brush: 
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
  - During this run you have played Full House 2 times, 0 of which were played this round.
- **Flush** (Level 1):
  - **Chips**: 35
  - **Mult**: 4
  - **Example**: `H_A, H_K, H_T, H_5, H_4`
  - During this run you have played Flush 3 times, 0 of which were played this round.
- **Pair** (Level 2):
  - **Chips**: 25
  - **Mult**: 3
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
  - During this run you have played Straight 0 times, 0 of which were played this round.
- **Three of a Kind** (Level 11):
  - **Chips**: 230
  - **Mult**: 23
  - **Example**: `S_T, C_T, D_T, H_6 (not scored), D_5 (not scored)`
  - During this run you have played Three of a Kind 7 times, 0 of which were played this round.
- **Flush Five** (Level 1):
  - **Chips**: 160
  - **Mult**: 16
  - **Example**: `S_A, S_A, S_A, S_A, S_A`
  - During this run you have played Flush Five 0 times, 0 of which were played this round.
- **Two Pair** (Level 9):
  - **Chips**: 180
  - **Mult**: 10
  - **Example**: `H_A, D_A, C_Q (not scored), H_4, C_4`
  - During this run you have played Two Pair 10 times, 1 of which were played this round.
- **Five of a Kind** (Level 1):
  - **Chips**: 120
  - **Mult**: 12
  - **Example**: `S_A, H_A, H_A, C_A, D_A`
  - During this run you have played Five of a Kind 0 times, 0 of which were played this round.
- **High Card** (Level 1):
  - **Chips**: 5
  - **Mult**: 1
  - **Example**: `S_A, D_Q (not scored), D_9 (not scored), C_4 (not scored), D_3 (not scored)`
  - During this run you have played High Card 2 times, 0 of which were played this round.




## Shop

Here are the available cards in the shop:


- 0: Mars ((lvl.1) Level up Four of a Kind +3 Mult and +30 chips)
  - **Set**: Planet
  - **Cost**: $1
  - **Sell value**: $1
- 1: Joker Stencil (X1 Mult for each empty Joker slot Joker Stencil included (Currently X0))
  - **Set**: Joker
  - **Cost**: $4
  - **Sell value**: $2

The cost of the reroll is $4.




### Booster Packs

- 0: **Jumbo Celestial Pack**
  - **Effect**: Choose 1 of up to 5 Planet cards to be used immediately
  - **Cost**: $3
- 1: **Arcana Pack**
  - **Effect**: Choose 1 of up to 3 Tarot cards to be used immediately
  - **Cost**: $2







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
