import random
import math
import matplotlib.pyplot as plt
import multiprocessing  as mp
from collections import Counter

class Reservoir:
    # reservoir 
    pool = list()
    #sample size: account for the index of received data    
    index = 0

    def __init__(self, pool_capacity: int):
        #pool size: pool_capacity
        self.pool_capacity = pool_capacity

    def receive_data(self, data: str or int):
        """ accept data and sample """
        #When i<=k, the element enters the pool directly
        #The probability of each element entering the pool is 1 
        if self.index < self.pool_capacity:
          self.pool.append(data)
        #When i>k, elements in the pool will be randomly replaced by new element  
        #Every element of dataset within the probability of sample_size/dataset_size(pool_capacity/dataset_size) to stay in pool         
        else:                
          d_index = random.randint(0, self.index)            
          if d_index in range(0, self.pool_capacity):
            self.pool[d_index] = data

        self.index += 1

    #release instance
    def _del_(self):
       del self.pool[0:self.index]
       self.index = 0     

def test_reservoir_with_dataset(sum_res_dict,sample_size,dataset_size,iterator):
    #dataset size: how many data in the stream  
    dataset = range(1,dataset_size+1)

    #sample size: param->pool_capacity
    resN = [Reservoir(sample_size) for i in range(iterator)]
    samples = list()

    #using itertor to repeat the reservoir sampling
    #obtain ideal sample results through a large number of randomness
    for i in range(iterator):
        for d in dataset:
           resN[i].receive_data(d) 
        samples.extend(resN[i].pool)
        #print("reservoir sampling",i+1,":",resN[i].pool)
        resN[i]._del_()

    #count the sampling res in each distributed reservoir 
    r = dict(Counter(samples))
    #print(r)

    #summary res of all distributed sampling 
    for s in range(1,dataset_size+1):
       sum_res_dict[s] = sum_res_dict[s] + r[s]

    return r

       
 

if __name__ == '__main__':   
    #test_reservoir_with_dataset(4,10,1000)
    sample_size = 4
    dataset_size = 10

    #make the most of CPU
    num_cores = int(mp.cpu_count())
    #print(num_cores)
    pool = mp.Pool(num_cores)

    #initialize the batch of iterator param 
    iterator_dict = dict()
    random_nums = random.sample(range(sample_size,dataset_size+1000000),num_cores)
    print("the iterator for each distribution: ",random_nums)
    N = 0 #sum of total sample in all distribution
    for id in range(num_cores):
       iterator_dict[id] = random_nums[id]
       N += random_nums[id]

    #using dict to share the results of  all distributed sampling
    manager = mp.Manager()
    sum_res_dict = manager.dict()
    for s in range(1,dataset_size+1):
       sum_res_dict[s] = 0 
    
    #distributed reservior
    pool_results = [pool.apply_async(test_reservoir_with_dataset, args=(sum_res_dict,sample_size,dataset_size,iterator)) for task, iterator in iterator_dict.items()]
   
    #analysis the res from distribution
    distri_res_ct = 1
    dis_probabilties_1 = list()
    for i in pool_results:
        #sort the value with key, map to the sequence of datas in dataset
        temp_dict = i.get()
        print(temp_dict)
        distri_sample_with_dtseque =  [temp_dict[k] for k in sorted(temp_dict.keys())]
        
        #probabilities of distribution samples
        dis_probabilties = [round(i/random_nums[distri_res_ct-1],3) for i in distri_sample_with_dtseque]
        dis_probabilties_1.append(dis_probabilties[0])
        print("distribution",distri_res_ct,": ",dis_probabilties)
        distri_res_ct += 1

    #release sub-threads
    pool.close()
    pool.join()
    
    #analysis summary of all distribution in main-thread
    #sum(M_distri)/sum(N_distri)
    print(sum_res_dict)
    sum_probabilties = [round(M/N,3) for M in list(sum_res_dict.values())]
    print("summary: ",sum_probabilties)
    dis_probabilties_1.append(sum_probabilties[0])

    #draw chart
    plt.figure(1)
    plt.pie(sum_probabilties, labels=range(1,dataset_size+1), autopct='%1.1f%%')

    plt.figure(2)
    plt.plot(range(1,num_cores+2), dis_probabilties_1, linestyle='-',color="r")
    plt.show() 



        
    

    
    