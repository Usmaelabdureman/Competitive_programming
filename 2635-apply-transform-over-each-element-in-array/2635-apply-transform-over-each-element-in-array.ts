function map(arr: number[], fn: (n: number, i: number) => number): number[] {
  const result: number[] = [];

  for (let i = 0; i < arr.length; i++) {
    const transformedValue = fn(arr[i], i);
    result.push(transformedValue);
  }

  return result;
}
