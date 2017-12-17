'use strict'

let linked = require('../LinkedList')
let chai = require('chai')
let expect = chai.expect

describe('LL JS tests', function(){
  it('Linked list has head', function(){
    let ll = new linked.LinkedList()
    expect(ll.head).to.equal(null)
  })
  it('ll push adds new item', function(){
    let ll = new linked.LinkedList()
    ll.push(2)
    expect(ll.head.value).to.equal(2)
  })
  it('ll push 2 items adds them to list', function(){
    let ll = new linked.LinkedList()
    ll.push(2)
    ll.push(4)
    expect(ll.head.next.value).to.equal(2)
  })
  it('ll pop removes head', function(){
    let ll = new linked.LinkedList()
    ll.push('tugboat')
    ll.pop()
    expect(ll.head).to.equal(null)
  })
  it('ll pop returns value', function(){
    let ll = new linked.LinkedList()
    ll.push('tugboat')
    expect(ll.pop()).to.equal('tugboat')
  })

})
