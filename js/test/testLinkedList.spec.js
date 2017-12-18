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
  it('ll pop shifts head properly', function(){
    let ll = new linked.LinkedList()
    ll.push('potato')
    ll.push('cabbage')
    ll.pop()
    expect(ll.head.value).to.equal('potato')
  })
  it('ll pop on empty shows list empty', function(){
    let ll = new linked.LinkedList()
    expect(ll.pop()).to.equal('List is empty')
  })
  it('empty ll size returns 0', function(){
    let ll = new linked.LinkedList()
    expect(ll.size).to.equal(0)
  })
  it('ll size returns proper size', function(){
    let ll = new linked.LinkedList()
    for(let i = 0; i < 10; i ++ ){
      ll.push(i)
    }
    expect(ll.size).to.equal(10)
  })
  it('ll search empty return null', function(){
    let ll = new linked.LinkedList()
    expect(ll.search(2)).to.equal('List is empty.')
  })
  it('ll search with one node return node', function(){
    let ll = new linked.LinkedList()
    ll.push(1)
    expect(ll.search(1)).to.equal(ll.head)
  })
  it('ll search with bad value return not found', function(){
    let ll = new linked.LinkedList()
    ll.push(1)
    expect(ll.search(2)).to.equal('Node not found.')
  })
  it('ll remove removes number', function(){
    let ll = new linked.LinkedList()
    for(let i = 0; i < 10; i ++ ){
      ll.push(i)
    }
    ll.remove(2)
    expect(ll.search(2)).to.equal('Node not found.')
  })
  it('ll display on empty is undefined', function(){
    let ll = new linked.LinkedList()
    expect(ll.display()).to.equal(undefined)
  })
  it('ll display on lists list', function(){
    let ll = new linked.LinkedList()
    for(let i = 0; i < 10; i ++ ){
      ll.push(i)
    }
    expect(ll.display()).to.equal('9, 8, 7, 6, 5, 4, 3, 2, 1, 0')
  })
})
