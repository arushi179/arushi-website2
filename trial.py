probability_scores =  [[0.8 , 0.2]]
probability_scores=[j for elem in probability_scores for j in elem]
for i in range(len(probability_scores)):
        if i==0:
            prob_1=probability_scores[i]
      #print( prob_1)
        else:
            prob_2 = probability_scores[i]
           # print(prob_2)

print(prob_2)