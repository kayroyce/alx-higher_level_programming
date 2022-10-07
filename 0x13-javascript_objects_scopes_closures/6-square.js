#!/usr/bin/node

const Rectangle = require('./4-rectangle');

class Square extends Rectangle {
    constructor(size) {
        super(size, size)
    }

    charPrint(c) {
        for(let i = 0; i < this.width; i++) {
            if(c === undefined) {
                console.log('X' .repeat(this.height));
            }
            else {
            console.log('X' .repeat(this.height));
            }
        }
    }
}

module.exports = Square;