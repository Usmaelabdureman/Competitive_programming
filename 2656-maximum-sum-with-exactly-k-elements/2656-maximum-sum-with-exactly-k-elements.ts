function maximizeSum(nums: number[], k: number): number {
    nums.sort((a,b)=>a-b);
    let score=0
    for (let i =0;i<k;i++){
        const m=nums.pop();
        score+=m
        nums.push(m+1)
    }
    return score
};