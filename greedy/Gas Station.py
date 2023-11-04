from typing import List


class Solution:
    # def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    #     final=[]
    #     cost_route_new = cost*2
    #     gas_new= gas*2
    #     print(gas_new)
    #
    #
    #
    #
    #     for i in range(len(gas) - 1):
    #         gas_tank=0
    #         goal_reach = False
    #
    #
    #         for j in range(i,i+len(cost)):
    #             if j+1 == i+len(cost):
    #                 goal_reach=True
    #             current_gas = gas_new[j]
    #             gas_tank=gas_tank+current_gas
    #             if gas_tank < cost_route_new[j] and goal_reach ==True:
    #                 break
    #             if gas_tank >= cost_route_new[j] and goal_reach == True:
    #                 final.append(i)
    #
    #             gas_tank-= current_gas
    #     if len(final) ==0:
    #         return -1
    #     else:
    #         print(final)
    #         return final[0] +1

    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n=len(gas)
        for i in range(n):
            gas[i]=gas[i]-cost[i]
        if sum(gas)<0 :
            return -1
        print(sum(gas))

        s=0
        x=0
        for i in range(n):
            s+=gas[i]
            if s<0:
                s=0
                x=i+1
        return x

a=Solution()
gas = [1,2,3,4,5]
cost = [3,4,5,1,2]

print(a.canCompleteCircuit(gas,cost))







