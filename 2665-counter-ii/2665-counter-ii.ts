type ReturnObj = {
    increment: () => number,
    decrement: () => number,
    reset: () => number,
}

function createCounter(init: number): ReturnObj {
    let curVal=init;
    return {
        increment:()=>{
            curVal+=1
            return curVal;
        },
        decrement:()=>{
            curVal-=1
            return curVal;
        },
        reset:()=>{
            curVal=init
            return curVal;
        }
    }
	
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */