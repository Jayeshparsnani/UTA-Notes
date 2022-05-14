from sys import argv

class project3:
    def __init__(self):
        self.h1 = [0.1, 1, 0]
        self.h2 = [0.2, 0.75, 0.25]
        self.h3 = [0.4, 0.5, 0.5]
        self.h4 = [0.2, 0.25, 0.75]
        self.h5 = [0.1, 0, 1]
        self.bags = [self.h1, self.h2, self.h3, self.h4, self.h5]
        self.obs = 0.5
#   finding posterior probability.
    def posterior_probability(self, cand):
        for candy in self.bags:
            if cand=='C':
                candy[0] = candy[1]*candy[0]/self.obs
            else:
                candy[0] = candy[2]*candy[0]/self.obs
                
# changing observation of candy after every step.
    def candy_observation(self, cand):
        self.obs = 0
        for candy in self.bags:
            if cand=="C":
                self.obs += candy[0] * candy[1]
            else:
                self.obs += candy[0] * candy[2]
        return self.obs

if __name__ == "__main__":
    Q = argv[1]
    P3 = project3()
    f = open('result.txt', 'w')
    f.write("Observation sequence Q: {}\n".format(Q))
    f.write("Length of Q: {}\n".format(len(Q)))
    Q = Q  + 'C' # for extra candy
    P3.candy_observation(Q[0])
    for i in range(len(Q)-1):
        f.write("\nAfter Observation {}: {}\n\n".format(i+1, Q[i]))   
        P3.posterior_probability(Q[i])
        curr = P3.candy_observation(Q[i+1])
        for j in range(len(P3.bags)):
            f.write("P(h{} | Q) = {}\n".format(j+1, P3.bags[j][0]))
        if Q[i+1]=='C':
            f.write("\nProbability that the next candy we pick will be C, given Q: {}".format(curr))
            f.write("\nProbability that the next candy we pick will be L, given Q: {}\n".format(1-curr))
        else:
            f.write("\nProbability that the next candy we pick will be C, given Q: {}".format(1-curr))
            f.write("\nProbability that the next candy we pick will be L, given Q: {}\n".format(curr))