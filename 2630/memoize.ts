type Fn = (...params: any) => any;

type ArgNode = Map<any, ArgNode>;

function memoize(fn: Fn): Fn {
    let cacheRoot: ArgNode = new Map();
    const outputSymbol = Symbol('output');

    return function (...args: any[]) {
        let node = cacheRoot;
        for (const arg of args) {
            if (!node.has(arg)) {
                node.set(arg, new Map());
            }
            node = node.get(arg)!;
        }

        if (!node.has(outputSymbol)) node.set(outputSymbol, fn(...args));
        return node.get(outputSymbol);
    };
}

/**
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1

 */


