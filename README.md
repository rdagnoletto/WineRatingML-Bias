# WineRatingML Bias
 


Personal Project using tensorflow and some ML theories. My goal was to try to remove the bias from wine scores (for example, a reviewer may prefer wine type X over Y so it would be hard to compare scores). So if they gave a wine of type X a 98 and a Y wine a 95, my goal was to find out which wine is more of a standout. If they regularly rate wines of type X in the high 90s and rarely give Y wines over 91, the Y wine that got a 95 is theoretically more of an exceptional wine than the 98 once biased was removed.

I did this by scraping wine scores from the web and then training models to predict the score each reviewer would give a wine based on the country it was made in, the varietal, the price, and some other factors (not vintage because this varies in quality outside of the reviewer bias). Then by comparing the predicted scores to the real scores (actual score minus predicted score) I could say that positive numbers are better than average for the price and type and the opposite for negative scores.
