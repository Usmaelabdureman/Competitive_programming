type ToBeOrNotToBe = {
    toBe: (val: any) => boolean;
    notToBe: (val: any) => boolean;
};

function expect(val: any): ToBeOrNotToBe {
    return {
         toBe:(otherVal:any)=>{
        if (val === otherVal){
            return true
        }
        else{
            throw new Error("Not Equal")
        }
        
    },
        notToBe:(otherVal:any)=>{
            if (otherVal!==val){
                return true
            }
            else{
                throw new Error("Equal")
            }
        }
    }
   
	
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */