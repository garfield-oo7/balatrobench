With 7 cards and three hearts among them, I'm weighing whether to discard the non-heart cards like the jack, ten, seven, and three to try drawing toward a flush, since I still have discards available.

Running the hypergeometric math, getting roughly 7% chance of landing 2+ more hearts in 4 draws, which is pretty low. Maybe I should reconsider keeping fewer cards or look at a straight draw instead using H_8, H_6, H_5 with the other cards.

Actually I spot a straight draw opportunity: keeping 5,6,7,8 and needing a 4 or 9 gives 8 outs out of roughly 40 unseen cards, better odds than the flush. Discarding S_J, C_T, S_3 to chase that straight at level 1 would give decent chips and mult, though I'll need to verify it clears 600 alone.

But comparing to the flush option: with Crafty's flush boost, even a modest heart flush could be worth far more than repeated straights, so I'm weighing whether to pursue the flush by discarding non-hearts repeatedly across multiple hands instead.

Finishing that calculation, P(≥2 hearts)=1-0.149-0.373≈0.478, so roughly 50% to complete the flush. I'll go with discarding the off-suit cards to chase the flush, though I'm second-guessing whether keeping C_7 for a backdoor straight is worth it instead.

