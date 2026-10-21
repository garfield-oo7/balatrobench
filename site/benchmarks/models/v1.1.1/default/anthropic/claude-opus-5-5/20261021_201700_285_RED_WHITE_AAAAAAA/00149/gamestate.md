# Current Game State


- **Phase**: Shop Phase (gamestate is SHOP)
- **Round**: 20
- **Ante**: 7/8
- **Money**: $33
- **Deck**: RED
- **Stake**: WHITE
- **Seed**: AAAAAAA

## Jokers

The current Jokers count is 5/5.

- 0: Spare Trousers (This Joker gains +2 Mult if played hand contains a Two Pair (Currently +48 Mult))
  - **Sell value**: $3
- 1: Odd Todd (Played cards with odd rank give +31 Chips when scored (A, 9, 7, 5, 3))
  - **Sell value**: $2
- 2: Ancient Joker (Each played card with Club suit gives X1.5 Mult when scored, suit changes at end of round)
  - **Sell value**: $4
- 3: Acrobat (X3 Mult on final hand of round)
  - **Sell value**: $3
- 4: The Duo (X2 Mult if played hand contains a Pair)
  - **Sell value**: $4

## Consumables

The current Consumables count is 0/2.


## Vouchers

Here is the list of vouchers redeemed during the run:

- v_wasteful: 
## Poker Hands

Here is a list of the poker hands and their levels:

- **Flush House** (Level 2):
  - **Chips**: 180
  - **Mult**: 18
  - **Example**: `D_7, D_7, D_7, D_4, D_4`
  - During this run you have played Flush House 0 times, 0 of which were played this round.
- **Full House** (Level 5):
  - **Chips**: 140
  - **Mult**: 12
  - **Example**: `H_K, C_K, D_K, S_2, D_2`
  - During this run you have played Full House 1 times, 0 of which were played this round.
- **Flush** (Level 2):
  - **Chips**: 50
  - **Mult**: 6
  - **Example**: `H_A, H_K, H_T, H_5, H_4`
  - During this run you have played Flush 1 times, 0 of which were played this round.
- **Pair** (Level 2):
  - **Chips**: 25
  - **Mult**: 3
  - **Example**: `S_K (not scored), S_9, D_9, H_6 (not scored), D_3 (not scored)`
  - During this run you have played Pair 3 times, 0 of which were played this round.
- **Four of a Kind** (Level 2):
  - **Chips**: 90
  - **Mult**: 10
  - **Example**: `S_J, H_J, C_J, D_J, C_3 (not scored)`
  - During this run you have played Four of a Kind 0 times, 0 of which were played this round.
- **Straight Flush** (Level 2):
  - **Chips**: 140
  - **Mult**: 12
  - **Example**: `S_Q, S_J, S_T, S_9, S_8`
  - During this run you have played Straight Flush 1 times, 0 of which were played this round.
- **Straight** (Level 2):
  - **Chips**: 60
  - **Mult**: 7
  - **Example**: `D_J, C_T, C_9, S_8, H_7`
  - During this run you have played Straight 1 times, 0 of which were played this round.
- **Three of a Kind** (Level 2):
  - **Chips**: 50
  - **Mult**: 5
  - **Example**: `S_T, C_T, D_T, H_6 (not scored), D_5 (not scored)`
  - During this run you have played Three of a Kind 2 times, 0 of which were played this round.
- **Flush Five** (Level 2):
  - **Chips**: 210
  - **Mult**: 19
  - **Example**: `S_A, S_A, S_A, S_A, S_A`
  - During this run you have played Flush Five 0 times, 0 of which were played this round.
- **Two Pair** (Level 9):
  - **Chips**: 180
  - **Mult**: 10
  - **Example**: `H_A, D_A, C_Q (not scored), H_4, C_4`
  - During this run you have played Two Pair 23 times, 2 of which were played this round.
- **Five of a Kind** (Level 2):
  - **Chips**: 155
  - **Mult**: 15
  - **Example**: `S_A, H_A, H_A, C_A, D_A`
  - During this run you have played Five of a Kind 0 times, 0 of which were played this round.
- **High Card** (Level 2):
  - **Chips**: 15
  - **Mult**: 2
  - **Example**: `S_A, D_Q (not scored), D_9 (not scored), C_4 (not scored), D_3 (not scored)`
  - During this run you have played High Card 2 times, 0 of which were played this round.




## Shop

Here are the available cards in the shop:


- 0: Scary Face (Played face cards give +30 Chips when scored)
  - **Set**: Joker
  - **Cost**: $4
  - **Sell value**: $2
- 1: The Wheel of Fortune (1 in 4 chance to add Foil, Holographic, or Polychrome edition to a random Joker)
  - **Set**: Tarot
  - **Cost**: $3
  - **Sell value**: $1

The cost of the reroll is $5.


Here are the vouchers that can be redeemed:

- 0: Overstock (+1 card slot available in shop)
  - **Cost**: $10



### Booster Packs

- 0: **Spectral Pack**
  - **Effect**: Choose 1 of up to 2 Spectral cards to be used immediately
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
