class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        sum_gas = sum(gas)
        sum_cost = sum(cost)

        if sum_gas < sum_cost:
            return -1
        
        total_gas = 0
        start_node = 0

        for i in range(len(gas)):
            total_gas += gas[i] - cost[i]

            if total_gas < 0:
                start_node = i + 1
                total_gas = 0
        
        return start_node
