
class Dsu {
    private var parentOrSize: [Int]
    private let n: Int
    private var counter: Int

    init(_ n: Int) {
        self.n = n
        self.counter = n
        self.parentOrSize = Array(repeating: -1, count: n)
    }

    var connected: Int { counter }

    func isRoot(_ node: Int) -> Bool {
        assert(node >= 0 && node < n)
        return parentOrSize[node] < 0
    }

    func findSet(_ node: Int) -> Int {
        if isRoot(node) {
            return node
        }
        parentOrSize[node] = findSet(parentOrSize[node])
        return parentOrSize[node]
    }

    func unionSet(_ x: Int, _ y: Int) -> Int {
        var xRoot = findSet(x), yRoot = findSet(y)

        if xRoot == yRoot {
            return xRoot
        }

        if size(xRoot) < size(yRoot) {
            swap(&xRoot, &yRoot)
        }
        parentOrSize[xRoot] += parentOrSize[yRoot]
        parentOrSize[yRoot] = xRoot
        counter -= 1
        return xRoot
    }

    func size(_ node: Int) -> Int {
        let root = findSet(node)
        return -parentOrSize[root]
    }
}
