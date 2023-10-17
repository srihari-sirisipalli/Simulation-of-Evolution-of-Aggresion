import random
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd

class Agent:
    def __init__(self,type_history=[],food_history=[],current_food=0,dead=False):
        if len(type_history)==0:
            weights = [1, 0]
            self.type_history=[np.random.choice(['dove', 'hawk'], p=weights)]
            self.current_food=0
        else:
            self.type_history=type_history.copy()
            self.current_food=current_food
        self.dead=dead
        self.food_history=food_history.copy()
        
    
    def update_details(self,current_food):
        if current_food==0:
            self.dead=True
        else:
            self.food_history.append(current_food)

    
    def current_details(self):
        return self.type_history[-1],self.food_history[-1]
    
    def print_details(self):
        print("Agent Details:")
        print(f"Dead: {self.dead}")
        print(f"Type History: {self.type_history}")
        print(f"Food History: {self.food_history}")
        print('-------------------------')

class Simulation:
    def __init__(self, num_agents, num_generations):
        self.num_agents = num_agents
        self.num_generations = num_generations
        self.alive_agents=[Agent() for _ in range(num_agents)]
        self.dead_agents=[]
        self.count_alive_dove=[]
        self.count_alive_hawk=[]
        self.total_alive=[]
        self.dove_population=0
        self.hawk_population=0

    def interact(self, agent1, agent2):
        if agent2==None:
            agent1.current_food=2
            agent1.food_history.append(agent1.current_food)
        elif agent1.type_history[-1] == 'dove' and agent2.type_history[-1] == 'dove':
            agent1.current_food = 1
            agent2.current_food = 1
            agent1.food_history.append(agent1.current_food)
            agent2.food_history.append(agent2.current_food)
        elif agent1.type_history[-1] == 'dove' and agent2.type_history[-1] == 'hawk':
            agent1.current_food=0.5
            agent2.current_food=1.5
            agent1.food_history.append(agent1.current_food)
            agent2.food_history.append(agent2.current_food)

        elif agent1.type_history[-1] == 'hawk' and agent2.type_history[-1] == 'dove':

            agent1.current_food=1.5
            agent2.current_food=0.5
            agent1.food_history.append(agent1.current_food)
            agent2.food_history.append(agent2.current_food)

        elif agent1.type_history[-1]=='hawk' and agent2.type_history[-1] =='hawk':
            # Both are hawks
            agent1.current_food = 0
            agent2.current_food = 0
            agent2.food_history.append(agent1.current_food)
            agent2.food_history.append(agent2.current_food)
        
    
    def compete(self):
        random.shuffle(self.alive_agents)
        i=0
        while i<len(self.alive_agents):
            # n_agents=random.choice([1,2])
            random_weight=random.random()
            # weights = [1-random_weight,random_weight]
            weights = [0.75,0.25]
            n_agents=np.random.choice([2, 1], p=weights)
            if n_agents==2 and i<=len(self.alive_agents)-2:
                agent1=self.alive_agents[i]
                agent2=self.alive_agents[i+1]
                i=i+1
            elif n_agents==2 and i==len(self.alive_agents)-1:
                agent1=self.alive_agents[i]
                agent2=None
            elif n_agents==1:
                agent1=self.alive_agents[i]
                agent2=None
            i=i+1
            if agent2!=None:
                # print("*****************")
                # print(agent1.type_history[-1],agent2.type_history[-1])
                # print("*****************")
                self.interact(agent1,agent2)
            else:
                # print("*****************")
                # print(agent1.type_history[-1])
                # print("*****************")
                self.interact(agent1,agent2)
    def reproduce(self):
        for agent in self.alive_agents:
            if agent.current_food==2:
                new_agent=Agent(type_history=[agent.type_history[-1]])
                self.alive_agents.append(new_agent)
                agent.current_food = 0
            elif agent.current_food==3/2 and random.choice([1,0])==1:
                new_agent=Agent(type_history=[agent.type_history[-1]])
                self.alive_agents.append(new_agent)
                agent.current_food = 0
    def survive(self):
        agents_to_remove = []
        for agent in self.alive_agents:
            if agent.current_food == 0:
                agent.dead = True
                self.dead_agents.append(agent)
                agents_to_remove.append(agent)
            elif agent.current_food == 1/2:
                if random.choice([1, 0]) == 1:
                    agent.dead = True
                    self.dead_agents.append(agent)
                    agents_to_remove.append(agent)
                    agent.current_food=0

                else:
                    agent.current_food=0
            elif agent.current_food == 1:
                agent.current_food = 0
        
        # Remove agents outside the loop
        for agent in agents_to_remove:
            self.alive_agents.remove(agent)

    def inject_new_agents(self,n=0,type=None):
        if n>0:
            if type==None:
                weights = [0.5, 0.5]
                type=[np.random.choice(['dove', 'hawk'], p=weights)]
            for i in range(n):
                self.alive_agents.append(Agent(type_history=[type]))
    def print_statistics(self):
        num_dove_agents = sum(1 for agent in self.alive_agents if agent.type_history[-1] == 'dove' and not agent.dead)
        num_hawk_agents = sum(1 for agent in self.alive_agents if agent.type_history[-1] == 'hawk' and not agent.dead)
        num_alive_agents = len(self.alive_agents)
        # num_dead_agents=len(self.dead_agents)
        print("Simulation Statistics:")
        print(f"Total Number of Alive Agents: {num_alive_agents}")
        # print(f"Total Number of Dead Agents: {num_dead_agents}")

        print(f"Number of Dove Agents: {num_dove_agents}")
        print(f"Number of Hawk Agents: {num_hawk_agents}")
        print("=========================")
    def collect_data(self):
        self.count_alive_dove.append(self.dove_population)
        self.count_alive_hawk.append(self.hawk_population)
        self.total_alive.append(self.dove_population+self.hawk_population)
    def run(self):
        for generation in range(self.num_generations):
            # print(f"Generation {generation} Agent Details:")
            self.dove_population=sum(1 for agent in self.alive_agents if agent.type_history[-1] == 'dove' and not agent.dead)
            self.hawk_population=sum(1 for agent in self.alive_agents if agent.type_history[-1] == 'hawk' and not agent.dead)
            self.collect_data()
            # for agent in self.alive_agents:
            #     agent.print_details()
            # Print statistics at the end of the generation
            # self.print_statistics()
            
            # print("=========================")
            if generation==10:
                self.inject_new_agents(1,'hawk')

            self.compete()
            self.survive()
            self.reproduce()

        self.dove_population=sum(1 for agent in self.alive_agents if agent.type_history[-1] == 'dove' and not agent.dead)
        self.hawk_population=sum(1 for agent in self.alive_agents if agent.type_history[-1] == 'hawk' and not agent.dead)
        self.collect_data()

        # print(f"Generation {num_generations} Agent Details:")
        # for agent in self.alive_agents:
        #     agent.print_details()
            # Print statistics at the end of the generation
        # self.print_statistics()
        # print("=========================")
        df=pd.DataFrame(list(zip([i for i in range(0,self.num_generations+1)],self.count_alive_dove ,self.count_alive_hawk,self.total_alive)) ,columns=['generation','dove','hawk','total'])
        plt.plot(df['generation'],df['dove'])
        plt.fill_between(df['generation'], 0, df['dove'], color='blue')
        plt.plot(df['generation'],df['total'])
        plt.fill_between(df['generation'], df['dove'], df['total'], where=(df['total'] > df['dove']), interpolate=True, color='red')
        

 
        plt.show()
    

num_agents =6  # Change the number of agents
num_generations = 100
simulation = Simulation(num_agents, num_generations)
simulation.run()
