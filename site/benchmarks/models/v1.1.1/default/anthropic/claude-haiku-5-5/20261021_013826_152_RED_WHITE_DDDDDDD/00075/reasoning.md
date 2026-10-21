My hand has spades debuffed, with only four non-spade cards (H_A, H_9, D_5, H_4), so a flush is off the table since the spades won't score even if I include them for the hand type. I need to think about what scoring combination works best given this constraint, with 4 hands and 4 discards left to hit 10000.

Estimating roughly 69% odds of drawing at least one spade, I calculate the flush score would land around 4785 since all spades are debuffed and only joker bonuses contribute — far short of 10000. That pushes me to consider a hearts-based flush instead, since H_A, H_9, H_4, and D_5 could work if I draw two more hearts and avoid the debuff issue entirely.

Scoring a 5-heart flush with A, 9, 4 gives roughly 5577 points including the flush bonus and multipliers — still not enough. I'm factoring in Odd Todd's +31 chips for each odd-ranked card (A, 9, 5 all qualify) and Scary Face's +30 for face cards, trying to see if a hearts flush with a face card drawn in could push the total closer to 10000.

I realize I should use the Jupiter consumable now to level up the flush for +80 chips and +10 mult, and consider using The Empress to turn the A and 9 into Mult cards for an extra +8 mult when scored. Planning to apply Jupiter first, then Empress on two key cards.

For the discard, I'll keep the three hearts and discard the off-suit cards, hoping to draw into more hearts for the flush. I'm estimating the probability of drawing at least two more hearts from the remaining deck, roughly calculating the odds come out around 80% or so given the heart density left.

For consumable order, I'll use Jupiter first then Empress, since using Empress removes it and shifts the index of remaining consumables, so I need to track the indices carefully to target the right hand cards with each effect.

