func maxProfit(prices []int) int {
    profit := 0
    low := 100000

    for _, elem := range prices {
        if elem < low {
            low = elem
        } else if diff := elem - low; diff > profit {
            profit = diff
        }
        
    }

    return profit;
}
