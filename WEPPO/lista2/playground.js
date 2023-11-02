var foo = {
        _i : 0,
    get bar() {
        return foo._i;
    },
    set bar(i) {
        foo._i = i;
    }
    }
    Object.defineProperty( foo, 'qux', {
        get : function() {
        return 17;
    }
    });
    Object.defineProperty( foo, 'baz', {
        value : function() {
        return 34;
    }
    });
    console.log(foo.bar);
    console.log( foo.qux );
    console.log( foo.baz() );

    console.log(foo);