
class Trie {
    
    private var children: [Trie?]
    
    init() {
        children = Array(repeating: nil, count: 2)
    }
    
     func insert(_ num: Int) {
         var root = self
         for i in (0..<32).reversed() {
             let bit = (num >> i) & 1
             if root.children[bit] == nil {
                 root.children[bit] = Trie()
             }
             root = root.children[bit]!
         }
    }
}
