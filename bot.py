import gym
import universe
import random

# what the bot does?
# step 1 determine should i turn?
# step 2 where to turn?

#reinformation learning function
def determine_turn(turn, observation_n, j, total_sum, prev_total_sum, reward_n):
    ''' for every 14 iterations , sum the total observations, take the average
    if lower than 0, change the directions . if we go i4 iterations and get a reward each step, we're doing something right
    thats when we turn'''
    if(j == 14):
        if(total_sum/j) == 0:
            turn = True
        else:
            turn = False

        #reset variables
        total_sum = 0
        j = 0
        prev_total_sum = total_sum
        total_sum = 0
    else:
        turn = False
    if(observation_n != None):
        j+=1
        total_sum += reward_n
    return (turn, j, total_sum, prev_total_sum)

def main():
    env = gym.make('flashgames.CoasterRacer-v0')
    #initiate environment (gym)/universe
    # sets up the environmest in vnc docker

    observation_n = env.reset()

    #initialize variables
    #define the number of game iterations

    n = 0
    j = 0

    #sum of observations

    total_sum = 0
    prev_total_sum = 0
    turn = False

    #defining keyboard actions

    left = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', True), ('KeyEvent', 'ArrowRight', False)]
    right = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'ArrowRight', True)]
    forward = [('KeyEvent', 'ArrowUp', True), ('KeyEvent', 'ArrowLeft', False), ('KeyEvent', 'ArrowRight', False)]


    #logic
    while True:
        n+=1
        # counter for the number of iterations of the game

        if(n > 1):
            if (observation_n[0] != None):
                prev_score = reward_n[0]
                # store the reward in the variable

                if (turn):
                    event = random.choice([left, right])
                    # perform an action
                    action_n = [event for ob in observation_n]
                    turn = False
        elif(~turn):
            action_n = [forward for  ob in observation_n]
            #if no turn is needed , go straight

        if(observation_n[0] != None):
            turn, j, total_sum, prev_total_sum = determine_turn(turn, observation_n[0], j, total_sum, prev_total_sum, reward_n[0])

        #save new variables for each iteration
        observation_n, reward_n, done_n, info = env.step(action_n)
        #a time step

        env.render()
        #rendereing our enviroment for every time step
if __name__ == '__main__':
    main()








