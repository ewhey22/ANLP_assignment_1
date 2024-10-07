###### USEFUL FORMULAS #######

# Total sequence probability for trigrams: 
# P_hat(x_1, x_2, x_3 ...., x_n) = 
# p(x_1|</s> <s>) * p(x_2|<s> x_1) * p(x_3|x_1 x_2) * p(x_4|x_2 x_3) .... * p(x_n|x_n-2 x_n-1) ??? * p(</s>|x_n-1 x_n)

# Trigram estimation with MLE (not ideal, will overfit)= 
# Count(w_x-2 w_x-1 w_x)/ Count(w_x-2 w_x-1)

# Deal with zero count numerators (i.e. no w_x-2 w_x-1 w_x sequence in the training data) with smoothing 

# Perplexity =
# 











# 4.3.2:
#By looking at the language model probabilities in this file, can you say anything about the
# kind of estimation method that was used? We are not asking for certainty, but based on your
# knowledge of English and of different estimation methods, you should be able to narrow down
# the possibilities.
# Write a paragraph or so explaining which method(s) might have been used, and say what
# evidence your guess is based on.

# MLE? -- overfitting, relatively high probability for low n-gram counts

# Add-one smoothing? -- takes too much probability mass from high frequency n-grams 

# Add-alpha smoothing? --all unseen n-grams have same probability, even when this is unrepresentative of human language 

# G-T? -- all unseen n-grams have same probability, even when this is unrepresentative of human language

# Interpolation 

# Stupid backoff? --- Not a distribution - probabilities won't add to 1


