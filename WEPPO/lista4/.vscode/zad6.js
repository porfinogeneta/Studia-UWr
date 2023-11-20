function Tree(val, left, right) {
    this.left = left;
    this.right = right;
    this.val = val;
}
// Tree.prototype[Symbol.iterator] = function*() {
//     yield this.val;
//     if ( this.left ) yield* this.left;
//     if ( this.right ) yield* this.right;
// }
var root = new Tree( 1, new Tree( 2, new Tree( 3 ) ), new Tree( 4 ));

// for ( var e of root ) {
//     console.log( e );
// }
// 1 2 3 4

/*
        1
       / \
      2   4
     / \
    3   5
       / \
      6   7
     /     \
    8       9
*/

const tree = new Tree(
    1,
    new Tree(
      2,
      new Tree(3, null, null),
      new Tree(
        5,
        new Tree(6, new Tree(8, null, null)),
        new Tree(7, null, new Tree(9, null, null))
      )
    ),
    new Tree(4, null, null)
  );

Tree.prototype[Symbol.iterator] = function*() {
    let queue = []
    let current = this
    // dokładamy węzeł do kolejki
    // index, delete_count, element
    queue.splice(0, 0, this)
    while (queue.length > 0){
        current = queue[0]
        queue.splice(0,1) // usunięcie pierwszego node z kolejki
        // current = queue.pop()
        if (current.left){
            // dodanie na koniec kolejki
            queue.splice(queue.length, 0, current.left)
            // queue.push(current.left)
        }
        if (current.right){
            // dodanie na koniec kolejki
            queue.splice(queue.length,0, current.right)
            // queue.push(current.right)
        }
        // console.log("Current queue");
        // queue.forEach(nd => console.log(nd.val));
        // console.log('End of queue')
        yield current.val
    }
}

for ( var e of tree ) {
    console.log( e );
}

// Co by się stało, gdyby zamiast kolejki użyć stosu
// (dodawanie elementów na koniec stosu, ściągane elementów z końca stosu)
// Implementacja 'stosowa' sprawia, że zamienia nam się to na DFS.