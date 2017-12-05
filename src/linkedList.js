'use strict'

class Node{

  constructor(val){
    this.value = val
    this.next = null
  }
}

class LinkedList{

  constructor(){
    this.head = null
    this.size = 0
  }

  push(val){
    let newNode = new Node(val)
    this.head = newNode
    this.size ++

  }

  pop(){
    let temp = this.head.value
    this.head = this.head.next
    this.size --
    return temp

  }

  size(){
    return this.size
  }

  search(val){
    let tempNode = this.head
    while(tempNode !== null){
      if (tempNode.val === val){
        return tempNode
      }
      else{
        tempNode = tempNode.next
      }
    }
    return
  }

  remove(val){
    let curr = this.head
    while (curr !== null ){
      if (curr.next === val){
        curr.next = curr.next.next
        this.size --
        return
      }
      curr = curr.next
    }
  }

  display(){

  }

}

//
// push(val) will insert the value ‘val’ at the head of the list
// pop() will pop the first value off the head of the list and return it. Raises an exception with an appropriate message if there are no values to return.
// size() will return the length of the list
// search(val) will return the node containing ‘val’ in the list, if present, else None
// remove(node) will remove the given node from the list, wherever it might be (node must be an item in the list). If the node is not in the list, it should raise an exception with an appropriate message.
// display() will return a unicode string representing the list as if it were a Python tuple literal: “(12, ‘sam’, 37, ‘tango’)”
